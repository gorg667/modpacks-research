---
title: "Launchers, installing and updating modpacks"
summary: "Which launcher to use (and which to avoid for which packs), how to install from CurseForge, Modrinth and FTB, how to allocate RAM, and how not to lose your world when updating."
order: 3
reading: "10 min read"
---

## The launchers

Modpacks are installed and run through a *launcher* that downloads the mods, sets up the right Minecraft version and mod loader, and manages Java. You have five real options:

| Launcher | Best for | Notes |
|---|---|---|
| **Prism Launcher** | Everyone who wants control | Free, open source, fast. Installs packs from CurseForge, Modrinth, FTB (legacy), ATLauncher and Technic. Per-instance Java and RAM. The community default for GTNH, MeatballCraft and anything with special Java needs. |
| **CurseForge App** | Beginners on CurseForge-first packs | The official Overwolf-based app. One-click for ATM, Prominence, RLCraft, etc. Heavier, ads in the free tier. **Do not use for GTNH** (broken, outdated listing) or for packs that need custom Java. |
| **Modrinth App** | Modrinth-first packs (Homestead, COBBLEVERSE, FO) | Clean, fast, open source. Growing catalogue; many big packs are dual-listed. |
| **FTB App** | FTB packs (StoneBlock 4, OceanBlock 2, Direwolf20) | Required for in-app FTB server hosting; also installs CurseForge packs. |
| **ATLauncher / Technic** | Legacy packs and a few holdouts | ATLauncher hosts GTNH and older packs; Technic is mostly historical. |

**Recommendation:** Prism Launcher for anyone comfortable clicking "add instance"; the CurseForge or Modrinth app if you want the simplest path and your pack is there.

## Installing

1. Install the launcher and **sign in with your Microsoft account** (you need Java Edition).
2. Search the pack by name. Install the *official* listing — copycats and "Plus" forks are common; the official page is linked from every review here.
3. Pick the **latest stable** version unless a review says otherwise (DeceasedCraft's v6 beta can't be finished; GTNH betas are for testing).
4. Let it download (1–3 GB for big packs).
5. **Set RAM** (below) before first launch.
6. First launch of a big pack takes 1–5 minutes. Don't force-quit a blank window.

**Java.** Launchers auto-select Java for the Minecraft version. If you get "Java version mismatch" or an instant crash: 1.12.2 → Java 8; 1.18–1.20.1 → Java 17; 1.21 → Java 21. GTNH's official download uses Java 17–21 via lwjgl3ify; MeatballCraft supports Java 21/22 via Cleanroom — follow *their* instructions.

## Allocating RAM

The single most impactful setting. In the launcher's Java/instance settings, set **maximum memory**:

- Target the review's RAM figure (StoneBlock 4: 6–8 GB; ATM10: 10–12 GB).
- **Never exceed half your physical RAM.** 16 GB system → 8 GB is safe, 10 borderline, 12 will make the game *slower*.
- More is not better past the target — bigger heaps mean longer garbage-collection pauses.

**JVM flags.** Java 17+ with default G1 is fine for most packs. Packs that specify flags (MeatballCraft, Craft to Exile 2, GTNH) do so for a reason — paste theirs in. Otherwise see the [performance guide](performance-tuning.html).

## Updating without losing your world

1. **Back up first.** Copy `saves/<world>` somewhere else. Every time.
2. **Read the changelog** for "removed mod", "world reset recommended", "config changes".
3. **Update through the launcher**, not by dragging files.
4. If it goes badly, reinstall the previous version and restore the backup.
5. **Servers:** client and server must be on the *same* pack version — mismatches are the #1 "can't connect" cause.

Rule of thumb: *if it ain't broke, don't update mid-playthrough* unless the changelog fixes something you've hit.

## Adding or removing mods

Most packs tolerate **client-side additions** (minimaps, Jade, shader loaders). Adding content mods to a designed pack (StoneBlock 4, expert packs) breaks the design; removing mods often breaks recipes. Back up before experimenting.

**Shaders:** Forge/NeoForge packs use Oculus/Iris + Embeddium/Rubidium (usually bundled); Fabric packs use Iris + Sodium (usually bundled). Never add OptiFine to a modern pack.

## Common launch problems

| Symptom | Likely cause |
|---|---|
| Crash before the Mojang logo | Wrong Java version |
| `OutOfMemory` / exit code 1 | Too little RAM allocated |
| Freezes every few minutes | Too *much* RAM, or a memory-hungry pack (MeatballCraft) under-allocated |
| Pink/missing textures | Resource pack or shader incompatibility |
| "Mod X requires Y" | Partial download — reinstall |
| Server: "Incompatible mods" | Client/server version mismatch |
