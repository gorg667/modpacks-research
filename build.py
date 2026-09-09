#!/usr/bin/env python3
"""
Static site generator for the Minecraft Modpack Guide.

Input:
  content/packs/*.md   -> one modpack review each (YAML frontmatter + markdown body)
  content/guides/*.md  -> guide articles (YAML frontmatter + markdown body)
  content/site.yaml    -> site-wide config (title, tagline, nav, quick picks)
  templates/*.html     -> simple {{placeholder}} templates
  static/*             -> copied to docs/assets/
Output:
  docs/                -> GitHub Pages ready static site (committed; no build step on GH)

Run:  python3 build.py
"""
import json, re, shutil, datetime, html
from pathlib import Path
import markdown, yaml

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
TPL = ROOT / "templates"
OUT = ROOT / "docs"

MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list", "md_in_html", "sane_lists"])

def read_md(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"missing frontmatter: {path}")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def render_md(body):
    MD.reset()
    return MD.convert(body)

def tpl(name):
    return (TPL / name).read_text(encoding="utf-8")

def fill(template, **kw):
    out = template
    for k, v in kw.items():
        out = out.replace("{{" + k + "}}", str(v))
    return re.sub(r"\{\{[a-zA-Z0-9_]+\}\}", "", out)

def esc(s):
    return html.escape(str(s), quote=True)

SITE = yaml.safe_load((CONTENT / "site.yaml").read_text(encoding="utf-8"))
BASE = SITE.get("base_url", "")

def page(title, body_html, rel="", description="", extra_head="", active=""):
    nav = "".join(
        f'<a href="{rel}{esc(i["href"])}" class="{"active" if active == i["id"] else ""}">{esc(i["label"])}</a>'
        for i in SITE["nav"])
    return fill(tpl("base.html"), title=esc(title), site_title=esc(SITE["title"]),
                description=esc(description or SITE["tagline"]), body=body_html, rel=rel, nav=nav,
                year=datetime.date.today().year, updated=SITE.get("updated", ""), extra_head=extra_head, base=BASE)

# ---------- helpers ----------
def score_bar(label, val):
    return (f'<div class="score-row"><span class="score-label">{esc(label)}</span>'
            f'<span class="score-bar"><span class="score-fill" style="width:{int(val)*10}%"></span></span>'
            f'<span class="score-num">{val}/10</span></div>')

def tier_badge(tier):
    return f'<span class="tier tier-{esc(tier)}">{esc(tier)}</span>'

def chip(text, cls=""):
    return f'<span class="chip {cls}">{esc(text)}</span>'

def pack_card(p, prefix="packs/"):
    tags = "".join(chip(t) for t in p.get("tags", [])[:4])
    return f"""
<a class="card pack-card" href="{prefix}{esc(p['slug'])}.html" data-category="{esc(p['category'])}" data-loader="{esc(p['loader'])}" data-difficulty="{esc(p['difficulty'])}" data-tier="{esc(p['tier'])}" data-score="{p['score']}" data-mc="{esc(p['mc_version'])}" data-name="{esc(p['name'].lower())} {esc(' '.join(p.get('tags', [])).lower())}">
  <div class="card-head">{tier_badge(p['tier'])}<h3>{esc(p['name'])}</h3><span class="score-pill">{p['score']}</span></div>
  <p class="card-verdict">{esc(p['verdict'])}</p>
  <div class="card-meta">
    <span title="Minecraft version and loader">🧩 {esc(p['mc_version'])} · {esc(p['loader'])}</span>
    <span title="Difficulty">⚔️ {esc(p['difficulty'])}</span>
    <span title="Recommended RAM">🧠 {esc(p['ram'])}</span>
    <span title="Estimated time to finish">⏱ {esc(p['playtime'])}</span>
  </div>
  <div class="card-tags">{tags}</div>
</a>"""

WEIGHTS = {"content": 1.5, "polish": 1.2, "progression": 1.5, "performance": 0.8,
           "beginner": 0.6, "multiplayer": 0.8, "longevity": 1.0}
RUBRIC = [("content", "Content depth"), ("polish", "Polish & stability"), ("progression", "Progression design"),
          ("performance", "Performance (lighter = higher)"), ("beginner", "Beginner friendliness"),
          ("multiplayer", "Multiplayer suitability"), ("longevity", "Longevity / replay value")]

# ---------- packs ----------
def build_packs():
    packs = []
    for f in sorted((CONTENT / "packs").glob("*.md")):
        meta, body = read_md(f)
        meta["slug"] = f.stem
        meta["body_html"] = render_md(body)
        r = meta["ratings"]
        if "score" not in meta:
            meta["score"] = round(sum(r[k] * WEIGHTS[k] for k in WEIGHTS) / sum(WEIGHTS.values()), 1)
        packs.append(meta)
    packs.sort(key=lambda p: (-p["score"], p["name"]))
    return packs

def pack_page(p, all_packs):
    r = p["ratings"]
    scores = "".join(score_bar(lbl, r[k]) for k, lbl in RUBRIC)
    facts = [("Minecraft", p["mc_version"]), ("Loader", p["loader"]), ("Java", p.get("java", "—")),
             ("Mods", p.get("mod_count", "—")), ("Category", p["category"]), ("Difficulty", p["difficulty"]),
             ("RAM (client)", p["ram"]), ("Time to finish", p["playtime"]), ("Status", p.get("status", "—")),
             ("Author / team", p.get("author", "—")), ("First released", p.get("released", "—"))]
    facts_html = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in facts)
    links = "".join(f'<a class="btn" href="{esc(l["url"])}" target="_blank" rel="noopener">{esc(l["label"])} ↗</a>' for l in p.get("links", []))
    pros = "".join(f"<li>{esc(x)}</li>" for x in p.get("pros", []))
    cons = "".join(f"<li>{esc(x)}</li>" for x in p.get("cons", []))
    tags = "".join(chip(t) for t in p.get("tags", []))
    mine = set(p.get("tags", []))
    related = [q for q in all_packs if q["slug"] != p["slug"]]
    related.sort(key=lambda q: -(len(set(q.get("tags", [])) & mine) * 2 + (q["category"] == p["category"]) * 3))
    related = related[:4]
    related_html = "".join(f'<a class="related" href="{esc(q["slug"])}.html">{tier_badge(q["tier"])} {esc(q["name"])} <span class="muted">{q["score"]}</span></a>' for q in related)
    best_for = "".join(f"<li>{esc(x)}</li>" for x in p.get("best_for", []))
    avoid_if = "".join(f"<li>{esc(x)}</li>" for x in p.get("avoid_if", []))
    body = fill(tpl("pack.html"), name=esc(p["name"]), tagline=esc(p.get("tagline", "")), verdict=esc(p["verdict"]),
                tier=tier_badge(p["tier"]), score=p["score"], scores=scores, facts=facts_html, links=links,
                pros=pros, cons=cons, tags=tags, body=p["body_html"], related=related_html,
                best_for=best_for, avoid_if=avoid_if, category=esc(p["category"]),
                hero_class="hero-" + re.sub(r"[^a-z]", "", p["category"].lower()),
                updated=esc(p.get("updated", SITE.get("updated", ""))))
    desc = f"{p['name']} review: {p['verdict']} ({p['mc_version']} {p['loader']}, {p['difficulty']} difficulty, {p['ram']} RAM)."
    return page(f"{p['name']} — Review", body, rel="../", description=desc, active="packs")

# ---------- guides ----------
def build_guides():
    guides = []
    for f in sorted((CONTENT / "guides").glob("*.md")):
        meta, body = read_md(f)
        meta["slug"] = f.stem
        meta["body_html"] = render_md(body)
        guides.append(meta)
    guides.sort(key=lambda g: g.get("order", 99))
    return guides

def guide_page(g, guides):
    toc = "".join(f'<a href="{esc(x["slug"])}.html" class="{"active" if x["slug"] == g["slug"] else ""}">{esc(x["title"])}</a>' for x in guides)
    body = fill(tpl("guide.html"), title=esc(g["title"]), summary=esc(g.get("summary", "")), body=g["body_html"],
                toc=toc, updated=esc(g.get("updated", SITE.get("updated", ""))), reading=esc(g.get("reading", "")))
    return page(g["title"], body, rel="../", description=g.get("summary", ""), active="guides")

# ---------- index & misc ----------
def build_index(packs, guides):
    cats = sorted({p["category"] for p in packs})
    loaders = sorted({p["loader"] for p in packs})
    order = ["Beginner", "Easy", "Moderate", "Hard", "Expert", "Brutal"]
    diffs = [d for d in order if any(p["difficulty"] == d for p in packs)]
    opts = lambda vals: "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in vals)
    tiers = {}
    for p in packs:
        tiers.setdefault(p["tier"], []).append(p)
    tier_rows = ""
    for t in ["S", "A", "B", "C"]:
        if t in tiers:
            items = "".join(f'<a href="packs/{esc(p["slug"])}.html" class="tier-item">{esc(p["name"])}<span>{p["score"]}</span></a>' for p in tiers[t])
            tier_rows += f'<div class="tier-row"><div class="tier-cell tier-{t}">{t}</div><div class="tier-items">{items}</div></div>'
    by_slug = {p["slug"]: p for p in packs}
    picks = "".join(
        f'<a class="pick" href="packs/{esc(pk["slug"])}.html"><span class="pick-label">{esc(pk["label"])}</span><strong>{esc(by_slug[pk["slug"]]["name"])}</strong><span class="muted">{esc(pk["why"])}</span></a>'
        for pk in SITE["quick_picks"] if pk["slug"] in by_slug)
    guide_links = "".join(f'<a class="card guide-card" href="guides/{esc(g["slug"])}.html"><h3>{esc(g["title"])}</h3><p>{esc(g.get("summary", ""))}</p></a>' for g in guides)
    body = fill(tpl("index.html"), cards="".join(pack_card(p) for p in packs), cat_opts=opts(cats),
                loader_opts=opts(loaders), diff_opts=opts(diffs), count=len(packs), tier_rows=tier_rows,
                picks=picks, guides=guide_links, intro_html=render_md(SITE.get("intro_md", "")),
                updated=esc(SITE.get("updated", "")))
    return page("Best Minecraft Modpacks — reviews, tier list & quiz", body, rel="", description=SITE["tagline"], active="home")

def build_packs_index(packs):
    cards = "".join(pack_card(p, prefix="") for p in packs)
    body = f"""<section class="section"><h1>All {len(packs)} reviewed modpacks</h1>
<p class="lead">Sorted by overall score. Use the <a href="../index.html#browse">filterable browser</a> on the home page to narrow by category, loader or difficulty.</p>
<div class="grid">{cards}</div></section>"""
    return page("All modpack reviews", body, rel="../", active="packs")

def build_compare(packs):
    rows = ""
    for p in packs:
        r = p["ratings"]
        rows += (f'<tr><td><a href="packs/{esc(p["slug"])}.html">{esc(p["name"])}</a></td><td>{tier_badge(p["tier"])}</td>'
                 f'<td data-v="{p["score"]}"><strong>{p["score"]}</strong></td><td>{esc(p["category"])}</td><td>{esc(p["mc_version"])}</td>'
                 f'<td>{esc(p["loader"])}</td><td>{esc(p["difficulty"])}</td><td>{esc(p["ram"])}</td><td>{esc(p["playtime"])}</td>'
                 + "".join(f'<td data-v="{r[k]}">{r[k]}</td>' for k, _ in RUBRIC) + "</tr>")
    return page("Compare all modpacks", fill(tpl("compare.html"), rows=rows, count=len(packs)), rel="", active="compare",
                description="Side-by-side sortable comparison of every reviewed Minecraft modpack: version, loader, RAM, difficulty and rubric scores.")

def build_quiz():
    return page("Which modpack should I play? (quiz)", tpl("quiz.html"), rel="", active="quiz",
                description="Answer 8 quick questions and get a personalised Minecraft modpack recommendation.")

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    packs, guides = build_packs(), build_guides()
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    for f in (ROOT / "static").glob("*"):
        shutil.copy(f, OUT / "assets" / f.name)
    (OUT / ".nojekyll").touch()
    write(OUT / "index.html", build_index(packs, guides))
    write(OUT / "packs" / "index.html", build_packs_index(packs))
    for p in packs:
        write(OUT / "packs" / f"{p['slug']}.html", pack_page(p, packs))
    for g in guides:
        write(OUT / "guides" / f"{g['slug']}.html", guide_page(g, guides))
    write(OUT / "compare.html", build_compare(packs))
    write(OUT / "quiz.html", build_quiz())
    keys = ["slug", "name", "category", "loader", "mc_version", "difficulty", "ram", "playtime", "tier", "score", "verdict", "tags", "ratings"]
    data = [{k: p[k] for k in keys} | {"quiz": p.get("quiz", {})} for p in packs]
    write(OUT / "assets" / "packs.json", json.dumps(data, indent=1, ensure_ascii=False))
    write(OUT / "404.html", page("Not found", '<section class="section"><h1>404</h1><p>That page doesn\'t exist. <a href="index.html">Back to the guide</a>.</p></section>'))
    urls = ["index.html", "compare.html", "quiz.html", "packs/index.html"] + [f"packs/{p['slug']}.html" for p in packs] + [f"guides/{g['slug']}.html" for g in guides]
    if BASE:
        write(OUT / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
              + "".join(f"<url><loc>{BASE}/{u}</loc></url>" for u in urls) + "</urlset>")
    print(f"built {len(packs)} packs, {len(guides)} guides -> {OUT}")

if __name__ == "__main__":
    main()
