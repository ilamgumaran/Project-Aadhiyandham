# Bio-Sand Filtration: The Living Filter

**Alignment:** Outcome 2: Absolute Biological Sovereignty

Bio-sand filtration is the cornerstone zero-energy water treatment technology for any post-collapse settlement. Unlike chemical treatment (which requires a supply chain for chlorine or iodine), UV sterilization (which requires electricity or clear skies), or boiling (which requires fuel), a bio-sand filter operates on gravity alone. Once constructed from locally sourced sand and gravel, it requires no replacement parts, no consumable inputs, and no external energy. A single filter produces 400-600 litres of treated water per day — enough for 20-30 people — indefinitely.

The mechanism is not merely mechanical. While the sand column does physically strain out protozoan cysts and helminth eggs, the primary pathogen removal occurs in a living biofilm called the **Schmutzdecke** (German: *Schmutzdecke*, "dirty layer"; Tamil: *உயிர்ப்படலம்*, "living membrane"). This biofilm — a dense community of bacteria, protozoa, algae, and their extracellular polymeric substances — colonizes the top 2-5 cm of the sand bed over a 10-14 day ripening period. Once mature, the Schmutzdecke actively consumes waterborne pathogens: its protozoa engulf bacteria, its bacteriophages lyse viruses, and the entire community competes with and starves out incoming pathogens. The filter is, in the truest sense, a living machine.

This module provides the theoretical basis, construction specifications, and maintenance protocols for deploying bio-sand filtration at settlement scale. The design presented here is based on the CAWST (Centre for Affordable Water and Sanitation Technology) intermittent slow sand filter — the most extensively field-tested household water treatment technology in the developing world, with over 800,000 units deployed across 70 countries as of 2020.

> **SAFE**: Bio-sand filter construction and operation poses no inherent hazard. Standard precautions apply when handling heavy materials (sand, gravel, containers). **CRITICAL WARNING**: Do not drink unfiltered water from a new or recently disturbed filter during the 10-14 day ripening period. During ripening, all filter output must be boiled or otherwise disinfected before consumption.

---

## Theoretical Foundation

### Darcy's Law and Flow Through Porous Media

The flow rate through a bio-sand filter is governed by Darcy's Law, the fundamental equation of groundwater hydraulics:

**Q = K x A x (dh / L)**

Where:
- **Q** = volumetric flow rate (m³/day)
- **K** = hydraulic conductivity of the filter medium (m/day)
- **A** = cross-sectional area of the filter bed (m²)
- **dh** = hydraulic head difference — the height of standing water above the sand surface (m)
- **L** = depth of the filter bed (m)

For a typical bio-sand filter:
- K for fine sand (0.15-0.35 mm effective grain size) = 1-5 m/day
- A = 0.06-0.09 m² (a 30 cm x 30 cm square or ~30 cm diameter barrel)
- dh = 0.05-0.15 m (5-15 cm standing water head)
- L = 0.50-0.60 m (50-60 cm sand depth)

Substituting conservative values: Q = 2 m/day x 0.09 m² x (0.10 / 0.55) = 0.033 m³/day = 33 L/day at the low end. With a full 15 cm head and clean sand: Q = 5 x 0.09 x (0.15 / 0.50) = 0.135 m³/day = 135 L/day. In practice, intermittent operation with repeated batch pours yields 400-600 L/day because each new pour re-establishes the full head.

The critical insight: as the Schmutzdecke matures, K decreases because the biofilm reduces effective pore size. Flow rate drops. This is a *feature*, not a defect — it signals that the biological layer is active and functioning. A filter that flows too fast is not filtering adequately.

```text
    Darcy's Law: Flow Through a Sand Column

    |<--- A (cross-section area) --->|
    |                                |
    |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |  ---
    |  ~~~~~ STANDING WATER ~~~~~~~  |   |  dh (hydraulic head)
    |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |   |  = water height above sand
    |================================|  ---
    |:::::::::::::::::::::::::::::::::|   |
    |::::: SAND BED (porous) ::::::::|   |
    |:::::::::::::::::::::::::::::::::|   |  L (bed depth)
    |::::: K = hydraulic conductivity|   |
    |:::::::::::::::::::::::::::::::::|   |
    |================================|  ---
    |          v  v  Q (outflow)      |
    Q = K x A x (dh / L)
    Higher dh  -->  faster flow
    Thicker bed (L)  -->  slower flow
    Mature Schmutzdecke  -->  lower K  -->  slower flow
```

### The Schmutzdecke: A Living Biofilm

The Schmutzdecke (Tamil: *உயிர்ப்படலம்*) is the single most important component of a bio-sand filter. It is a biologically active layer, typically 2-5 cm thick, that forms at and just below the sand surface.

**Composition:**
- **Bacteria**: heterotrophic bacteria that consume dissolved organic carbon and compete with incoming pathogens for nutrients
- **Protozoa**: amoebae and flagellates that physically engulf and digest bacteria (including pathogens like E. coli and Vibrio cholerae)
- **Algae**: photosynthetic organisms (if light reaches the surface) that produce oxygen and contribute to the biofilm matrix
- **Extracellular polymeric substances (EPS)**: the "glue" that holds the biofilm together — a sticky matrix of polysaccharides, proteins, and DNA secreted by the resident organisms
- **Bacteriophages**: viruses that infect and lyse bacteria — these contribute to pathogenic virus removal

```text
    Schmutzdecke Biofilm Ecology (top 2 cm of sand, zoomed in)

    WATER ABOVE        incoming pathogen ---> (*)
    ==========================================  surface
    :: ORGANIC MAT  ~~ sticky EPS matrix ::::   |
    ::  [algae]-->O2   [algae]-->O2     :::::   |  0-2 mm
    ::............................................   |
    ::  (A) amoeba engulfs (*)  <-- PREDATION :   |
    ::     \___/                               :   |
    ::  (P) protozoa hunting bacteria          :   |  2-10 mm
    ::  [bacteriophage] --lyses--> (*)         :   |
    ::  {competing bacteria} starve pathogens  :   |
    ::............................................   |
    ::  (*) pathogen adsorbed to sand grain O  :   |
    ::    O~~~(*)  electrostatic attraction     :   | 10-20 mm
    ::  O    O    O    O  <-- sand grains      :   |
    ::............................................
    Key: (*) = pathogen   O = sand grain   [  ] = biofilm organism
    Removal: predation + competition + adsorption + die-off
```

**Maturation timeline:**
- Days 1-3: initial bacterial colonization of sand grain surfaces
- Days 3-7: biofilm thickening, EPS production begins, protozoan colonization starts
- Days 7-14: mature Schmutzdecke established in warm climates (>15 degrees C); pathogen removal efficiency reaches operational levels
- Days 14-30: continued maturation in cold climates (<10 degrees C); full maturity may require 21-30 days

**The cardinal rule**: the Schmutzdecke must NEVER be allowed to dry out. If the water level drops below the sand surface, the biofilm desiccates and dies. Recovery requires a complete re-ripening cycle of 10-14 days. The entire filter design — specifically the outlet pipe elevation — exists to prevent this.

### Pathogen Removal Mechanisms (Four Barriers in One Filter)

A bio-sand filter achieves pathogen removal through four simultaneous mechanisms. No single mechanism is sufficient alone; their combination produces the high overall removal rates.

1. **Mechanical straining**: Particles larger than the pore spaces between sand grains (~50-100 micrometres) are physically trapped in the upper sand layers. This removes: protozoan cysts (Giardia lamblia 8-15 um, Cryptosporidium parvum 4-6 um), helminth eggs (20-80 um, including Ascaris and Schistosoma), most suspended sediment, and larger algae. Mechanical straining is effective from day one — no ripening required.

2. **Adsorption**: Electrostatic and van der Waals forces attract microorganisms to sand grain surfaces. Clean silica sand grains carry a slight negative surface charge at neutral pH; many bacteria carry positive surface charges or hydrophobic surface structures that promote attachment. This mechanism is most effective for viruses (20-300 nm), which are too small for mechanical straining but readily adsorb to grain surfaces. Adsorption efficiency improves as biofilm coats the sand grains, increasing surface area and charge heterogeneity.

3. **Biological predation**: The Schmutzdecke's protozoa actively engulf bacteria. Bacteriophages within the biofilm lyse bacterial cells. Predatory bacteria (such as Bdellovibrio) attack other bacteria. This mechanism is the PRIMARY reason why a mature filter outperforms a new one by 10-100x for bacterial removal. It is effective against: E. coli, Vibrio cholerae, Salmonella, Shigella, Campylobacter, and many other waterborne bacterial pathogens.

4. **Natural die-off**: Pathogens trapped within the sand column face hostile conditions — darkness (no photosynthesis for those that need it), nutrient depletion (the resident biofilm consumes available nutrients first), temperature stress, and predation pressure. Over hours to days, trapped pathogens die. This is why the "pause period" between pours matters: it gives the filter time to kill what it has caught.

```text
    Four Barriers of Pathogen Removal (top to bottom)

    RAW WATER containing: bacteria(*) viruses(v) cysts(C) eggs(E)
    ~~~ (*)(v)(C)(E)(*)(v)(C)(E)(*)(v) ~~~ incoming water
    ============================================
    BARRIER 1: MECHANICAL STRAINING   (day 1+)
    |  pore size ~50-100 um blocks:           |
    |  (C) cysts, (E) eggs  --> TRAPPED       |
    |  (*)(v) pass through                    |
    |------------------------------------------|
    BARRIER 2: BIOLOGICAL PREDATION   (day 14+)
    |  Schmutzdecke protozoa engulf (*)       |
    |  bacteriophages lyse (v)                |
    |  competitive exclusion starves (*)      |
    |------------------------------------------|
    BARRIER 3: ADSORPTION             (day 1+)
    |  sand grain O~~~(*) electrostatic bond  |
    |  sand grain O~~~(v) van der Waals force |
    |  biofilm coat increases surface area    |
    |------------------------------------------|
    BARRIER 4: NATURAL DIE-OFF   (pause period)
    |  darkness + nutrient depletion + time    |
    |  trapped pathogens die in hours-days     |
    ============================================
    OUTLET: greatly reduced pathogen load
```

### Removal Efficiency (Peer-Reviewed Data)

| Contaminant | Removal Rate | Log Reduction | Source |
|-------------|-------------|---------------|--------|
| Bacteria (E. coli) | 90-99% | 1-2 log | CAWST 2012 field data; Stauber et al. 2006 |
| Protozoa (Giardia, Cryptosporidium) | >99% | >2 log | Palmateer et al. 1999 |
| Helminths (worm eggs) | >99% | >2 log | CAWST 2012 |
| Viruses | 70-99% | 0.5-2 log | Elliott et al. 2008 (highly variable; depends on Schmutzdecke maturity) |
| Turbidity | 85-95% reduction | — | CAWST 2012 |
| Iron | 90-95% reduction | — | CAWST 2012 (important for taste and staining) |

**Critical note**: Bio-sand filtration alone does NOT guarantee potable water to WHO standards. It is designed as one barrier in a **dual-barrier system**. Filter output should be followed by a second treatment step — UV disinfection (sunlight SODIS in PET bottles for 6+ hours), boiling (rolling boil for 1 minute), or chlorination (if available) — for full safety. This is especially true for viral removal, where bio-sand performance is most variable.

---

## Core Principles

1. **The Ripening Imperative**: A new bio-sand filter is NOT safe to drink from. The Schmutzdecke requires 10-14 days to establish its pathogen-consuming community. During the ripening period, filter output must still be boiled or otherwise treated. Mark the filter with a visible "RIPENING — BOIL OUTPUT" tag. Remove the tag only after the flow rate has noticeably decreased from initial levels (indicating biofilm growth) and a minimum of 14 days have elapsed.

2. **The Wet Rule**: The sand bed must NEVER dry out. If the water level drops below the sand surface, the Schmutzdecke dies within hours. Design the filter with a standing water level 5-10 cm above the sand surface at all times. The outlet pipe elevation controls this — the outlet must exit the container at or above the sand surface level. If you remember nothing else from this module, remember this: the sand stays wet, always.

3. **The Pause Period**: After each batch of water is poured in, the filter needs a rest period (ideally 1-6 hours, maximum 48 hours) before the next batch. This pause allows the Schmutzdecke time to consume trapped pathogens and allows natural die-off processes to work within the sand column. Continuous pouring overwhelms the biological layer, flushing live pathogens through before they can be killed. Pour — wait — pour. Never run the filter like a tap.

4. **The Grain-Size Rule**: Sand grain diameter of 0.15-0.35 mm (effective size, D10) is critical. Too coarse (>0.5 mm) = inadequate filtration, pathogens pass through. Too fine (<0.1 mm) = flow rate too slow, filter becomes unusable within days. Field test: rub sand between thumb and forefinger — it should feel distinctly gritty but individual grains should be barely visible to the naked eye. Sand the size of granulated sugar is approximately correct. River sand is usually suitable; beach sand is often too uniform and too fine; crushed rock must be carefully sieved.

5. **The Turbidity Threshold**: If source water turbidity exceeds approximately 50 NTU — visibly cloudy, you cannot see your fingers through 30 cm of water in a clear container — pre-treat by sedimentation or cloth filtration before pouring into the bio-sand filter. High turbidity clogs the Schmutzdecke prematurely, causing rapid flow-rate decline and requiring frequent "swirl and dump" maintenance that disrupts the biofilm.

---

## Practical Implementation

### Materials and Specifications

| Component | Specification | Purpose |
|-----------|--------------|---------|
| Container | 200L drum, concrete box, or ceramic vessel. Min. internal: ~30 cm x 30 cm x 90 cm tall | Filter housing |
| Fine sand | 0.15-0.35 mm effective grain size, washed until rinse water runs clear | Primary filter medium and Schmutzdecke substrate |
| Coarse sand | 0.5-1.0 mm grain size | Separation layer between fine sand and gravel |
| Fine gravel | 2-6 mm diameter | Underdrain support, prevents sand migration |
| Coarse gravel | 6-12 mm diameter | Underdrain base, surrounds drain pipe |
| Biochar (optional) | Crushed hardwood charcoal, 1-3 mm pieces | Adsorption of dissolved organics, taste/odour improvement |
| Outlet pipe | 12-20 mm diameter tube, bamboo, or copper pipe, L-shaped | Controls standing water level; sets the "wet rule" |
| Diffuser plate | Flat stone, fired ceramic disc, or perforated metal plate, ~25 cm diameter | Dissipates pour energy; prevents disturbing the Schmutzdecke |
| Lid | Any solid cover: wood plank, metal sheet, stone slab | Prevents contamination, insect entry, and algal growth |

### Filter Construction Step-by-Step

**Step 1 — Prepare the container.** Drill or cut a hole 5 cm above the bottom of the container for the outlet pipe. The hole diameter should match your pipe (12-20 mm). If using a plastic drum, heat the pipe end and push it through to create a sealed fit. If using concrete, embed the pipe during casting.

**Step 2 — Install the outlet pipe.** Insert the pipe through the hole. Inside the container, the pipe should extend horizontally to the centre of the base. Outside the container, bend the pipe upward (an L-bend or U-bend) so that the outlet opening is at the height of the intended sand surface (approximately 75-80 cm above the container bottom). This outlet elevation is what maintains the standing water head above the sand — it is the single most critical dimension in the entire filter. Seal around the pipe penetration with clay, silicone, or cement.

**Step 3 — Install the coarse gravel layer (5 cm).** Place 6-12 mm gravel evenly across the bottom, surrounding the internal portion of the outlet pipe. Level it. This layer prevents fine material from entering and clogging the drain.

**Step 4 — Install the fine gravel layer (5 cm).** Place 2-6 mm gravel on top of the coarse gravel. Level it. This is a transition layer that prevents the coarse sand above from migrating into the coarse gravel below.

**Step 5 — Install the coarse sand layer (5 cm).** Place 0.5-1.0 mm sand on top of the fine gravel. Level it. Another transition layer.

**Step 6 — Install the biochar layer (2-5 cm, optional).** If biochar is available (see cross-reference to Terra Preta module), place a 2-5 cm layer of crushed charcoal (1-3 mm pieces) on top of the coarse sand. Biochar provides additional adsorption capacity for dissolved organic compounds, pesticide residues, and taste/odour compounds. It is not required for basic pathogen removal but significantly improves water taste and provides a margin of safety against chemical contaminants. Pre-wash the biochar to remove fines.

**Step 7 — Install the fine sand layer (45-55 cm).** This is the main filter medium and the substrate for the Schmutzdecke. Pour washed fine sand (0.15-0.35 mm) in 10 cm lifts, tamping gently after each lift to eliminate air pockets — especially at the edges against the container wall. Tamp firmly at the perimeter to prevent short-circuiting (water finding a fast path along the wall). The final sand surface should be level and at the height where the outlet pipe exits the container on the outside.

**Step 8 — Sand washing procedure.** This step must be completed BEFORE Step 7. Wash sand in small batches (half a bucket at a time) by adding water, stirring vigorously, and pouring off the cloudy water. Repeat until the rinse water runs clear — typically 5-10 washes per batch. Unwashed sand contains clay and silt particles that will clog the filter within days. This is the most labour-intensive part of construction; budget 2-4 hours for a single filter's sand supply.

**Step 9 — Place the diffuser plate.** Set a flat stone, ceramic disc, or perforated plate on top of the sand surface, resting on small spacers (pebbles or sticks) to leave a 2-3 cm gap above the sand. When water is poured into the filter, it hits the diffuser plate instead of the sand surface, preventing the pour from cratering the Schmutzdecke. This is essential — without a diffuser, every pour destroys the biofilm you are trying to cultivate.

**Step 10 — Initial charge and ripening.** Fill the filter with water slowly (pour onto the diffuser plate). Water will begin flowing from the outlet pipe. The initial output will be cloudy — this is normal. Continue pouring batches of water (20-40 litres at a time, with 1-6 hour pauses between batches) for 10-14 days. During this entire period, ALL output water must be boiled or otherwise disinfected. The filter is "ripe" when: (a) the flow rate has decreased noticeably from initial rates, (b) the output water is visually clear, and (c) at least 14 days have elapsed. Attach a "RIPENING COMPLETE" date tag to the filter.

### ASCII Cross-Section Diagram

```text
         ____________________
        |                    |  <--- Lid (keeps insects and debris out)
        |   [ RAW WATER ]   |
        |     poured onto    |
        |   diffuser plate   |
        |         vvv        |
        |  ==================|  <--- Diffuser plate (flat stone / perforated plate)
        |  ~~~~~~~~~~~~~~~~~~|
        |  ~ STANDING WATER ~|  5-10 cm  (maintained by outlet pipe height)
        |  ~~~~~~~~~~~~~~~~~~|
  ===== |  ..................|  <--- Schmutzdecke (living biofilm, 2-5 cm)    ======
  |     |::::::::::::::::::::|                                                    |
  |     |::::::::::::::::::::|                                                    |
  |     |::::: FINE SAND ::::|  45-55 cm  (0.15-0.35 mm grain size)               |
  |     |::::::::::::::::::::|  <--- Primary filter bed                           |
  |     |::::::::::::::::::::|                                                    |
  |     |::::::::::::::::::::|                                                    |
  |     |####################|                                                    |
  |     |#### BIOCHAR #######|  2-5 cm  (optional, 1-3 mm charcoal pieces)        |
  |     |####################|                                                    |
  |     |.  .  .  .  .  .  .|                                                    |
  |     | COARSE SAND  . . . |  5 cm  (0.5-1.0 mm)                               |
  |     |.  .  .  .  .  .  .|                                                    |
  |     |o o o o o o o o o o |                                                    |
  |     | FINE GRAVEL  o o o |  5 cm  (2-6 mm)                                    |
  |     |o o o o o o o o o o |                                                    |
  |     |O O O O O O O O O O |                                                    |
  |     | COARSE GRAVEL  O O |  5 cm  (6-12 mm)                                   |
  |     |O O O O O O O O O O |                                                    |
  |     |______[====]________|  <--- Internal drain pipe (perforated)             |
  |            |                                                                  |
  |            | outlet pipe                                                      |
  |            | (exits container                                                 |
  |            |  5 cm above base)                                                |
  |            |                                                                  |
  ============ |  <--- Outlet pipe rises OUTSIDE container to sand-surface height |
               |                                                                  
               V  SAFE WATER outlet (elevated to maintain standing water head)    
          [ COLLECTION VESSEL ]
```

**Key dimensions (total height ~85-95 cm internal):**
- Coarse gravel: 5 cm
- Fine gravel: 5 cm
- Coarse sand: 5 cm
- Biochar (optional): 2-5 cm
- Fine sand: 45-55 cm
- Standing water: 5-10 cm
- Freeboard above water: 15-20 cm (to contain pour volume)

### Filter Sizing for a Settlement

| Settlement Size | Daily Water Need (20 L/person) | Filters Required | Notes |
|----------------|-------------------------------|-----------------|-------|
| 10 people | 200 L/day | 1 filter | Plus 1 backup during maintenance |
| 25 people | 500 L/day | 1-2 filters | Plus 1 backup |
| 50 people | 1,000 L/day | 2-3 filters | Plus 1 backup; stagger construction by 1 week so ripening periods do not overlap |
| 100 people | 2,000 L/day | 4-5 filters | Dedicated water team of 2 people required |

Construction time: 1-2 days per filter, assuming sand is pre-washed and materials are staged. Sand washing is the bottleneck — budget 1 day of labour per filter just for sand preparation. Total system deployment for a 50-person settlement: approximately 1 week from material gathering to first ripe filter.

### Maintenance Protocol

**Daily:**
- Pour water in batches of 20-40 litres onto the diffuser plate. Allow 1-6 hour pause periods between batches. Never pour continuously.
- Verify that the standing water level remains above the sand surface after the outlet flow stops. If it does not, the outlet pipe elevation is wrong — correct it immediately.
- Keep the lid on the filter when not actively pouring.

**Monthly:**
- Check the flow rate by timing how long it takes to fill a 1-litre container from the outlet. A healthy filter should fill 1 litre in 1-2.5 minutes (0.4-1.0 L/min). If the flow rate is below 0.1 L/min, the Schmutzdecke is over-mature and maintenance is needed.

**When flow rate drops below usable (the "swirl and dump"):**
1. Remove standing water above the sand surface (scoop or siphon it out).
2. Insert your clean hand (washed, no soap residue) into the top 1-2 cm of sand.
3. Swirl gently — agitate the top sand layer to release trapped organic matter into suspension.
4. Pour off the cloudy water. Repeat 2-3 times until the water above the sand is only slightly cloudy.
5. Do NOT remove more than 2 cm of sand depth. Do NOT scrape or remove sand from the filter.
6. Refill with water. The filter will need 2-3 days to re-establish the Schmutzdecke. During this period, boil all output.

**Annual:**
- Measure total sand depth. If it has dropped below 45 cm (from repeated swirl-and-dump cycles removing small amounts of sand each time), add fresh washed sand to restore the full 50-55 cm depth. The new sand goes on top. Allow 7-10 days for the Schmutzdecke to re-colonize the new surface.

**NEVER:**
- Use soap, bleach, chlorine, or any chemical inside the filter — these kill the Schmutzdecke.
- Allow the sand to dry out — even for a few hours in hot weather.
- Remove the diffuser plate and pour water directly onto the sand surface.
- Dip dirty hands, cups, or utensils into the collection vessel.

---

## Common Failure Modes

1. **Schmutzdecke Death (Drying)**: The standing water drops below the sand surface and the biofilm desiccates. This can happen from a leaking container, an improperly set outlet pipe, or simply forgetting to add water for a day in hot weather. **Recovery**: Refill with water and wait 10-14 days for complete re-ripening. During this time, boil all filter output. **Prevention**: The outlet pipe elevation must be at or above the sand surface. Inspect the container monthly for leaks. In hot, dry climates, add a batch of water every 24 hours minimum even if demand is low.

2. **Premature Clogging**: Flow rate drops to near zero within days of construction. **Cause**: Sand is too fine (D10 < 0.1 mm) or source water is excessively turbid (>50 NTU), loading the Schmutzdecke with sediment faster than biological processes can break it down. **Prevention**: Test sand grain size before installation. Pre-treat turbid water by sedimentation — fill a bucket, let it stand for 2-4 hours, decant the clear top 80% into the filter, discard the sediment. Cloth filtration through folded cotton sari cloth (4-8 layers) reduces turbidity by 40-50%.

3. **Short-Circuiting**: Water finds a fast path along the container wall or through cracks, bypassing the sand column entirely. Output water quality is poor despite a mature-looking filter. **Cause**: Inadequate sand packing against container walls, cracks in a concrete container, or a warped plastic drum creating gaps. **Prevention**: Tamp sand firmly during installation, especially at edges. Use a round container — rectangular containers have corners where channels form. Inspect concrete containers for cracks before filling. If short-circuiting is suspected (output remains turbid despite 14+ days of ripening), empty the filter and rebuild with careful attention to wall contact.

4. **Post-Filtration Contamination**: The filter performs correctly, but the water is re-contaminated between the outlet and the point of consumption. Dirty hands touching the outlet pipe, insects entering the collection vessel, or using a contaminated cup to scoop water from the vessel. **Prevention**: Cover the outlet pipe when not in use. Use a collection vessel with a narrow mouth or a tap/spigot. Never dip hands or utensils into stored filtered water — pour it out. Clean the collection vessel daily with boiling water.

5. **Cold-Climate Failure**: At temperatures below 5 degrees C, biological activity in the Schmutzdecke slows dramatically. Pathogen removal efficiency for bacteria can drop by 50% or more. The filter may appear to function normally (water flows, output is clear) but is not achieving adequate disinfection. **Prevention**: Insulate the filter with straw bales, earth banking, or house it inside a heated shelter. In very cold climates (<5 degrees C sustained), bio-sand filtration must be supplemented with boiling or SODIS as a mandatory second barrier, not merely a recommended one.

---

## Vocabulary of the Foundation

- **Schmutzdecke** (Tamil: *உயிர்ப்படலம்*): The biologically active layer at the sand surface composed of bacteria, protozoa, algae, and extracellular polymeric substances. The primary pathogen removal mechanism in a bio-sand filter.
- **Darcy's Law**: The equation governing fluid flow through porous media: Q = K x A x (dh/L). Predicts filter flow rate from sand properties, filter dimensions, and water head.
- **Hydraulic conductivity (K)**: A measure of how easily water flows through a porous medium (units: m/day). Fine sand: 1-5 m/day. Gravel: 100-1000 m/day.
- **Turbidity**: The cloudiness of water caused by suspended particles. Measured in Nephelometric Turbidity Units (NTU). Clear water: <1 NTU. Visibly cloudy: >50 NTU.
- **NTU (Nephelometric Turbidity Unit)**: The standard unit of turbidity measurement. WHO guideline for drinking water: <1 NTU ideal, <4 NTU acceptable.
- **Log reduction**: A logarithmic measure of pathogen removal. 1 log = 90% removal, 2 log = 99%, 3 log = 99.9%. Bio-sand filters achieve 1-2 log for bacteria.
- **Ripening**: The 10-14 day period during which the Schmutzdecke establishes itself in a new or recently disturbed filter. Filter output is NOT safe during ripening.
- **Effective grain size (D10)**: The sieve opening that passes 10% of the sand sample by weight. For bio-sand filters: D10 = 0.15-0.35 mm.
- **Adsorption**: The adhesion of molecules or microorganisms to a surface (sand grains, biochar) via electrostatic or van der Waals forces. Distinct from absorption (bulk uptake).
- **SODIS (Solar Water Disinfection)**: A method of disinfecting water by exposing it to sunlight in clear PET bottles for 6+ hours. UV-A radiation and thermal inactivation kill pathogens. Recommended as a second barrier after bio-sand filtration.
- **CFU (Colony-Forming Unit)**: A measure of viable bacteria in a water sample. WHO standard for drinking water: 0 CFU/100 mL for E. coli.
- **Potable water**: Water that is safe for human consumption — free of pathogens, toxic chemicals, and excessive turbidity. WHO Guidelines for Drinking-water Quality (4th ed.) define the standard.
- **Biochar**: Charcoal produced by pyrolysis of biomass in low-oxygen conditions. When crushed and incorporated into a bio-sand filter, it enhances adsorption of dissolved organic compounds and improves taste.

---

## Cross-References

- [01. Rationale: Water and Sanitation](01_Rationale_and_Importance.md)
- [03. Immediate Sanitation](03_Immediate_Sanitation.md)
- [06. Thermophilic Sanitation Math](06_Thermophilic_Sanitation_Math.md) — pathogen die-off data relevant to understanding what the filter must remove
- Outcome 1 Section 02: [04. Water Sovereignty and Hydrams](../../Outcome_1_Locating_Refugia/02_The_Site/04_Water_Sovereignty_and_Hydrams.md) — the water supply system that feeds the filter
- Outcome 1 Section 02: [05. Hydrological Analysis](../../Outcome_1_Locating_Refugia/02_The_Site/05_Hydrological_Analysis_and_Watershed_Math.md) — watershed math for water availability
- Outcome 2 Section 04: [02. Terra Preta and Biochar](../04_Food_and_Soil_Sovereignty/02_Terra_Preta_and_Biochar.md) — biochar production for the optional biochar layer

---

## Further Study

- CAWST (Centre for Affordable Water and Sanitation Technology), *Biosand Filter Manual* (2012) — the definitive field construction guide, freely available at cawst.org
- David Manz, *Slow Sand Filtration: Demand vs Supply* (2007) — academic treatment of intermittent slow sand filtration by the inventor of the modern biosand filter
- WHO, *Guidelines for Drinking-water Quality* (4th ed., 2017) — water quality standards and household water treatment recommendations
- Huisman & Wood, *Slow Sand Filtration* (WHO, 1974) — classic reference on slow sand filtration theory and municipal-scale design
- Mark Sobsey, *Managing Water in the Home: Accelerated Health Gains from Improved Water Supply* (WHO, 2002) — comparative analysis of household water treatment methods
- Stauber et al., "A Randomized Controlled Trial of the Concrete Biosand Filter in Bonao, Dominican Republic" (2006) — field trial data on pathogen removal
- Elliott et al., "Reductions of E. coli, echovirus type 12 and bacteriophages in an intermittently operated household-scale slow sand filter" (2008) — virus removal data

---

## Glossary Reference

*See [../../Glossary.md](../../Glossary.md) for full definitions of:*
* **Execution**
* **Preparation**
* **Refugia**
* **Terra Preta**
