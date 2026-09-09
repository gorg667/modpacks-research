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
- [ ] 1. Skeleton + push
- [ ] 2. Research: modpack landscape (launchers, loaders, categories) → research/landscape.md
- [ ] 3. Research: individual packs (facts, versions, mod counts, sources) → research/packs/*.md
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
