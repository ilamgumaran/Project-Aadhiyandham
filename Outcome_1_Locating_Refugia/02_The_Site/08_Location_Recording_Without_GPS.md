# Recording and Transmitting Location Without GPS

**Alignment:** Outcome 1: Locating and Connecting Optimal Refugia

<!--
section:        02
outcome:        1
difficulty:     moderate
time_to_build:  1-2 days
season:         any
team_size:      2-4
depends_on:
  - 02_Topographical_Resilience.md
  - 03_Solar_and_Thermal_Balance.md
  - 06_Field_Mineralogy_and_Zero_Tech_Analysis.md
provides_to:
  - 01_Decentralized_Networking_and_Trade.md
  - 02_Zero_Power_Communication_Protocols.md
materials:
  - stone (for cairns)
  - iron gall ink or charcoal
  - hide or paper
  - chisel or hardened steel blade
status:         complete
-->

## 1. Why This Is Important

Every module in Section 02 (The Site) assumes you can *find* the refugium. But what happens when printed maps disintegrate, compasses break, or new groups need to locate you decades later? Without GPS, coordinates are meaningless numbers. The community needs a permanent, self-validating location recording system that works across generations, survives language drift, and does not depend on any technology that can fail.

This module provides three independent systems: **physical marking** (for anyone walking nearby), **celestial anchoring** (for anyone with clear sky), and **narrative encoding** (for anyone who can hear a story).

---

## 2. Expected Outcome

A refugium location that can be found by a stranger 100 years from now using only their eyes, the sky, and an oral tradition passed through three generations of intermediaries.

---

## 3. System 1: Physical Landmark Anchoring (The Sentinel Network)

### 3.1. The Principle

Instead of storing coordinates, store the location as a **relationship between permanent landmarks**. Mountains, river confluences, and rock formations survive centuries. Your position is defined by the angles and distances between these features.

### 3.2. The Three-Sentinel Record

Select three landmarks visible from the refugium that meet ALL of these criteria:
*   **Geological permanence:** Solid rock formation, mountain peak, or major river confluence. NOT a tree, building, or sand feature.
*   **Distinctiveness:** Cannot be confused with adjacent features. A lone rock spire qualifies; a featureless ridgeline does not.
*   **Angular separation:** At least 30 degrees apart when viewed from the refugium. Three landmarks bunched together provide poor triangulation.

**Recording format (inscribe on stone or durable hide):**

```
SENTINEL 1: [Name] — Bearing [fists from North at sunrise on equinox]
SENTINEL 2: [Name] — Bearing [fists from North at sunrise on equinox]
SENTINEL 3: [Name] — Bearing [fists from North at sunrise on equinox]
```

**Bearing measurement without compass:** At the spring or autumn equinox, face the sunrise (true East). Extend your arm and count fist-widths (each fist at arm's length ≈ 10 degrees) from the sunrise point clockwise. This gives a repeatable angular bearing independent of magnetic declination.

### 3.3. Distance Encoding (The Walking Clock)

Record distance from the nearest Sentinel to the refugium in **walking time**, not units that require calibration:

```
From [Sentinel 1]: Walk toward [Sentinel 2] for [X] sunrise-to-noon periods.
```

One "sunrise-to-noon" period ≈ 6 hours of walking ≈ 18-24 km on flat terrain, ≈ 10-15 km on hilly terrain. The variability is acceptable because the Sentinel network narrows the search area, not pinpoints it.

### 3.4. The Approach Cairn System

Build a series of stone cairns that guide a traveler from the nearest major trail or river to the refugium:

| Cairn Type | Construction | Meaning |
|:---|:---|:---|
| **Waypoint** | 3-stone stack (60cm tall) | "You are on the correct path" |
| **Direction change** | 3-stone stack with a flat pointer stone on top, angled toward next cairn | "Turn this direction" |
| **Warning** | Single large stone placed ON a smaller stone (inverted scale) | "Danger ahead — cliff, bog, or restricted area" |
| **Arrival** | 5-stone pyramid (1m tall) with white quartz capstone (if available) | "Refugium is within visual range" |

**Spacing rule:** Each cairn must be visible from the previous one. In forest, this means every 50-100 meters. In open terrain, every 500-1000 meters. When in doubt, place more.

**Durability:** Dry-stack stone cairns survive centuries with no maintenance. Avoid using mortar (it cracks and collapses the entire stack). Select angular stones that interlock, not round river cobbles.

---

## 4. System 2: Celestial Anchoring (Latitude Without Instruments)

### 4.1. The Principle

Latitude can be determined from the night sky with bare eyes. Longitude cannot be reliably determined without a precision clock, but latitude alone — combined with the Sentinel bearings — is sufficient to encode a location that narrows the search to a band approximately 5 km wide.

### 4.2. Latitude from Polaris (Northern Hemisphere)

1.  At night, find Polaris (the North Star) using the "pointer stars" of the Big Dipper's outer edge.
2.  Extend your arm fully. Measure the angle from the horizon to Polaris in **fist-widths** (each fist ≈ 10°) and **finger-widths** (each finger ≈ 2°).
3.  The angle of Polaris above the horizon **equals your latitude**.

**Recording example:** `Polaris stands 3 fists and 2 fingers above the northern horizon.` This encodes latitude ≈ 34° (3×10 + 2×2 = 34°), accurate to ±2°, which is ±220 km — but combined with Sentinels, the location is fully specified.

### 4.3. Latitude from the Sun (Both Hemispheres)

At local solar noon (when a vertical stick casts its shortest shadow):

1.  Measure the shadow length (S) and the stick height (H).
2.  Calculate the sun's elevation angle: `tan(angle) = H / S`, so `angle = arctan(H / S)`.

Without trigonometric tables, use the **ratio method:**

| Shadow:Stick Ratio (S/H) | Sun Elevation (approx.) |
|:---|:---|
| 0.0 (no shadow) | 90° (sun directly overhead) |
| 0.27 | 75° |
| 0.58 | 60° |
| 1.00 | 45° |
| 1.73 | 30° |
| 3.73 | 15° |

3.  At the equinoxes (March 20, September 22), your latitude = 90° − sun elevation.
4.  At the solstices, adjust by ±23.4° (Earth's axial tilt).

**Recording format:** `At equinox noon, the shadow-to-stick ratio measures 1.0. Therefore latitude ≈ 45°.`

### 4.4. Longitude Approximation (The Noon Offset Method)

True longitude requires a reference clock, which will not exist post-collapse. However, **relative longitude** between two known refugia can be approximated:

1.  Both communities observe a predictable celestial event (e.g., a lunar eclipse, which is visible simultaneously across a hemisphere).
2.  Each community records the local time of the event using their solar noon as the reference (hours before or after noon).
3.  Each hour of difference = 15° of longitude.

**Example:** If Refugium A sees the lunar eclipse 2 hours after their noon, and Refugium B sees it 4 hours after their noon, Refugium B is approximately 30° east of Refugium A.

**Recording format:** `During the eclipse of [year description], the moon entered shadow 3 sun-hours past noon.`

---

## 5. System 3: Narrative Encoding (The Route Song)

### 5.1. The Principle

Oral traditions survive far longer than written documents if encoded in a structure that resists corruption through retelling. Aboriginal Australian songlines have encoded navigation routes for 10,000+ years using rhythm, melody, and landmark sequences. This module adapts the principle for any culture.

### 5.2. The Route Song Structure

Encode the approach route to the refugium as a **rhythmic, rhyming narrative** with the following constraints:

*   **Each verse = one day's travel** (sunrise to sunset).
*   **Each verse must name a physical landmark** that a traveler can verify.
*   **Directional cues are embedded in the narrative**, not stated abstractly.
*   **The rhythm is fixed** — any word substitution by a reteller will break the meter, signaling corruption.

**Template verse format (English example):**

```
When [landmark] stands upon your [left/right] hand,
And [water feature] cuts across the land,
Walk toward the [compass direction] where [natural sign],
Until the [next landmark] marks the [morning/evening] line.
```

**Example:**

```
When Split Rock stands upon your left hand,
And Willow Creek cuts across the land,
Walk toward the sunset where the oaks grow tall,
Until the Three Sisters mark the evening's fall.
```

### 5.3. Corruption Detection

*   **Meter check:** If a verse doesn't rhyme or scan rhythmically, it has been altered.
*   **Landmark verification:** If the traveler reaches a landmark that doesn't match the verse, they have deviated from the route.
*   **Redundancy:** Encode the same route in two independent songs (e.g., one for the outbound journey, one for the return). Discrepancies reveal which version has drifted.

### 5.4. The Archive Copy

In addition to oral transmission, inscribe the route song onto:
*   **Stone tablets** (using chisel or iron stylus) — survives millennia.
*   **Fired clay tablets** — survives centuries in dry climates.
*   **Iron gall ink on vellum** (animal hide) — survives 200-500 years if stored dry.

Paper is the last resort. It degrades within 50-100 years in humid climates.

---

## 6. Correcting for Magnetic Declination Drift

### 6.1. The Problem

A magnetic compass does not point to true north. The offset (declination) varies by location and changes approximately 0.05-0.2° per year. Over 100 years, this can introduce an error of 5-20°, making compass-only directions dangerously inaccurate.

### 6.2. The Annual Calibration Protocol

Every equinox, perform the following:

1.  At local solar noon, plant a vertical stick and mark the shadow direction. This shadow points exactly true north (Northern Hemisphere) or true south (Southern Hemisphere).
2.  Lay a compass beside the shadow line.
3.  Read the compass bearing of the shadow. The difference between the compass reading and 0° (or 180°) is the current magnetic declination.
4.  **Record it.** `Equinox [year]. Shadow points 8° east of compass north.`

Over decades, the community builds a declination history. If it shifts by more than 3° in a single decade, all recorded compass bearings must be updated.

### 6.3. Embedding Declination into the Sentinel Record

Always record bearings using BOTH methods:

```
SENTINEL 1: Twin Peaks — 4 fists from equinox sunrise (celestial bearing)
                       — Compass bearing 042° (magnetic, declination +8° east, recorded [year])
```

The celestial bearing is permanent. The compass bearing is a convenience that requires periodic correction.

---

## 7. Visual Illustration (Conceptual)

```text
                    ★ Polaris (Latitude anchor)
                    |
                    | angle = latitude
                    |
         ┌─────────┼─────────┐
         │    NIGHT SKY       │
    ─────┼────────────────────┼──── Horizon
         │                    │
         │                    │
   [SENTINEL 1]    ☉    [SENTINEL 2]          
    Mountain      YOU     River Fork           
      ↖          /|\          ↗               
        ↖        |          ↗                 
          ↖  ◉ Cairn      ↗                   
            ↖   Trail   ↗                     
              [SENTINEL 3]                     
               Rock Spire                      

  THREE-SENTINEL TRIANGULATION
  + POLARIS LATITUDE = Location Record
```

---

## 8. Vocabulary of the Foundation

*   **Sentinel:** A geologically permanent landmark used as a reference point for triangulation. Must survive centuries without human maintenance.
*   **Celestial Bearing:** A directional measurement taken relative to the equinox sunrise position, independent of magnetic declination.
*   **Route Song:** A rhythmically structured oral narrative encoding a travel route, designed to resist corruption through multi-generational retelling.
*   **Declination:** The angular difference between magnetic north (where a compass points) and true north (the Earth's rotational axis). Changes over time.
*   **Fist-width:** An angular measurement equal to approximately 10° when the fist is held at arm's length against the sky.

---

## 9. Scientific Validation & Research Context

*   **Aboriginal Songlines:** Research by linguist R.M.W. Dixon and geographer Duane Hamacher has documented that Australian Aboriginal songlines encode geographic features that have been geologically verified as accurate over 10,000+ years, including coastlines submerged since the last ice age. The structured oral format is more durable than any physical medium.
*   **Polaris Latitude Accuracy:** Naked-eye Polaris sighting provides latitude accurate to ±1-2° (±110-220 km). Combined with three Sentinel landmarks, this narrows location to a specific valley.
*   **Stone Cairn Durability:** Archaeological surveys of Scottish Highland cairns and Inuit inuksuit demonstrate structural survival of dry-stacked stone markers for 1,000-4,000 years in exposed alpine and arctic environments without maintenance.
*   **Magnetic Declination Rate:** NOAA geomagnetic models show secular variation of 0.05-0.2°/year depending on location, with cumulative shifts of up to 20° over a century in some regions (e.g., North America east coast has shifted from 15°W to 13°W over the last 50 years).

---

## 10. Practical Implementation Guide for Beginners

### 10.1. Step-by-Step Action Plan
*   **Phase 1: Sentinel Selection.** Walk the perimeter of your refugium. Identify 5 candidate landmarks (you need 3, but redundancy accounts for geological events). Verify each is solid rock or a major water confluence.
*   **Phase 2: Equinox Calibration.** At the next equinox, measure the fist-width bearing to each Sentinel from the center of the settlement. Record on stone and hide. Simultaneously calibrate your compass declination.
*   **Phase 3: Cairn Trail.** Walk the primary approach route from the nearest major trail/river to the refugium. Place waypoint cairns at visual intervals. Build a direction-change cairn at every turn. Build the arrival pyramid at the final ridgeline before visual contact.
*   **Phase 4: Route Song.** Compose a verse for each day of travel from the nearest known location (e.g., a major river crossing or former town) to the refugium. Test it by having someone who has never visited follow the song alone.

### 10.2. Troubleshooting & Failure Modes
*   **Cairns destroyed:** Flash floods, avalanches, or deliberate dismantling can remove cairns. Rebuild every spring after snowmelt. If a hostile group is dismantling cairns, switch to blazed trees (axe-cut notches at eye level on the trail-facing side).
*   **Sentinel lost:** If a rockfall alters a Sentinel peak, record the change and substitute the next-best landmark. Update all records. This is why you select 5 candidates initially.
*   **Route Song corrupted:** If two reciters disagree on a verse, BOTH versions are suspect. Walk the disputed section physically to determine which verse matches the terrain. Re-establish the canonical version and archive it on stone.

### 10.3. Community & Decadal Flourishing
*   **Apprenticeship:** Every generation must have at least 2 people who can recite the route song from memory and perform the equinox calibration. Test them annually.
*   **Inter-settlement sharing:** When contact is made with another refugium, exchange Sentinel records and route songs. Each community should hold the location data for at least 3 other refugia.
