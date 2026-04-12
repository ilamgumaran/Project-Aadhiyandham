# Hydrological Analysis: Watershed Math and Drought Resilience

**Alignment:** Outcome 1: Locating and Connecting Optimal Refugia

> **SAFE**: Hydrological measurement techniques are observational. Exercise caution near fast-moving water during flow measurement — never wade into water deeper than knee height or with current strong enough to affect balance.

---

## Theoretical Foundation

A settlement is defined by its water floor — the absolute minimum volume of water available during the peak of a 100-year drought. Every other resource constraint (soil fertility, timber, forage) can be addressed through labor and ingenuity. Water cannot be manufactured. The hydrological analysis of a candidate site is therefore the single most consequential calculation in settlement design.

### The Hydrological Cycle at Settlement Scale

Water moves through a closed loop that determines everything a settlement can and cannot do. The sequence at landscape scale proceeds as follows:

**Precipitation** falls on the catchment area. A fraction is intercepted by the forest canopy and evaporates before reaching the ground (canopy interception loss, typically 15-30% in dense forest). The remainder reaches the soil surface. A fraction infiltrates into the soil matrix, where it either feeds plant roots (and returns to the atmosphere via transpiration) or percolates downward through permeable strata to recharge the groundwater table. Groundwater moves laterally through aquifers and discharges at springs, seeps, and stream baseflow. Surface water that does not infiltrate becomes direct runoff — stormflow — which travels overland or through shallow subsurface paths to streams and rivers. The entire system is driven by solar energy (evapotranspiration) and gravity (infiltration, flow).

A settlement's water supply is a function of three variables: the watershed area draining to its sources, the precipitation received by that watershed, and the fraction of precipitation that reaches usable springs and streams. The **runoff coefficient** quantifies this last variable — the fraction of rainfall that becomes surface water rather than being absorbed or evaporated:

| Land Cover | Runoff Coefficient |
|---|---|
| Dense forest | 0.05 - 0.20 |
| Grassland / meadow | 0.10 - 0.35 |
| Degraded / bare soil | 0.35 - 0.60 |
| Bare rock / outcrop | 0.70 - 0.90 |
| Urban / impervious surface | 0.70 - 0.95 |

These values have profound implications. A forested watershed absorbs most of its rainfall into groundwater, producing steady baseflow. A deforested watershed sheds rainfall as surface runoff, producing flashy stormflow and diminished baseflow. Protecting watershed forest is therefore a direct investment in water supply reliability.

### The Rational Method for Peak Flow Estimation

The Rational Method provides a first-order estimate of peak flood discharge from a catchment. The formula:

```
Q = C x I x A
```

Where:
- **Q** = peak flow (m^3/s)
- **C** = runoff coefficient (dimensionless, from table above)
- **I** = rainfall intensity (m/s) for the design storm duration
- **A** = catchment area (m^2)

**Worked example:** A 1 km^2 forested catchment (C = 0.15) experiences a 50 mm/hr rainstorm:

```
I = 0.050 m / 3600 s = 1.389 x 10^-5 m/s
A = 1,000,000 m^2
Q = 0.15 x 1.389 x 10^-5 x 1,000,000 = 2.08 m^3/s
```

A flow of 2.08 m^3/s is substantial — roughly equivalent to a stream 2 meters wide and 0.5 meters deep moving at 2 m/s. This flow must be safely conveyed around or through settlement infrastructure. Any bridge, culvert, reservoir spillway, or ford must be designed to pass the peak flow of the design storm without structural failure or erosion.

### Baseflow vs Stormflow

Springs and streams carry two fundamentally different types of water, and confusing them is a common source of settlement water crises.

**Baseflow** is the sustained discharge from groundwater seepage. It is filtered through soil and rock, typically clean, and relatively constant between storm events. Baseflow is determined by aquifer size, geology, and long-term recharge rate — not by recent rainfall. A spring fed by a large, slow aquifer (deep sandstone, limestone karst with extensive conduit systems) may have nearly constant flow year-round, varying by a factor of 2-3 between wet and dry seasons. A spring from shallow fractured rock or thin soil may vary by a factor of 10:1 or more between wet and dry seasons.

**Stormflow** is the rapid pulse of surface runoff during and immediately after rain events. It is turbid, may carry pathogens and chemical contaminants from the land surface, and ceases within hours to days after rainfall stops. Stormflow cannot be relied upon for settlement water supply, and requires treatment before consumption.

Settlement water systems should be designed to capture baseflow only. The intake structure for a spring should be designed to exclude stormflow (which may overwhelm the spring during heavy rain). Stream intakes should include provisions for shutting down during high-turbidity flood events.

### Drought Hydrology

The concept of the "100-year drought" is statistical: it describes a drought of severity that has a 1% probability of occurring in any given year. This does not mean it occurs once per century — it means that in any given year, there is a 1 in 100 chance of experiencing it.

Over long settlement horizons, the cumulative probability is sobering. The probability of experiencing at least one event of return period T within N years is:

```
P = 1 - (1 - 1/T)^N
```

| Event | Over 100 years | Over 500 years |
|---|---|---|
| 100-year drought | 63.4% | 99.3% |
| 500-year drought | 18.1% | 63.2% |
| 1000-year drought | 9.5% | 39.4% |

A settlement designed for a 500-year horizon has a 99.3% probability of experiencing at least one 100-year drought and a 63.2% probability of experiencing a 500-year drought. Design water systems for the 100-year drought flow as an absolute minimum. The 0.4 safety factor applied to dry-season measurements (described below) is intended to approximate this margin.

### Water Quality and Source Protection

Groundwater discharged from springs is naturally filtered through soil and rock matrix. In an undisturbed watershed with adequate soil depth (1m+) and residence time, spring water is typically safe for direct consumption without treatment, provided the source area is protected from contamination.

Surface water — streams, ponds, reservoirs — is always exposed to environmental contamination (animal feces, decomposing organic matter, surface runoff carrying soil pathogens) and should always be treated before drinking.

Source protection is the most cost-effective water treatment technology available. The principle: maintain an undisturbed vegetated buffer of at least 100 meters upslope and lateral to all spring sources. Within this protection zone, prohibit:

- Latrines and human waste disposal
- Animal pens and grazing
- Composting operations
- Fuel storage or chemical use
- Soil disturbance (clearing, cultivation, construction)

Mark the source protection zone physically with cairns, posts, or living fence, and enforce the prohibition as settlement law.

### Historical Precedent

The Nabataean civilization centered on Petra (4th century BCE through 1st century CE) sustained a city of 20,000 or more people in a desert environment receiving less than 100 mm of annual rainfall. Their extraordinary system of dams, cisterns, channels, and aqueducts captured virtually every drop of runoff from the surrounding sandstone watersheds. Archaeological surveys by Oleson and others have documented hundreds of individual water-capture structures distributed across the landscape, each sized to its local catchment. The Nabataeans did not find water — they engineered it.

The Sinhalese kingdoms of Sri Lanka, from the 3rd century BCE onward, constructed massive irrigation reservoirs (locally called "tanks") — some holding more than 50 million cubic meters — that sustained intensive rice agriculture across the dry zone for over 2,000 years. The cascade tank system, where overflow from one reservoir feeds the next downslope, demonstrates sophisticated understanding of watershed-scale hydrology.

Both civilizations prove the same principle: hydrological engineering, not rainfall, determines carrying capacity. A settlement with 2,000 mm of annual rainfall but no storage or source protection may be more water-insecure than a settlement with 200 mm and excellent catchment engineering.

---

## Core Principles

**1. The Drought Floor Rule.** Design all water infrastructure for the 100-year drought flow, not the average flow. Measure spring and stream discharge at the end of the dry season and apply the 0.4 safety factor: `Drought Floor = Dry Season LPM x 0.4`. This ensures the settlement survives even when flow drops by 60% below the driest conditions you have personally measured.

**2. The Baseflow Principle.** Settlement water supply must come from baseflow (springs, groundwater seepage) rather than stormflow (surface runoff). Baseflow is reliable, clean, and predictable. Stormflow is intermittent, turbid, and potentially contaminated. Design intake structures to capture baseflow and exclude stormflow.

**3. The 90-Day Buffer.** Maintain 90 days of stored water capacity at all times. This volume bridges seasonal gaps between rainy and dry periods and provides a buffer against emergency contamination events (upstream landslide, animal carcass in source, earthquake disruption of spring flow). Storage is insurance — it converts a crisis into an inconvenience.

**4. The Source Protection Zone.** Maintain a minimum 100-meter undisturbed vegetated buffer upslope of all water sources. No latrines, animal operations, composting, or soil disturbance within this zone. Source protection is the cheapest and most effective water treatment system ever devised.

**5. The Monitoring Imperative.** Measure spring and stream flow monthly for the first 3 years of settlement, then quarterly thereafter. Maintain written records in the settlement archive. You cannot manage what you do not measure. A 12-month flow record reveals seasonal patterns; a 3-year record reveals inter-annual variability; a 10-year record reveals drought cycles.

---

## Practical Implementation

### The Bucket-and-Stopwatch Method

For small springs and seeps that can be fully diverted into a container, the bucket-and-stopwatch method provides accurate flow measurement.

1. **Capture:** Divert the entire flow of the water source into a bucket or container of known volume (e.g., 10 liters).
2. **Time:** Record the seconds required to fill the container.
3. **Calculate:** `Flow (LPM) = (Volume in Liters / Seconds) x 60`.
   - *Example:* A 10 L bucket fills in 5 seconds. `(10 / 5) x 60 = 120 LPM`.

Repeat three times and average the results to reduce measurement error.

### The Float Method for Larger Streams

For streams too large to divert into a bucket, use the float method to estimate volumetric flow:

1. **Select** a straight, uniform section of stream at least 10 meters long, with consistent width and depth and no obstructions.
2. **Measure channel cross-section:** At three evenly spaced points along the section, measure the channel width (W, in meters) and depth (D, in meters) at 3-5 points across the width. Compute the average cross-sectional area: `A_cross = W_avg x D_avg`.
3. **Measure surface velocity:** Drop a small stick or leaf at the upstream end and time its travel over the 10-meter distance. Repeat five times and average. This gives surface velocity (V_s) in m/s.
4. **Correct for depth:** Average stream velocity is approximately 80% of surface velocity (the bed and banks create friction). `V_avg = 0.8 x V_s`.
5. **Calculate flow:** `Q = A_cross x V_avg` (in m^3/s). Multiply by 1000 and by 60 to convert to liters per minute: `LPM = Q x 60,000`.

**Accuracy:** plus or minus 20-30%, which is adequate for settlement planning purposes. Perform multiple measurements and average.

### Annual Flow Monitoring Log

Maintain a written log at each water source using the following format:

| Month | Date | Source Name | Method | Flow (LPM) | Weather (last 7 days) | Notes |
|---|---|---|---|---|---|---|
| Jan | 15 Jan | North Spring | Bucket | 42 | 3 days rain | Measured after 2 dry days |
| Feb | 12 Feb | North Spring | Bucket | 38 | Dry all week | Baseflow reading |
| ... | ... | ... | ... | ... | ... | ... |

**Critical measurement protocol:**
- Measure at the same location each time (mark it physically with a cairn or stake).
- Measure at the same time of day (morning, before peak evapotranspiration).
- For baseflow readings, measure after 5 or more consecutive dry days. Do not measure during or immediately after rainfall — that captures stormflow, which inflates the reading.
- After 12 months of data, plot the values to create a **hydrograph** — a graph of flow versus time that reveals the seasonal pattern of your water source.

### The Seasonal Decay Factor

Springs fluctuate with season and year. To find your **Drought Floor**, measure the flow at the end of the dry season (the annual minimum) and apply the Aadhiyandham Margin of Safety:

```
Drought Floor = Dry Season LPM x 0.4
```

This 0.4 factor accounts for the possibility that the drought you measured was not the worst drought — the 100-year event may reduce flows by an additional 60% beyond what you observed. This is conservative by design. In water planning, conservatism is survival.

### Individual Consumption Baselines

| Tier | Liters Per Person Per Day | Description |
|---|---|---|
| Survival | 15 | Drinking, cooking, basic hygiene only |
| Standard | 50 | Includes small garden irrigation and modest livestock |
| Abundance | 100 | Full permaculture operation and mechanical water use |

### Carrying Capacity Calculator

The fundamental carrying capacity formula:

```
Maximum Population = (Drought Floor LPM x 1440) / Daily Liters Per Person
```

Where 1440 is the number of minutes in a day.

Expanded scenario table for planning:

| Scenario | Water Per Person (L/day) | Source Flow for 50 people (LPM) | Source Flow for 100 people (LPM) |
|---|---|---|---|
| Survival (15 L/day) | 15 | 0.52 | 1.04 |
| Standard (50 L/day) | 50 | 1.74 | 3.47 |
| Agriculture-inclusive (150 L/day) | 150 | 5.21 | 10.42 |
| Full abundance (250 L/day) | 250 | 8.68 | 17.36 |

The agriculture-inclusive tier assumes approximately 1,000 m^2 of garden per person irrigated at 5 mm/day, which adds roughly 100 L/day per person to the standard domestic consumption of 50 L/day. The full abundance tier adds livestock watering (cattle: 50 L/head/day, goats: 10 L/head/day) and water for mechanical uses (clay processing, tool cooling, washing).

**Worked example:** A spring measured at 8 LPM at the end of the dry season. Drought Floor = 8 x 0.4 = 3.2 LPM. At the Standard tier (50 L/day): `(3.2 x 1440) / 50 = 92 people`. At the Agriculture-inclusive tier (150 L/day): `(3.2 x 1440) / 150 = 30 people`. The settlement must choose its ambition level based on its water floor.

### Reservoir Design Guide

If the water source is intermittent (rain-fed stream, seasonal spring) or if you require a buffer against contamination events, reservoir storage is essential.

**1. The 90-Day Rule for Sizing:**

```
Reservoir Volume (Liters) = Population x Daily Consumption (L) x 90
```

For 50 people at the Standard tier: `50 x 50 x 90 = 225,000 Liters = 225 m^3`.

**2. Shape — Deep and Narrow:**

Evaporation is proportional to surface area. A deep, narrow reservoir minimizes the surface-area-to-volume ratio. Comparison:

- A cylinder 3 m deep x 5 m radius holds `pi x 5^2 x 3 = 236 m^3` (236,000 L) with a surface area of 78.5 m^2.
- A cylinder 1.5 m deep x 7.1 m radius holds the same 236 m^3 but with a surface area of 158 m^2 — double the evaporation exposure.

Always excavate deeper rather than wider.

**3. Lining Options:**

- **Compacted clay:** Minimum 30 cm thickness, applied in 10 cm lifts, each puddled (saturated and compacted by foot or animal trampling) until plastic and impermeable. The most durable and lowest-technology option.
- **Bentonite clay blanket:** If locally available, a 5-10 cm layer of sodium bentonite swells when wet to form an effective seal.
- **Scavenged plastic sheeting:** HDPE or EPDM liner, minimum 1 mm thickness, protected from UV and puncture by a 15 cm soil cover layer above and below.

**4. Inlet and Silt Management:**

Install a silt trap upstream of the main reservoir — a small settling basin (5-10% of main reservoir volume) where inflowing water slows and drops its suspended sediment. Clean the silt trap annually before the rainy season. Without a silt trap, sediment accumulation progressively reduces reservoir capacity — a 1% annual siltation rate halves the effective volume within 70 years.

**5. Overflow and Spillway:**

Design a spillway that can safely pass at least 10 times the average inflow without eroding the dam or embankment. Line the spillway channel with stone or compacted gravel. An undersized spillway is the most common cause of earthen dam failure.

**6. Evaporation Reduction:**

| Method | Evaporation Reduction | Notes |
|---|---|---|
| Floating duckweed (*Lemna*) | ~30% | Also provides livestock feed; requires management to prevent complete coverage |
| Shade cloth / palm frond cover | ~50% | Requires structural support; limited to smaller reservoirs |
| Fully enclosed cistern | ~100% | Most effective; practical only for volumes under ~50 m^3 |
| No cover (open water) | 0% (baseline) | Losses of 5-10 mm/day in hot, dry climates are common |

For a reservoir with 78.5 m^2 surface area in a climate with 8 mm/day evaporation, the daily loss without cover is 628 liters/day — equivalent to the drinking water for 42 people at the survival tier. Evaporation control is not optional in warm climates.

### Rainwater Harvesting Supplement

For settlements with roof structures, rainwater collection provides a valuable supplement to spring and stream sources.

```
Annual Collection (L) = Roof Area (m^2) x Annual Rainfall (m) x Runoff Coefficient x 1000
```

Runoff coefficients for roofing materials:
- Metal / corrugated iron: 0.80 - 0.85
- Tile: 0.70 - 0.80
- Thatch: 0.50 - 0.60

**Worked example:** A 50 m^2 metal roof in a location receiving 800 mm annual rainfall:

```
Collection = 50 x 0.80 x 0.80 x 1000 = 32,000 L/year = 87.7 L/day average
```

This supplements but does not replace spring or stream sources. Rainwater is inherently seasonal and variable. However, for a single household of 4 people at the survival tier (60 L/day total), a 50 m^2 roof in an 800 mm rainfall zone provides meaningful security.

Install first-flush diverters (discard the first 1-2 mm of rainfall from each event, which washes accumulated dust, bird droppings, and debris from the roof surface) and covered storage tanks to maintain quality.

### Water Budget Worksheet

The water budget integrates all sources against all demands on a monthly basis. Construct a table for each month of the year:

| Category | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sources (L/day)** | | | | | | | | | | | | |
| Spring A (baseflow) | | | | | | | | | | | | |
| Spring B (baseflow) | | | | | | | | | | | | |
| Stream intake | | | | | | | | | | | | |
| Rainwater harvesting | | | | | | | | | | | | |
| Reservoir drawdown | | | | | | | | | | | | |
| **Total Supply** | | | | | | | | | | | | |
| **Demands (L/day)** | | | | | | | | | | | | |
| Drinking & cooking | | | | | | | | | | | | |
| Hygiene & washing | | | | | | | | | | | | |
| Garden irrigation | | | | | | | | | | | | |
| Livestock | | | | | | | | | | | | |
| Mechanical / craft use | | | | | | | | | | | | |
| Reservoir evaporation | | | | | | | | | | | | |
| **Total Demand** | | | | | | | | | | | | |
| **Surplus / Deficit** | | | | | | | | | | | | |

Fill this table using measured flows and projected demands. The critical months are those showing a deficit — these are the months when the settlement draws down stored water. The cumulative deficit over all deficit months must not exceed the reservoir volume minus the 90-day emergency reserve. If it does, either reduce demand (fewer people, less irrigation) or increase supply (additional sources, larger catchment).

---

## Common Failure Modes

**1. Designing for average flow instead of drought floor.** The most common and most dangerous error. Average flow may be 5 to 10 times the drought floor. A settlement sized for average flow will experience water crisis during the first major drought — which, over a multi-generational horizon, is a certainty, not a possibility.

**2. Siltation of reservoirs.** Every stream carries a sediment load proportional to its catchment's erosion rate. Without silt traps and regular maintenance, reservoirs fill progressively with sediment. A reservoir losing 1% of its volume annually to siltation loses half its effective capacity within a human lifetime. Install silt traps, clean them annually, and maintain watershed vegetation to minimize erosion.

**3. Source contamination from upslope activities.** Pathogens from latrines and animal pens travel through soil via percolation and can reach springs and seeps within weeks to months, depending on soil type and distance. A single latrine placed 30 meters upslope of a spring can render the spring unsafe for drinking. Enforce source protection zones without exception.

**4. Evaporation losses in open reservoirs.** In hot, dry climates, open-water evaporation can reach 8-10 mm per day, which translates to 30-50% annual loss of stored volume. This is a silent, continuous drain on the water budget that is easily overlooked. Use floating vegetation, shade structures, or enclosed cisterns to reduce losses.

**5. Population growth exceeding water budget.** Settlements that do not enforce population limits tied to the measured water floor will inevitably outgrow their water supply. The carrying capacity formula must be treated as a hard ceiling, not a guideline. When population approaches 80% of the calculated maximum, halt growth until additional water sources are developed and proven through at least one full dry season of measurement.

---

## Vocabulary of the Foundation

- **Watershed**: The total land area that drains to a single point (stream confluence, spring, reservoir). All precipitation falling within the watershed boundary eventually reaches that point. The watershed is the fundamental unit of hydrological analysis.

- **Baseflow**: The component of stream or spring flow derived from groundwater discharge. Baseflow is sustained between rainfall events and represents the reliable, clean water supply from subsurface storage.

- **Stormflow**: The component of stream flow derived from direct surface runoff during and immediately after rainfall. Stormflow is rapid, turbid, unreliable, and requires treatment.

- **Runoff Coefficient**: The fraction of precipitation that becomes surface runoff rather than infiltrating into soil or evaporating. Expressed as a dimensionless number between 0 and 1. Determined primarily by land cover, soil type, and slope.

- **Rational Method**: An empirical formula (Q = C x I x A) for estimating peak surface runoff from a catchment during a design storm. Used to size spillways, culverts, and flood conveyance structures.

- **Drought Floor**: The minimum reliable water supply, calculated as the dry-season measured flow multiplied by the 0.4 safety factor. All population and infrastructure planning must reference the drought floor, not average flow.

- **Hydrograph**: A graph of water flow (discharge) plotted against time. A 12-month hydrograph reveals seasonal patterns; a multi-year hydrograph reveals drought cycles and long-term trends.

- **Carrying Capacity (hydrological)**: The maximum population a site can sustain based on its drought floor water supply and the chosen consumption tier. Determined by the formula: `(Drought Floor LPM x 1440) / Daily Liters Per Person`.

- **Silt Trap**: A small settling basin installed upstream of a reservoir where inflowing water velocity decreases, allowing suspended sediment to settle out before entering the main storage body.

- **Evapotranspiration**: The combined loss of water from the landscape through direct evaporation (from soil, water surfaces) and transpiration (water uptake and release by plants). The primary mechanism by which water exits the local hydrological cycle.

- **Aquifer**: A body of permeable rock or sediment that stores and transmits groundwater. The size, permeability, and recharge rate of the aquifer feeding a spring determine the spring's reliability and drought resilience.

- **Source Protection Zone**: The designated area upslope and lateral to a water source within which all activities that could introduce contamination are prohibited. Minimum recommended radius: 100 meters.

- **Cistern**: An enclosed, watertight container for storing collected water (rainwater or piped spring water). Cisterns eliminate evaporation loss and contamination risk but are limited in practical volume compared to open reservoirs.

---

## Cross-References

- [01 Rationale and Importance](01_Rationale_and_Importance.md) — Liebig's Law and the role of water as the ultimate limiting factor in site selection.
- [04 Water Sovereignty and Hydrams](04_Water_Sovereignty_and_Hydrams.md) — hydraulic ram pumps and techniques for moving water uphill without external energy.
- [11 Soil and Water Quality Baselines](11_Soil_and_Water_Quality_Baselines.md) — field methods for testing water quality parameters (pH, turbidity, coliform).
- [Outcome 2: Water and Sanitation Rationale](../../Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/01_Rationale_and_Importance.md) — water treatment principles and sanitation system design.
- [Outcome 2: Bio-Sand Filtration](../../Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/02_Bio_Sand_Filtration.md) — slow sand filtration for treatment of surface water sources.

---

## Further Study

- Dunne, T. & Leopold, L.B. *Water in Environmental Planning*. W.H. Freeman, 1978. The foundational text on applied hydrology for land-use planning. Covers watershed analysis, runoff estimation, erosion, and water quality in accessible, field-oriented language.
- Linsley, R.K., Franzini, J.B. & Freyberg, D.L. *Water Resources Engineering*. McGraw-Hill, 4th edition, 1992. A comprehensive engineering reference covering surface water hydrology, groundwater, reservoir design, and water supply systems.
- World Health Organization. *Guidelines for Drinking-water Quality*. 4th edition, 2011. The international standard for water quality parameters, treatment methods, and source protection protocols.
- Pacey, A. & Cullis, A. *Rainwater Harvesting: The Collection of Rainfall and Runoff in Rural Areas*. Intermediate Technology Publications, 1986. Practical guidance on rainwater collection systems for low-resource settings, including sizing, storage, and quality management.
- Oleson, J.P. *Humayma Excavation Project* and related publications on Nabataean hydraulic engineering. Documents the extraordinary water capture and storage systems that sustained desert civilization at Petra and surrounding settlements.

---

## Glossary Reference

*See [../../Glossary.md](../../Glossary.md) for full definitions of:*

- **Refugia**
- **Carrying Capacity**
- **Liebig's Law**
- **Drought Floor**
- **Baseflow**
