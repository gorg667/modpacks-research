---
title: "Performance tuning for modpacks"
summary: "RAM, JVM flags, the performance mods that actually matter, in-game settings, and how to diagnose lag — for clients and servers."
order: 4
reading: "9 min read"
---

## The 80/20 of modded performance

Four things account for most of the difference between a stuttering mess and a smooth pack:

1. **Correct RAM allocation** (not too little, not too much).
2. **A modern renderer** — Sodium/Embeddium instead of vanilla or OptiFine.
3. **Reasonable render distance and simulation distance** (12 and 8 are plenty in most packs).
4. **Not running out of CPU** — modded Minecraft is single-thread-bound; a fast core beats many cores.

Everything else is a few percent.

## RAM

Allocate roughly what the pack review says; never more than half your physical RAM. Symptoms of *too little*: `OutOfMemory` crashes, world-load freezes, stutter on every chunk. Symptoms of *too much*: periodic multi-second freezes (huge garbage-collection pauses) and the OS swapping. A 16 GB machine should run 6–8 GB packs happily and 10 GB packs adequately with browsers closed. 32 GB removes the question.

## Java and JVM flags

- **Java version follows Minecraft version**: 8 for 1.12.2 (unless the pack ships Cleanroom/lwjgl3ify), 17 for 1.18–1.20.1, 21 for 1.21+. Newer Java within the allowed range is usually faster; GTNH's Java 17–21 path is dramatically better than Java 8.
- **G1GC defaults are fine** on Java 17+. The classic "Aikar's flags" were tuned for servers on old Java; they still help servers and don't hurt clients. A commonly used client set for Java 17+:

```
-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
```

- **ZGC / Shenandoah** (Java 17+) reduce pause length at the cost of throughput; worth trying on 32 GB machines with 12 GB heaps if you see GC stutter. `-XX:+UseZGC` (Java 21: `-XX:+UseZGC -XX:+ZGenerational`).
- **Pack-specified flags win.** MeatballCraft, Craft to Exile 2 and GTNH publish flags for their memory-cleaner / performance setups — use those.

## Performance mods that matter

Most 2024+ packs bundle these. If yours doesn't, they're client-safe additions:

| Purpose | Fabric | Forge / NeoForge |
|---|---|---|
| Renderer (biggest single win) | Sodium | Embeddium (1.20.1) / Sodium (NeoForge 1.21) — *not* OptiFine |
| Shaders | Iris | Oculus (1.20.1) / Iris NeoForge |
| Game logic | Lithium | Canary / (Lithium NeoForge) |
| Memory | FerriteCore | FerriteCore |
| Startup & misc | ModernFix, ImmediatelyFast | ModernFix, ImmediatelyFast |
| Entities | Entity Culling | Entity Culling |
| Chunk gen (servers) | C2ME (Fabric), Chunky for pregen | Chunky for pregen |
| Item lag | Clumps (XP), FastFurnace | Clumps, FastWorkbench, FastFurnace |

**Do not install OptiFine** into a modern modpack. It conflicts with almost everything and is slower than Sodium/Embeddium. Fabulously Optimized exists precisely to replace it.

## In-game settings

- **Render distance 10–12**, simulation distance 6–8. Big modded worlds punish 16+.
- **Entity distance 100%** or lower in mob-heavy packs.
- **Turn off** Alex's Caves cave biomes, Distant Horizons, or dense worldgen features if chunk generation stutters on older CPUs.
- **Shaders:** Complementary Reimagined / Unbound "Low" or "Medium" presets are the community standard; Potato/MakeUp UltraFast for weak GPUs. Shaders cost 30–60% of FPS.
- **JEI/EMI search lag** in 500-mod packs is normal on first open; subsequent searches are cached.

## Diagnosing lag

- **Low FPS, smooth ticks** → GPU/renderer: lower render distance, shaders, entity distance.
- **Stutter every few seconds** → garbage collection: fix RAM (up or down), try ZGC.
- **Stutter when moving into new areas** → chunk generation (CPU): lower render distance, pregenerate (Chunky), disable heavy worldgen.
- **Everything slow, TPS below 20 (F3 or /forge tps)** → server-side lag: too many machines/entities/chunk loaders. Spark (`/spark profiler`) shows the culprit; it's bundled in many packs.
- **Crafting-table or inventory lag** → recipe/compat mods (Prominence II's known issue with Mowzie's × Cataclysm compat) or Polymorph scanning; check the pack's Discord.

## Servers

- **RAM:** roughly the client figure plus 2 GB; ATM10 12–16 GB for 4–8 players; StoneBlock 4 / most 200-mod packs 8 GB; Nomifactory 2–4 GB.
- **Pregenerate** 2,000–3,000 blocks radius with Chunky before players join.
- **Aikar's flags** are still the standard server JVM set for Java 17+.
- **Chunk loaders** are the #1 TPS killer; limit them per player.
- **enable-command-block=true** is required by several packs (StoneBlock 4, DeceasedCraft) for custom structures to function.
- Big Create contraptions and long train networks are the Create-pack load; big AE2/Refined Storage networks and mob farms are the kitchen-sink load; ore-processing multiblocks are the GregTech load. Design bases with this in mind.
