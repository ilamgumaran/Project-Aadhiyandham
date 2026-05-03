# Geological Stability Assessment: Reading the Ground Beneath You

**Alignment:** Outcome 1: Locating and Connecting Optimal Refugia

<!--
section:        02
outcome:        1
difficulty:     moderate
time_to_build:  3-7 days (field survey)
season:         dry season preferred (exposed rock faces)
team_size:      2-3
depends_on:
  - 02_Topographical_Resilience.md
  - 06_Field_Mineralogy_and_Zero_Tech_Analysis.md
provides_to:
  - 07_Initial_Site_Layout.md
  - 04_Water_Sovereignty_and_Hydrams.md
materials:
  - vinegar (limestone test)
  - water
  - straight stick (2m)
  - cord/string
  - charcoal for marking
status:         complete
-->

> **CAUTION**: Geological field assessment requires traversing potentially unstable terrain. Never approach active landslide scarps, cliff edges, sinkhole rims, or flood-swollen rivers. When probing for karst voids, stand to the side of the probe, not above it.

## Theoretical Foundation

The existing site evaluation framework (Section 02) assesses water, sun, soil, and topography — but treats the geology as frozen in time. It is not. Rivers migrate. Hillsides slide. Fault lines fracture. Sinkholes swallow. A site that scores perfectly on every other metric becomes a death trap if the bedrock is unstable, the slope is prone to mass wasting, or the region sits atop an active fault.

This module provides zero-tech field methods to assess geological stability over a 100-year horizon without seismographs, geological surveys, or printed maps. The expected outcome is a site-specific geological risk profile that either confirms the location is stable or identifies specific hazards that must be mitigated or that disqualify the site entirely.

**The Factor of Safety concept.** Slope stability is governed by the ratio of resisting forces to driving forces, expressed as the Factor of Safety (FoS):

```
FoS = Resisting Forces / Driving Forces

FoS = 1.0  -->  slope is at the point of failure (forces exactly balanced)
FoS = 1.5  -->  minimum for permanent structures (50% safety margin)
FoS > 2.0  -->  generally safe for all construction
```

FoS can be estimated in the field by observing the slope angle relative to the material's angle of repose (the steepest angle at which loose material remains stable — see Module 02.02). A slope at 80% of the angle of repose has roughly FoS = 1.25 — marginal. A slope at 60% of the angle of repose has roughly FoS = 1.7 — acceptable. Saturation from rainfall reduces FoS dramatically by adding pore-water pressure to the driving forces while reducing friction in the resisting forces.

```text
  Factor of Safety — Slope Cross-Section
        Rainfall / Infiltration
             | | | | |
    ~~~~~~~~~v~v~v~v~v~~~  Ground Surface
   /  Soil + Water Weight  \
  /  (DRIVING FORCE --->)   \        FoS = Resisting / Driving
 /____________________________\
 ~~~ Slip Plane ~~~~~~~~~~~~~~~\     RESISTING FORCES:
 |  Shear Strength of Soil      |    - Soil cohesion
 |  Root Cohesion (vegetation)  |    - Internal friction
 |  Friction Along Slip Plane   |    - Root reinforcement
 |  (<--- RESISTING FORCE)      |
 |______________________________|
 //////// Stable Bedrock ////////

  FoS < 1.0 ... FAILURE (slide occurs)
  FoS = 1.0 ... forces exactly balanced
  FoS = 1.5 ... MINIMUM for structures  <-- target
  FoS > 2.0 ... generally safe
```

**Return period probability.** The probability of experiencing at least one event of return period T within n years of occupation:

```
P = 1 - (1 - 1/T)^n

100-year flood over 500 years:   P = 1 - (1 - 0.01)^500  = 99.3%
500-year earthquake over 500 yr: P = 1 - (1 - 0.002)^500 = 63.2%
1000-year eruption over 500 yr:  P = 1 - (1 - 0.001)^500 = 39.4%
```

This math justifies conservative building codes. An event described as "rare" in a single human lifetime becomes near-certain over the timescale of a permanent settlement. Every geological hazard with a return period shorter than the intended occupation period must be treated as inevitable.

```text
  Return Period vs. Actual Probability of Occurrence
  ====================================================

  "100-year event" does NOT mean "once per century."
  It means 1% chance EVERY year. Over time, odds stack up:

  Occupation     |  100-yr event  |  500-yr event  | 1000-yr event
  Length (yrs)   |  (1%/yr)       |  (0.2%/yr)     | (0.1%/yr)
  ---------------+----------------+----------------+--------------
       1 year    |     1%         |     0.2%       |    0.1%
      10 years   |    10%         |     2%         |    1%
      50 years   |    39%         |    10%         |    5%
     100 years   |    63%         |    18%         |   10%
     500 years   |    99%         |    63%         |   39%

  KEY INSIGHT: A 100-year event is MORE LIKELY THAN NOT
  to occur within 100 years (63%, not 100%).
  Over 500 years of settlement, it is virtually certain.
```

**Scientific validation.** Geomorphological research (Shroder, 1980; Wieczorek & Snyder, 2009) validates that curved tree trunks are among the most reliable field indicators of active soil creep, with lateral displacement rates of 1-10 cm/year correlating with eventual catastrophic slope failure. Varnes (1978) and the USGS Landslide Hazard Program confirm that slopes exceeding 25 degrees in clay-rich materials are classified as "high susceptibility" for rainfall-triggered landslides. Ford & Williams (2007) document that doline density and growth rate are the most accessible predictors of sinkhole hazard, measurable with zero instrumentation. Leopold & Wolman's (1960) foundational work on fluvial geomorphology established that alluvial rivers migrate laterally at rates of 0.1-10m per year, fully consistent with the 3x channel-width buffer recommended in this module.

---

## Core Principles

1. **The Multiple Threat Survey.** Assess ALL five geological threats for every candidate site — not just the obvious one. A valley floor free of landslide risk may sit on dissolving limestone. A stable ridgeline may be bisected by an active fault. Single-threat assessment is the most common cause of geological catastrophe in settlement siting.

```text
  Five Geological Threats — Site Cross-Section
  ==============================================

   Volcanic Ashfall                          Distant
   (from prevailing wind) ~~~~>>>>~~~~ ..ite Volcano
                                      /    \
  5. ASHFALL zone         ------     / peak \
                         /      \   /........\
  1. LANDSLIDE --->     / unstable\
     (steep slope)     /  slope    \
                      /  >25 deg   \    3. EARTHQUAKE
  ~~~~~~~~~~~~~~~~~~ /              \   ~~~fault~~~below~~~
                    |  ** SAFE **    |
                    | SETTLEMENT    |   (offset streams,
                    |  ZONE: mid-   |    slickensides,
                    |  slope bench, |    hot springs)
                    |  stable rock  |
  ..................|...............|...................
  2. FLOOD ----->   :   River in    :  <--- meander
     (valley floor) :   floodplain  :       migration
  ~~~~~~~~~~~~~~~~~~:~~~~~~~~~~~~~~~:~~~~~~~~~~~~~~~~~~
  4. SINKHOLE       :  limestone    :
     (karst below)  :  cavern/void  :
  //////////////////:.dissolution..:///////////////////

  Optimal: mid-elevation bench on stable bedrock, ABOVE
  floodplain, BELOW unstable slopes, AWAY from faults,
  karst voids, and volcanic valley drainages.
```

2. **The Conservative Buffer.** Apply minimum safe distances that account for worst-case, not average-case, events. The 100-year flood is not the largest flood that will occur in 500 years of occupation. The runout zone of a landslide extends farther when the slope is fully saturated than when it is dry. Always design to the extreme case.

3. **The Indicator Hierarchy.** Field indicators are sufficient for go/no-go decisions — you do not need instruments to identify pistol-butt trees, offset streams, or karst dolines. A single CRITICAL indicator (tension cracks parallel to slope contour, active sinkhole growth, lahar deposits in a valley) is grounds for site rejection regardless of other merits.

4. **The Annual Monitoring Discipline.** Geological change is slow but cumulative — only continuous monitoring detects it before failure. A slope that creeps 2cm/year shows no visible change in any single observation but has moved a full meter in 50 years. The monitoring protocol must outlive the founders.

5. **The Acceptable Risk Threshold.** No site is zero-risk; the goal is to identify which risks exist and whether they can be mitigated or must be avoided. A site with moderate karst risk but excellent water and soil may be superior to a geologically stable site with poor water. The assessment produces a risk profile, not a binary pass/fail.

---

## Practical Implementation

### Phase 1: Walk the Slopes (Landslide and Mass Wasting)

Landslides are the most common geological killer for hillside settlements. They occur when the downward pull of gravity on saturated soil exceeds the shear strength of the slope material.

**Red flags visible without instruments:**

| Indicator | What It Means | Severity |
|:---|:---|:---|
| **Curved tree trunks ("pistol-butt" trees)** | Soil has been creeping downhill slowly; trees bent at the base but straightened upward | HIGH — active creep, will accelerate |
| **Crescent-shaped scars on hillside** | Previous landslide headscarp; material already failed once | CRITICAL — will fail again |
| **Springs emerging from mid-slope** | Subsurface water is lubricating a clay layer; saturation zone above a slide plane | HIGH — precursor to rotational slide |
| **Tilted fence posts, walls, or old structures** | Ground is moving laterally | HIGH — active movement |
| **Hummocky terrain (irregular bumps and depressions)** | Previous slide deposit; ground is a jumble of displaced material | MEDIUM — stable now but indicates past instability |
| **Bare soil patches on otherwise vegetated slope** | Recent or ongoing surface erosion or shallow slide | MEDIUM — investigate cause |
| **Cracks in the ground running parallel to slope contour** | Tension cracks; the upper mass is separating from stable ground | CRITICAL — imminent failure |

**The Slope Angle Test.** The critical threshold: slopes steeper than 25 degrees (approximately 47% grade) in clay-rich soil are at HIGH risk of failure when saturated.

Measuring slope without instruments:

1. Stand at the base of the slope. Hold a straight stick (2m) horizontally at waist height.
2. Have a partner stand where the stick tip meets the hillside.
3. Measure the vertical distance from the stick tip to the ground at the partner's feet.

```
Rise (vertical) / Run (horizontal stick length) = Slope ratio

If Rise = 0.9m and Run = 2.0m:
Slope = 0.9/2.0 = 0.45 = 45% ≈ 24°
```

| Slope Angle | Risk in Clay Soil | Risk in Rock/Gravel |
|:---|:---|:---|
| < 15° | Low | Very Low |
| 15-25° | Moderate | Low |
| 25-35° | High | Moderate |
| > 35° | Extreme (do not build) | High |

If you cannot determine the slope angle accurately, use the conservative rule: if you cannot walk up the slope comfortably without using your hands, it is too steep to build beneath.

**The Water Saturation Test.** After heavy rain, walk the slope 24 hours later:

- If water is seeping from the ground surface at mid-slope: **subsurface drainage problem.** The slope has a perched water table.
- If your boot sinks more than 5cm into the soil: **the soil is saturated to the root zone.** On slopes >20 degrees, this is a slide precursor.
- If you hear a "sucking" sound when you lift your foot: **clay content is high and water-logged.** This is the worst combination for slope stability.

**Safe Building Zone.** Never build within the runout zone of a potential slide. The runout distance is approximately:

- **2x the vertical height of the slope above** for shallow translational slides.
- **3-4x the vertical height** for deep rotational slides (the crescent-scar type).

If the slope above your candidate site is 50m tall, the minimum safe distance from the base is 100-200m on flat ground.

### Phase 2: Test the Bedrock (Seismic Activity)

You cannot predict earthquakes, but you can identify whether a region has active faulting. Collect rock samples from exposed outcrops. Apply the vinegar test (limestone = karst risk). Look for polished/grooved surfaces (fault activity). Note any volcanic rock types.

**Field indicators of active faulting:**

| Indicator | What It Means |
|:---|:---|
| **Linear valleys with steep, straight walls** | Fault-controlled valley; the straight wall is a fault scarp |
| **Offset streams** (a creek makes a sharp 90-degree bend for no topographic reason) | The stream crosses a fault that has displaced the ground laterally |
| **Hot springs or mineral springs** | Groundwater heated by proximity to deep crustal fractures |
| **Rock faces with polished, grooved surfaces (slickensides)** | Rocks have ground against each other during fault movement |
| **A line of springs or seeps running in a straight line across the landscape** | Water emerging along a fault plane |
| **Triangular faceted ridges** (mountain front looks like a row of triangles) | Repeated fault movement has exposed fresh rock faces |

**The Oral History Check.** Before selecting a site, ask any local inhabitants (if present) or search for cultural markers. Do local place names reference shaking, trembling, or falling? Many indigenous place names encode geological history. Are there ruins with characteristic collapse patterns (walls fallen outward from the base)? Is there oral tradition of "the ground opening" or "the river changing course overnight"?

**Seismic-Resilient Building Rules.** If the region shows ANY indicators of active faulting, ALL structures must follow these rules:

- **Single story only.** Multi-story structures amplify ground motion and collapse catastrophically.
- **No unreinforced stone walls.** Use timber frame with wattle-and-daub infill (flexes without shattering).
- **Anchor to foundation.** Every vertical timber must be pegged or lashed to a heavy sill beam resting on the ground.
- **Diagonal bracing.** Every wall must have at least one diagonal timber (a "knee brace") connecting the sill to the wall plate.
- **No heavy roof materials.** Thatch or shingle, never stone or tile (which kills occupants when it falls).
- **Wide doorways.** Minimum 1m wide to allow rapid egress during shaking.

### Phase 3: Probe for Karst (Sinkhole and Karst Collapse)

Karst landscapes form when soluble bedrock (limestone, dolomite, gypsum) dissolves underground, creating caverns that can collapse suddenly.

**Field indicators:**

| Indicator | Risk Level |
|:---|:---|
| **Limestone bedrock** (fizzes with vinegar) | Karst terrain CONFIRMED — proceed with caution |
| **Disappearing streams** (surface water vanishes into the ground) | HIGH — active dissolution in progress |
| **Circular depressions ("dolines")** across the landscape | HIGH — previous sinkholes; more will form |
| **Ponds with no visible inlet or outlet** | MEDIUM — may be filled sinkholes |
| **Sudden ground subsidence after heavy rain** | CRITICAL — active collapse zone |

**The Probe Test.** In suspected karst terrain, before building:

1. Drive a sharpened hardwood stake (2m long) into the ground with a mallet at 3m intervals across the building site.
2. If the stake suddenly plunges with no resistance after passing through the surface soil layer, there is a void beneath.
3. **Do not build over voids.** Move the site at least 30m away and re-test.

**Living With Karst.** Karst terrain is not automatically disqualifying — it often has excellent groundwater (springs fed by cavern systems), fertile soil (limestone dissolution enriches calcium), and natural defensive features (caves, sinkholes as barriers). But:

- **Never build on or directly adjacent to active dolines.**
- **Route latrines and composting AWAY from sinkholes** — contamination reaches the water table almost instantly in karst (no soil filtration).
- **Monitor existing dolines annually** — measure diameter and depth. If growing, the dissolution is active and nearby structures must be relocated.

### Phase 4: Read the River (Flooding and River Migration)

Rivers migrate. A site 200m from a riverbank today may be undercut in 50 years.

**How to identify the flood boundary without maps:**

- **The debris line:** After any major rain event, walk downstream and mark the highest point where flood debris (sticks, leaves, trash) has been deposited. This is the most recent flood extent.
- **Vegetation change boundary:** The line where upland species (oaks, maples) transition to floodplain species (willows, sycamores, alders) marks the approximate boundary of regular (5-10 year) flooding.
- **Soil color change:** Dig a 50cm test pit. If the soil transitions from brown/red topsoil to grey or blue-grey clay, you are in the floodplain. Grey clay = regular waterlogging = regular flooding.
- **Terrace edges:** If the ground rises in a distinct step (1-3m) above the river floodplain, you are on a river terrace — an older, abandoned floodplain. These are generally safe, but verify the terrace is not being undercut at its base.

**The Meander Migration Rule.** Rivers in alluvial (sandy/silty) valleys migrate laterally. The outer bank of every curve (meander) is being eroded; the inner bank is being deposited.

Rule of thumb: Never build within **3x the current river width** of the outer bank of a meander. A river 20m wide can migrate 60m in a single catastrophic flood.

Safe zones: The inner (point bar) side of meanders, or — best — elevated terraces above the active floodplain.

**The Multi-Generational Flood Record.** Begin recording the annual high-water mark on a permanent stone marker at a fixed location near the river:

```
Year [description] — Water reached [X] hand-widths above base mark.
```

After 10 years, this record reveals the flood cycle. After 50 years, it reveals long-term trends (rising flood levels = climate shift, upstream deforestation, or channel aggradation).

### Phase 5: Assess Volcanic Proximity

If the settlement is within 100 km of a volcanic peak, these indicators require assessment:

| Indicator | What It Means |
|:---|:---|
| **Black, glassy, or vesicular (bubbly) rock** | Volcanic origin — basalt, obsidian, pumice |
| **Hot springs, fumaroles, or sulfurous smell** | Active geothermal system; magma at depth |
| **Conical mountain with radial drainage** | Classic stratovolcano form; even if dormant, can reactivate |
| **Thick deposits of fine-grained ash in soil layers** | Historical eruptions have reached this area |
| **Lahars (solidified mudflow deposits)** — massive boulders mixed in fine mud, filling valley floors | CRITICAL — this valley has been scoured by volcanic mudflows |

**Minimum Safe Distance:**

| Volcanic Hazard | Minimum Distance |
|:---|:---|
| Lava flow | 20 km from summit (lava rarely travels farther on flat terrain) |
| Pyroclastic flow (superheated gas + rock) | 30 km (can travel at 100+ km/h down valleys) |
| Lahar (volcanic mudflow) | Do not build in ANY valley draining from a volcanic peak |
| Ashfall | 100+ km downwind (no practical defense; relocate if sustained) |

**The Practical Rule.** If you can see a volcanic peak from your settlement, you are close enough to be affected by its eruption. This does not disqualify the site, but it requires:

- An evacuation route that moves **perpendicular to valleys radiating from the peak** (never flee down-valley; that is where pyroclastic flows and lahars channel).
- Stockpiled cloth face coverings for ash protection.
- Roof pitch >30 degrees to prevent ash accumulation and structural collapse.

### Phase 6: Establish Baselines and Monitor

Install slope-monitoring stakes, mark the riverbank edge, measure spring output, and record the first flood-level mark. These are Year 1 baselines for the 100-year monitoring protocol. The geological monitoring protocol must be performed by at least 2 trained observers. Loss of monitoring continuity can allow hazards to develop undetected. All annual measurements must be recorded on durable media (stone or fired clay tablets for critical baselines, hide/paper for annual updates). The 100-year record becomes more valuable over time.

**The 100-Year Geological Monitoring Protocol:**

| Observation | Method | Warning Threshold |
|:---|:---|:---|
| Slope creep | Hammer a line of stakes into a suspect slope; measure alignment annually | Any stake displaced >5cm from the line |
| River migration | Mark the bank edge with cairns; measure distance from a fixed reference point | Bank retreat >1m in a single year |
| Sinkhole growth | Measure doline diameter and depth annually with a cord | Diameter increase >0.5m/year |
| Spring flow | Measure output at the same date each year (dry season minimum) | Flow decline >20% over 5 years |
| Ground cracking | Walk perimeter monthly; mark any new cracks with charcoal and date | Any crack >2cm wide or >5m long |
| Flood high-water | Record on permanent stone marker after each flood | 3 consecutive years exceeding the 10-year average |

**The 5-Year Review:** Every 5 years, a designated observer walks the entire settlement perimeter and compares current conditions to the baseline record established in year 1. Any significant deviation triggers a community assessment of whether structures need relocation.

### The Geological Site Assessment Checklist

A single-page pass/fail summary for every candidate site:

| Threat | Key Indicator | Pass | Fail | Mitigation if Marginal |
|:---|:---|:---|:---|:---|
| Landslide / Mass Wasting | Slope angle <25 degrees in clay; no pistol-butt trees or tension cracks | No active movement indicators; slope within safe angle | Any CRITICAL indicator (tension cracks, fresh scarps) | Relocate structures beyond runout zone (2-4x slope height) |
| Seismic Activity | No offset streams, slickensides, or fault-aligned springs | No field evidence of active faulting | Multiple fault indicators confirmed | Build single-story, timber-frame, diagonal-braced structures only |
| Sinkhole / Karst | Bedrock does not fizz with vinegar; no dolines or disappearing streams | No karst indicators present | Active subsidence or void detected by probe test | Avoid dolines by 30m+; route sanitation away from sinkholes |
| Flooding / River Migration | Site above debris line and vegetation boundary; not on outer meander bank | On terrace or upland, outside floodplain | Within floodplain or meander runout zone | Elevate structures; maintain 3x river-width buffer from outer bank |
| Volcanic Proximity | No volcanic rock, ash deposits, or lahar fills in site vicinity | Beyond minimum safe distances for all hazard types | Lahar deposits in valley floor; within 30 km of active vent | Establish perpendicular evacuation route; steep roof pitch for ash |

---

## Common Failure Modes

1. **Single-threat assessment.** Checking only for landslides while ignoring karst collapse beneath the site, or assessing only flood risk while building below an unstable slope. The five-threat survey exists because geological hazards co-occur — limestone terrain is prone to both sinkholes and flooding, and volcanic valleys combine lahar risk with seismic activity.

2. **Dry-season survey bias.** Slopes appear stable in dry season; the same slope fails when saturated in wet season. Springs that indicate subsurface instability may not flow during drought. The water saturation test must be conducted after heavy rainfall, not during the most convenient survey window.

3. **Building in meander runout zone.** The site looks safe today but is within the river's migration path. A river 20m wide migrating at 2m/year will reach a structure 60m from the bank in 30 years — well within a settlement's lifetime. The 3x channel-width rule accounts for catastrophic single-event migration, not gradual drift.

4. **Monitoring abandonment.** Geological observation stops after the founder generation; hazards develop undetected over decades. A slope creeping at 2cm/year shows no visible change to the casual observer but has accumulated a meter of displacement in 50 years. The monitoring protocol must be an apprenticed skill, transmitted with the same discipline as food production.

5. **Volcanic risk dismissal.** "The volcano has not erupted in living memory" — but geological time is not human time. A volcano with a 500-year eruption cycle has a 63% probability of erupting within 500 years of settlement. Lahar deposits in a valley floor are proof that the hazard is real regardless of how long ago the last event occurred.

---

## Vocabulary of the Foundation

- **Mass Wasting:** The downslope movement of rock, soil, and debris under the influence of gravity. Includes landslides, mudflows, rockfalls, and soil creep.
- **Karst:** A landscape formed by the dissolution of soluble rocks (limestone, dolomite, gypsum), characterized by sinkholes, caves, and disappearing streams.
- **Doline:** A closed depression in karst terrain formed by surface dissolution or the collapse of an underground cavity. Commonly called a sinkhole.
- **Slickensides:** Polished, grooved rock surfaces formed by frictional movement along a geological fault plane. Evidence of past seismic activity.
- **Lahar:** A destructive mudflow composed of volcanic debris and water that travels down valleys radiating from a volcano, often triggered by snowmelt or heavy rain on ash deposits.
- **Meander Migration:** The lateral movement of a river channel over time as the outer bank erodes and the inner bank accumulates sediment.
- **River Terrace:** A flat, elevated surface adjacent to a river, representing a former floodplain that the river has since cut below.
- **Factor of Safety (FoS):** The ratio of resisting forces to driving forces acting on a slope or structure. FoS = 1.0 is the threshold of failure; FoS = 1.5 is the minimum acceptable margin for permanent construction.
- **Return Period:** The average recurrence interval of a geological or hydrological event of a given magnitude. A "100-year flood" has a 1% probability of occurring in any single year.
- **Angle of Repose:** The steepest angle at which a pile of unconsolidated material (sand, gravel, soil) remains stable without sliding. Varies by material: dry sand ~34 degrees, wet clay ~15 degrees, angular gravel ~40 degrees.
- **Rotational Slide:** A landslide in which the failure surface is curved (concave-up), causing the sliding mass to rotate backward as it moves downslope. Produces crescent-shaped headscarps and hummocky toe deposits.
- **Translational Slide:** A landslide in which the failure surface is approximately planar, often along a bedding plane, clay layer, or soil-rock interface. The mass moves downslope without significant rotation.

---

## Cross-References

- [02_Topographical_Resilience.md](02_Topographical_Resilience.md) — slope stability fundamentals, angle of repose by material type
- [05_Hydrological_Analysis_and_Watershed_Math.md](05_Hydrological_Analysis_and_Watershed_Math.md) — flood hydrology, return period calculations, watershed delineation
- [06_Field_Mineralogy_and_Zero_Tech_Analysis.md](06_Field_Mineralogy_and_Zero_Tech_Analysis.md) — rock identification methods for karst and volcanic assessment
- [07_Initial_Site_Layout.md](07_Initial_Site_Layout.md) — incorporating geological constraints into settlement layout
- [../../Outcome_3_Perimeter_Defense/07_Passive_Defense/03_Wildfire_Defensible_Space.md](../../Outcome_3_Perimeter_Defense/07_Passive_Defense/03_Wildfire_Defensible_Space.md) — fire risk sector mapping and defensible space

---

## Further Study

- Varnes, D.J. "Slope Movement Types and Processes." In *Landslides: Analysis and Control*, Special Report 176, Transportation Research Board, 1978. The foundational classification of mass wasting types still used in geomorphology.
- Ford, D.C. & Williams, P.W. *Karst Hydrogeology and Geomorphology.* Wiley, 2007. The definitive reference on karst processes, sinkhole formation, and groundwater behavior in soluble rock terrain.
- Leopold, L.B. & Wolman, M.G. "River Channel Patterns: Braided, Meandering, and Straight." USGS Professional Paper 282-B, 1957. Foundational work on fluvial geomorphology and meander migration rates.
- Bolt, B.A. *Earthquakes.* 5th ed., W.H. Freeman, 2005. Accessible treatment of seismology, fault mechanics, and earthquake-resistant construction principles.
- USGS Landslide Hazards Program publications. Field identification guides for landslide indicators, slope stability assessment methods, and hazard mapping protocols.

---

## Glossary Reference

See **Outcome 1 Master Glossary** for standardized definitions of all geological and site assessment terminology used across this section.
