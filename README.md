# Modpack Atlas — the in-depth guide to the best Minecraft modpacks

A static, GitHub-Pages-hosted site with 41 long-form modpack reviews, a tier list, a sortable comparison table, a recommendation quiz and seven guides (choosing, methodology, launchers, performance, glossary, FAQ, history).

**Live site:** https://gorg667.github.io/modpacks-research/

## Structure

- `content/packs/*.md` — one review per pack (YAML frontmatter + Markdown). Frontmatter schema: see any file; `ratings` drive the score, `quiz` drives the quiz.
- `content/guides/*.md` — guide articles.
- `content/site.yaml` — site title, nav, quick picks, intro.
- `templates/*.html`, `static/*` — templates, CSS, JS.
- `build.py` — generator. `pip install markdown pyyaml && python3 build.py` → writes `docs/`.
- `docs/` — the built site (committed; GitHub Pages serves `main:/docs`).
- `research/` — raw research notes with source URLs.
- `PROGRESS.md` — working log.

## Hosting on GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → Branch `main`, folder `/docs`. `docs/.nojekyll` is present.

## Licence

Text CC BY 4.0. Code MIT. Not affiliated with Mojang, Microsoft, CurseForge, Modrinth or any modpack team.
