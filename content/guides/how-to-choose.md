---
title: "How to choose a modpack"
summary: "A decision framework: figure out what you actually want, what your PC can run, who you're playing with — and then pick from the shortlist that fits."
order: 1
reading: "14 min read"
---

There are tens of thousands of modpacks on CurseForge and Modrinth. Almost all of them are noise: abandoned experiments, duplicate kitchen sinks, one-mod showcases, and (increasingly) AI-generated descriptions wrapped around a random mod list. The forty-odd packs reviewed on this site are the ones that a decade of community consensus, download data and our own evaluation say are worth your time. This guide is about choosing *among* them.

## Step 1 — Decide what kind of fun you want

Every good modpack is built around one of a handful of core fantasies. Name yours before you look at a single mod list.

| You want to… | The category | Start here |
|---|---|---|
| Automate everything, build factories, solve logistics | **Tech / Expert** | [Create: Astral](../packs/create-astral.html) (learn), [Nomifactory](../packs/nomifactory.html) (GregTech), [GTNH](../packs/gregtech-new-horizons.html) (lifetime) |
| Try a bit of every mod with friends | **Kitchen Sink** | [ATM10](../packs/all-the-mods-10.html), [Enigmatica 10](../packs/enigmatica-10.html), [Direwolf20](../packs/direwolf20-1-21.html) |
| Follow a designed progression to a finish line | **Skyblock & Questing** | [StoneBlock 4](../packs/ftb-stoneblock-4.html), [SkyFactory 4](../packs/skyfactory-4.html) |
| Fight bosses, level up, find loot | **RPG & Adventure** | [Craft to Exile 2](../packs/craft-to-exile-2.html), [Vault Hunters](../packs/vault-hunters-3.html), [Integrated MC](../packs/integrated-mc.html) |
| Be scared and struggle | **Hardcore / Horror** | [RLCraft](../packs/rlcraft.html), [Rebirth of the Night](../packs/rebirth-of-the-night.html), [DeceasedCraft](../packs/deceasedcraft.html) |
| Relax, farm, build, decorate | **Cozy & Vanilla+** | [Homestead](../packs/homestead.html), [Sunlit Valley](../packs/sunlit-valley.html), [Better Minecraft](../packs/better-minecraft-bmc4.html) |
| Catch Pokémon | **Pokémon** | [COBBLEVERSE](../packs/cobbleverse.html), [BigChadGuys+](../packs/bigchadguys-plus.html) |
| Just run vanilla well | **Performance** | [Fabulously Optimized](../packs/fabulously-optimized.html) |

If you honestly can't choose, that's what kitchen sinks are for — but be warned that "a bit of everything" packs are the ones people most often abandon at hour 20, because nothing pulls you forward.

## Step 2 — Be honest about experience

Modded Minecraft has a real skill curve, and packs assume different starting points:

- **Never modded:** Better Minecraft, Homestead, SkyFactory 4, COBBLEVERSE. These explain themselves.
- **Know a few mods (Create, some Mekanism, JEI):** StoneBlock 4, Create: Astral, ATM10, Craft to Exile 2, Vault Hunters.
- **Comfortable with AE2, automation, multiblocks:** Enigmatica 2: Expert, StaTech Industry, Liminal Industries, Above and Beyond.
- **Finished an expert pack:** Nomifactory, Monifactory, Divine Journey 2, MeatballCraft, TerraFirmaGreg.
- **Finished several and want the mountain:** GregTech: New Horizons.

Skipping rungs is the #1 cause of burnout. Nobody's first pack should be GTNH, and the GTNH wiki says so itself.

## Step 3 — Check your hardware

RAM allocated to Minecraft (not total system RAM) is the constraint that matters. Rules of thumb:

| Allocated RAM | What runs well |
|---|---|
| 3–4 GB | Fabulously Optimized, Nomifactory, RLCraft, SkyFactory 4 |
| 5–6 GB | Better Minecraft, Homestead, Create: Astral, StoneBlock 4, Cursed Walking, most 150–250-mod packs |
| 8 GB | Prominence II, DeceasedCraft, Enigmatica 10, All of Create, TerraFirmaGreg, most 1.20/1.21 packs |
| 10–12 GB | ATM10, ATM9, ATMons, MeatballCraft |

Never allocate more than ~half your physical RAM; the OS and the game's own off-heap memory need the rest. 16 GB of system RAM is the comfortable floor for modern big packs; 8 GB machines should stick to the top two rows. See the [performance guide](performance-tuning.html) for JVM flags and settings.

**Java version** follows Minecraft version: 1.7.10 and 1.12.2 → Java 8 (unless the pack ships a modernised loader like GTNH's lwjgl3ify or Cleanroom); 1.16–1.17 → Java 8/16; 1.18–1.20.1 → Java 17; 1.20.5+ and 1.21 → Java 21. Launchers usually handle this; "won't launch" is almost always a Java mismatch.

## Step 4 — Who's playing?

- **Solo:** anything, but packs with a strong quest book (StoneBlock 4, Astral, CtE2, E2E) hold attention best. Roguelike loops (Vault Hunters) and hardcore survival are fine solo but lose their social sparkle.
- **Two or three friends:** the sweet spot for expert and Create packs — labour divides naturally. A&B, Liminal Industries, Nomifactory, E2E, TerraFirmaGreg.
- **A server of mixed tastes:** kitchen sinks (ATM10, E10, ATM9), Vault Hunters, COBBLEVERSE, DeceasedCraft, Better Minecraft. Anything where each player can pursue something different.
- **Family / very mixed skill:** Better Minecraft, Homestead, SkyFactory 4, BigChadGuys+.

## Step 5 — Loader and version (matters less than you think)

**Forge, NeoForge and Fabric** are just the plumbing; the launcher handles it. What they *imply* matters:

- **NeoForge 1.21.x** is where new big packs live in 2026 (ATM10, StoneBlock 4, E10, All of Create). Newest mods, heaviest.
- **Forge 1.20.1** is the most complete mod ecosystem ever and still home to most RPG and survival packs (Prominence, CtE2, DeceasedCraft, Cursed Walking, ATM9). Expect it to stay viable for years.
- **Fabric** is lighter and hosts the performance packs, Homestead, Prominence, COBBLEVERSE, Create: Astral, StaTech.
- **1.12.2 / 1.7.10** are "classic era": that's where the deepest expert packs are (GTNH, E2E, DJ2, Nomifactory, MeatballCraft, PO3, SevTech, RLCraft). You give up modern caves, combat and rendering; you gain a decade of mature, interlocked mods.

If a pack you want is on an older version, play it. "It's 1.12" is the single most common reason players skip the best-designed packs ever made, and it's a bad reason.

## Step 6 — Time budget

Be realistic. Packs on this site range from a weekend to a decade:

- **< 40 h:** OceanBlock 2, Fabulously Optimized (n/a), Better Minecraft "seen it all"
- **40–150 h:** StoneBlock 4, Create: Astral, Homestead, Liminal Industries, DeceasedCraft, Prominence II, COBBLEVERSE gyms
- **150–350 h:** ATM10/ATM9 Star, E2E, SevTech, A&B, Vault Hunters level 100, CtE2 Atlas
- **400–800 h:** Divine Journey 2, Nomifactory, Monifactory, TerraFirmaGreg
- **1,000 h+:** MeatballCraft, GregTech: New Horizons

## Step 7 — Read the "skip it if"

Every review on this site ends with *Play this if / Skip it if*. Those lists are written to save you the twenty hours it takes to find out a pack isn't for you. The cons sections are not boilerplate — they're compiled from the most-upvoted criticism we could find. If two or three of a pack's "skip it if" bullets describe you, believe them.

## Shortcuts

- Still unsure? Take the [quiz](../quiz.html). It weighs every reviewed pack against your answers.
- Want the numbers side by side? The [comparison table](../compare.html) sorts on any column.
- Want to understand *why* packs are scored as they are? Read the [methodology](methodology.html).

## The three most common mistakes

1. **Choosing by mod count.** More mods ≠ better. The best-designed packs on this site have 150–250 mods; the worst experiences people report come from 400-mod packs with no direction.
2. **Choosing by download count.** Downloads measure marketing and age. RLCraft and Prominence II are top-10 downloads and both have very real problems; Liminal Industries and Rebirth of the Night are far smaller and far better designed.
3. **Starting too hard.** Expert packs are wonderful *after* you've learned the grammar somewhere gentler. The ladder exists for a reason: Better Minecraft → StoneBlock 4 / Astral → E2E or StaTech → Nomifactory → GTNH.
