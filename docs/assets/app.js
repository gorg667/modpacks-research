/* Minecraft Modpack Guide — client JS: filters, table sort, quiz */
(function () {
  "use strict";

  /* ---------- index: filter / sort ---------- */
  const grid = document.getElementById("pack-grid");
  if (grid) {
    const cards = Array.from(grid.querySelectorAll(".pack-card"));
    const $ = (id) => document.getElementById(id);
    const inputs = ["f-search", "f-cat", "f-loader", "f-diff", "f-sort"].map($);
    const mcNum = (v) => { const m = v.match(/1\.(\d+)(?:\.(\d+))?/); return m ? 1000 * +m[1] + (+m[2] || 0) : 0; };
    function apply() {
      const q = $("f-search").value.trim().toLowerCase();
      const cat = $("f-cat").value, ld = $("f-loader").value, df = $("f-diff").value, sort = $("f-sort").value;
      let shown = 0;
      cards.forEach((c) => {
        const ok = (!q || c.dataset.name.includes(q) || c.dataset.category.toLowerCase().includes(q)) &&
          (!cat || c.dataset.category === cat) && (!ld || c.dataset.loader === ld) && (!df || c.dataset.difficulty === df);
        c.classList.toggle("hidden", !ok);
        if (ok) shown++;
      });
      const sorted = cards.slice().sort((a, b) => {
        if (sort === "name") return a.dataset.name.localeCompare(b.dataset.name);
        if (sort === "mc") return mcNum(b.dataset.mc) - mcNum(a.dataset.mc) || b.dataset.score - a.dataset.score;
        return b.dataset.score - a.dataset.score;
      });
      sorted.forEach((c) => grid.appendChild(c));
      $("f-count").textContent = shown + " of " + cards.length + " packs";
    }
    inputs.forEach((el) => el.addEventListener("input", apply));
    // allow ?cat=… deep links
    const params = new URLSearchParams(location.search);
    ["cat", "loader", "diff", "search"].forEach((k) => { if (params.get(k)) $("f-" + k).value = params.get(k); });
    apply();
  }

  /* ---------- compare: sortable table ---------- */
  const cmp = document.getElementById("cmp");
  if (cmp) {
    const ths = cmp.querySelectorAll("th");
    ths.forEach((th, idx) => th.addEventListener("click", () => {
      const asc = th.classList.contains("sorted") && !th.classList.contains("asc");
      ths.forEach((t) => t.classList.remove("sorted", "asc"));
      th.classList.add("sorted"); if (asc) th.classList.add("asc");
      const rows = Array.from(cmp.tBodies[0].rows);
      const val = (r) => { const td = r.cells[idx]; return td.dataset.v !== undefined ? +td.dataset.v : td.textContent.trim().toLowerCase(); };
      rows.sort((a, b) => { const x = val(a), y = val(b); const c = typeof x === "number" ? x - y : String(x).localeCompare(String(y)); return asc ? c : -c; });
      rows.forEach((r) => cmp.tBodies[0].appendChild(r));
    }));
  }

  /* ---------- quiz ---------- */
  const form = document.getElementById("quiz-form");
  if (form) {
    const Q = [
      { id: "experience", title: "How much modded Minecraft have you played?", opts: [
        ["none", "None — I've only played vanilla"], ["some", "A little — one or two packs, or I know a few mods"],
        ["lots", "Plenty — I know AE2 / Create / Mekanism etc."], ["veteran", "I've finished expert packs and want more"]] },
      { id: "vibe", title: "What do you want the game to feel like?", opts: [
        ["build", "Build factories & automate everything"], ["explore", "Explore, fight bosses, find loot"],
        ["cozy", "Relax, farm, decorate, chill"], ["survive", "Struggle to survive — tension and danger"],
        ["everything", "A bit of everything, no strict theme"], ["pokemon", "Catch and battle Pokémon"]] },
      { id: "structure", title: "How much hand-holding do you want?", opts: [
        ["guided", "A quest book that tells me exactly what to do next"], ["loose", "Some goals, but freedom to wander"],
        ["sandbox", "None — just give me the mods"]] },
      { id: "time", title: "Realistically, how long will you play this pack?", opts: [
        ["short", "A weekend or two (< 30 h)"], ["medium", "A month of evenings (30–150 h)"],
        ["long", "Several months (150–500 h)"], ["forever", "A year+ — I want a lifestyle, not a game"]] },
      { id: "difficulty", title: "How much challenge do you want from recipes and progression?", opts: [
        ["chill", "Easy — let me have fun fast"], ["some", "Moderate — earn the good stuff"],
        ["hard", "Hard — I want to be forced to automate"], ["brutal", "Brutal — GregTech-level engineering"]] },
      { id: "players", title: "Who are you playing with?", opts: [
        ["solo", "Solo"], ["duo", "One or two friends"], ["group", "A group / server (4+)"]] },
      { id: "hardware", title: "How is your PC?", opts: [
        ["low", "Weak — 8 GB RAM or a laptop with integrated graphics"], ["mid", "Average — 16 GB RAM, a mid-range GPU"],
        ["high", "Strong — 32 GB+ RAM, modern GPU"]] },
      { id: "version", title: "Do you care about the Minecraft version?", opts: [
        ["new", "Yes — I want modern (1.20+) features and mods"], ["any", "Not really, gameplay matters more"],
        ["old", "I actually prefer the classic era (1.7.10 / 1.12.2)"]] },
    ];
    form.innerHTML = Q.map((q, i) => `<fieldset><legend>${i + 1}. ${q.title}</legend>` +
      q.opts.map(([v, l], j) => `<label><input type="radio" name="${q.id}" value="${v}" ${j === 0 && false ? "checked" : ""} required> ${l}</label>`).join("") + `</fieldset>`).join("") +
      `<button class="btn primary" type="submit">Show my matches</button>`;

    const RAM_GB = (s) => { const m = String(s).match(/(\d+)/g); return m ? Math.max(...m.map(Number)) : 6; };
    const HOURS = (s) => { const m = String(s).match(/(\d[\d,]*)/g); return m ? Math.max(...m.map((x) => +x.replace(/,/g, ""))) : 60; };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const a = Object.fromEntries(new FormData(form).entries());
      const res = await fetch("assets/packs.json"); const packs = await res.json();
      const scored = packs.map((p) => {
        const q = p.quiz || {}; const r = p.ratings; const why = []; let s = 0;
        // vibe
        const vibes = q.vibes || [];
        if (vibes.includes(a.vibe)) { s += 30; why.push("matches the vibe you asked for"); }
        else if (a.vibe === "everything" && vibes.length >= 3) { s += 18; }
        else if (a.vibe === "pokemon") { s -= 40; }
        else if (vibes.includes("pokemon") && a.vibe !== "pokemon") { s -= 40; }
        // structure
        const st = q.structure || "guided";
        if (st === a.structure) { s += 12; why.push(a.structure === "guided" ? "strong quest book" : a.structure === "sandbox" ? "no imposed progression" : "loose, optional goals"); }
        else if ((st === "loose") || (a.structure === "loose")) s += 5;
        else s -= 6;
        // difficulty
        const dmap = { Beginner: 0, Easy: 1, Moderate: 2, Hard: 3, Expert: 4, Brutal: 5 };
        const want = { chill: 1, some: 2, hard: 3.5, brutal: 5 }[a.difficulty];
        const have = dmap[p.difficulty] ?? 2; const dd = Math.abs(want - have);
        s += dd < 1 ? 16 : dd < 2 ? 6 : dd < 3 ? -8 : -25;
        if (dd < 1) why.push(`${p.difficulty.toLowerCase()} difficulty is what you wanted`);
        // experience gate
        const exp = { none: 0, some: 1, lots: 2, veteran: 3 }[a.experience];
        if (exp === 0) { s += (r.beginner - 5) * 3; if (r.beginner >= 8) why.push("very newcomer-friendly"); if (have >= 4) s -= 25; }
        if (exp === 3 && have <= 1) s -= 10;
        if (exp >= 2 && r.content >= 9) s += 4;
        // time
        const h = HOURS(p.playtime);
        const tfit = { short: h <= 40, medium: h > 20 && h <= 200, long: h > 100 && h <= 800, forever: h > 300 }[a.time];
        if (tfit) { s += 10; why.push(`fits a ${a.time === "forever" ? "very long" : a.time}-term commitment`); } else s -= 8;
        if (a.time === "short" && h > 300) s -= 20;
        // players
        if (a.players === "group") { s += (r.multiplayer - 6) * 2.5; if (r.multiplayer >= 9) why.push("shines on a server"); }
        if (a.players === "solo" && r.multiplayer >= 9 && q.solo_ok === false) s -= 10;
        // hardware
        const ram = RAM_GB(p.ram);
        if (a.hardware === "low") { s += (r.performance - 6) * 3; if (ram >= 10) { s -= 20; } else if (r.performance >= 8) why.push("light on hardware"); }
        if (a.hardware === "mid" && ram >= 12) s -= 6;
        // version
        const mc = (p.mc_version.match(/1\.(\d+)/) || [0, 12])[1] | 0;
        if (a.version === "new") { if (mc >= 20) { s += 8; } else if (mc >= 18) s += 2; else s -= 14; }
        if (a.version === "old") { if (mc <= 12) { s += 10; why.push("classic-era Minecraft"); } else s -= 3; }
        // quality baseline
        s += (p.score - 7) * 4;
        return { p, s, why };
      }).sort((x, y) => y.s - x.s).slice(0, 5);

      const out = document.getElementById("quiz-result");
      out.hidden = false;
      out.innerHTML = `<h2>Your top matches</h2>` + scored.map((x, i) => `
        <div class="result-card">
          <div class="rank">#${i + 1} match</div>
          <h3><span class="tier tier-${x.p.tier}">${x.p.tier}</span> <a href="packs/${x.p.slug}.html">${x.p.name}</a> <span class="score-pill">${x.p.score}</span></h3>
          <p>${x.p.verdict}</p>
          <p class="why">${x.why.length ? "Why: " + x.why.join(" · ") : "A solid all-round fit."} — ${x.p.mc_version} ${x.p.loader}, ${x.p.ram} RAM, ${x.p.playtime}.</p>
        </div>`).join("") +
        `<p class="muted small">Scores are heuristic. If nothing here excites you, use the <a href="index.html#browse">filterable browser</a> or read <a href="guides/how-to-choose.html">How to choose a modpack</a>.</p>`;
      out.scrollIntoView({ behavior: "smooth" });
    });
  }
})();
