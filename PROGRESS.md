# PROGRESS LOG — Minecraft Modpack Guide Website

> READ THIS FIRST after any context compaction. It documents the plan, decisions, and current state.

## Goal
The most comprehensive, well-researched review/guide of the best Minecraft modpacks, delivered as a
GitHub Pages–hostable static website (in `/docs`, no build step, plain HTML/CSS/JS).

## User constraints
- Push directly to `main`, no branches/PRs.
- Push after EVERY meaningful step (credits may run out at any time).
- Keep this file updated with reasoning + state so a fresh context can continue.

## Architecture decisions
- Static site in `docs/` (GH Pages: Settings → Pages → Deploy from branch `main`, folder `/docs`).
- No framework/build: `index.html`, `assets/style.css`, `assets/app.js`, one page per modpack in `docs/packs/*.html`.
- Data-driven: `docs/assets/packs.json` holds structured data (loader, version, category, difficulty, ratings,
  hardware needs, links) → used for filter/sort table on index and comparison page.
- Research notes kept in `research/*.md` (raw facts gathered via web search, with source URLs) so writing can
  be verified/continued.
- `.nojekyll` in docs so underscores/files aren't mangled.

## Plan (checkbox = done)
- [x] 1. Skeleton + push
- [x] 2. Research: modpack landscape (landscape.md)
- [x] 3. Research: individual packs (research/packs/*.md — enough to write; can top-up later)
- [ ] 4. Write packs.json (structured data)
- [ ] 5. Build site shell: index (hero, methodology, tier list, filterable table), CSS, JS
- [ ] 6. Write per-pack review pages (detailed: overview, progression, highlights, cons, perf, who it's for, how to install)
- [ ] 7. Guide pages: how to choose, launchers, performance/JVM tuning, server hosting, glossary, FAQ
- [ ] 8. Comparison page / quiz ("which pack for me")
- [ ] 9. Polish: SEO meta, OG tags, sitemap, 404, accessibility, mobile
- [ ] 10. Final verification (serve locally, check links) + README

## Target modpack list (candidates, refine during research)
Kitchen-sink/tech: All the Mods 9 / ATM9: To the Sky / ATM10, FTB Skies, FTB StoneBlock 3, FTB Inferno, FTB OceanBlock, Direwolf20, Enigmatica 6/9 (+Expert), Craft to Exile 2, Prominence II, Create: Above and Beyond, Create: Arcane Engineering, Create: Astral, GregTech: New Horizons, Nomifactory (CEu), Divine Journey 2, Project Ozone 3, SevTech: Ages, Sky Factory 4, Better Minecraft, Medieval MC, Cottage Witch, Vault Hunters 3rd Edition, RLCraft, DawnCraft, Better MC RPG, Fabulously Optimized, Additive, Simply Optimized, Cobblemon (Cobblemon: Star Academy / Cobbleverse), Pixelmon, TerraFirmaGreg, TerraFirmaCraft packs, Rebirth of the Night, Blightfall (historic), Crash Landing (historic), Regrowth, Life in the Village 3, Valhelsia 6, Steampunk LPS, Hexxit Updated, Tekkit 2, Crazy Craft, Mineshafts & Monsters, Wynncraft? (no—server), Deceased Craft, Zombie apocalypse packs, One Block MC, Statech Industry, Monifactory, Meatballcraft, Integrated MC, Prodigium, All of Fabric 7, Better Adventures+, BigChadGuys+ (Cobblemon), Ragnamod VI, Roguelike Adventures and Dungeons 2, MC Eternal 2, Insane Craft, Blood N Bones (historic), Agrarian Skies (historic).

## Current state
(update below after each step)
- Step 1: skeleton created.
- Steps 2-3 done (research/*.md). Next: packs.json + site shell. 
- DESIGN DECISION for site: dark "obsidian" theme, accent colors per category; pages: index.html (hero, quick picks, tier list, filter table), packs/<slug>.html (full reviews), guides/*.html, compare.html, quiz.html, glossary.html, faq.html, about/methodology.html.
- Rating rubric (each 1-10): Content depth, Polish/stability, Progression design, Performance (higher = lighter), Beginner-friendliness, Multiplayer suitability, Longevity. Plus overall score + tier (S/A/B/C) + "Verdict" one-liner.

## STATE AFTER SANDBOX SWITCH (important)
- Uncommitted files are LOST on sandbox switch. Commit after EVERY file.
- Pipeline: `python3 build.py` (needs `pip install markdown pyyaml`) → docs/. Content in content/packs/*.md (schema = see all-the-mods-10.md frontmatter), content/guides/*.md, content/site.yaml. Templates in templates/, CSS/JS in static/.
- Quiz uses frontmatter `quiz: {vibes:[build|explore|cozy|survive|everything|pokemon], structure: guided|loose|sandbox, solo_ok: bool}`.
- Difficulty vocabulary: Beginner, Easy, Moderate, Hard, Expert, Brutal. Categories used: Kitchen Sink, Expert, Tech, Skyblock & Questing, RPG & Adventure, Hardcore Survival, Survival Horror, Cozy & Vanilla+, Pokémon, Performance.
- quick_picks slugs in site.yaml must exist: all-the-mods-10, better-minecraft-bmc4, gregtech-new-horizons, ftb-stoneblock-4, create-astral, prominence-2, homestead, cobbleverse, rlcraft, fabulously-optimized.
- Guides needed (placeholders exist): how-to-choose, methodology, glossary, faq, history. Planned extra: launchers-and-install, performance-tuning, servers, loaders-and-versions.
- Local preview: `cd docs && python3 -m http.server 8080` (Playwright chromium lacks libs in sandbox; use PlaywrightConsoleCapture tool for checks).
- Serve GH Pages from main:/docs.

## Review writing queue (✓ = committed)
✓ all-the-mods-10
Batch A (must for quick picks): better-minecraft-bmc4, gregtech-new-horizons, ftb-stoneblock-4, create-astral, prominence-2, homestead, cobbleverse, rlcraft, fabulously-optimized
Batch B: create-above-and-beyond, create-arcane-engineering, all-of-create, liminal-industries, meatballcraft, monifactory, nomifactory, terrafirmagreg, enigmatica-10, enigmatica-9-expert, enigmatica-2-expert, divine-journey-2, sevtech-ages, project-ozone-3
Batch C: vault-hunters-3, craft-to-exile-2, dawncraft, integrated-mc, roguelike-adventures-and-dungeons-2, deceasedcraft, cursed-walking, rebirth-of-the-night, nightfallcraft(?), ftb-oceanblock-2, ftb-skies, skyfactory-4, skyfactory-5, all-the-mods-9, atmons, bigchadguys-plus, pixelmon, sunlit-valley, statech-industry, direwolf20-1-21, mc-eternal-2, better-mc-fabric
