# The Ledger of Consequences (விளைவுகளின் ஏடு)

**Why the number matters, what happens when you ignore it, and how to tell an exact instruction from an approximate one.**

Companions: [WHAT_IF_INDEX.md](WHAT_IF_INDEX.md) · [settling_pressure_test_report.md](settling_pressure_test_report.md) · [pressure_test_report.md](pressure_test_report.md)

> **Read this before you build anything.** Most settlement deaths are not caused by ignorance of *what* to do — the modules state that clearly. They are caused by not understanding *what happens if you don't*, and therefore treating a life-or-death instruction as a helpful suggestion. A person who knows that fermenting below pH 4.6 is "recommended" will round it off on a busy day. A person who knows that pH 4.7 grows an invisible, odorless toxin that paralyzes and kills within three days will measure every batch. **This document exists to convert instructions into understood consequences**, because an understood consequence is obeyed and a bare instruction is negotiated away.

---

## 1. The Two Ways Instructions Kill

Failures of instruction come in exactly two shapes, and both are fatal:

1.  **Treating an exact instruction as approximate.** The classic settlement-killer. Someone decides that 55 °C for fifteen days is "about two weeks and pretty warm," applies the compost early, and seeds an Ascaris outbreak that returns through the salad. The number was not a suggestion; it was the boundary of a physical law.
2.  **Treating an approximate instruction as exact.** The subtler killer, of morale and time. Someone refuses to plant because they lack the "correct" 3.2 m row spacing, or burns out chasing a precision the task never required. Not every number is sacred; mistaking craft-judgment for law wastes the effort you need for the numbers that *are* sacred.

The meta-skill this document teaches is **telling the two apart.** Every instruction in the Aadhiyandham manual belongs to one of three precision tiers. Learn to read the tier, and you will spend your fear where it saves lives and your flexibility where it saves effort.

## 2. The Three Precision Tiers

```text
  TIER L — LAW            TIER C — CRAFT           TIER P — PREFERENCE
  (exact; deviation       (a range; the number     (adaptable; choose
   kills or destroys)      depends on conditions     to taste / context)
                           and you calibrate by
                           a test, not a guess)
  --------------------    ---------------------     --------------------
  MEASURE IT.             LEARN THE TEST.           ADAPT FREELY.
  Do not eyeball.         The test, not the         Local materials,
  Do not round.           number, is the truth.     taste, and custom
  Do not "improve."       Feedback calibrates it.   all override the book.

  e.g. canning pH 4.6     e.g. biochar cure time    e.g. garden layout
       55 C x 15 days          "snap test" dryness       ritual timing
       30 m latrine setback    seed row spacing          building shape
       CO ventilation          thatch pitch (>floor)     dye colors
       tourniquet placement    fermentation days
```

*   **Tier L — Law.** A physical, chemical, or biological threshold with a sharp edge and little or no warning on the far side. Below/above it, people die or the system fails catastrophically. Deviation is not a gamble with better odds; it is a coin that has already landed. **You measure these. You do not trust your eye, your memory, or your mood.** When this document marks something **[L]**, treat the number as you would treat the edge of a cliff in fog.
*   **Tier C — Craft.** A quantity that genuinely depends on local conditions — humidity, wood species, temperature, soil — so the book gives a *range* and a *test* that tells you when you are inside it. The number is a starting hypothesis; the test is the truth. Here, blindly obeying a single number is *worse* than learning the test, because the same "3 weeks" that dries wood in Arizona rots it in Oregon. When marked **[C]**, the instruction reads: *learn the test, calibrate to your ground.*
*   **Tier P — Preference.** Comfort, aesthetics, custom, efficiency. Adapt freely; the manual has no authority here and claims none.

**The single most dangerous error is tier confusion** — importing a Tier-C attitude ("roughly, it'll be fine") into a Tier-L instruction. The ledger below tags every critical instruction so you cannot make that mistake by accident.

## 3. How to Read the Ledger

Each entry gives: the **instruction** and its **tier**; the **exact value** (for Law) or **test** (for Craft); **what physically happens if you deviate**, traced all the way to the human consequence; the **onset** (how fast it hits — and crucially, whether it warns you); and the **margin** (how much room for error actually exists). Onset matters because *silent, delayed* consequences are the ones that kill — you get no feedback to correct by. The source module is linked for the full method.

> **The onset column is the heart of this document.** A consequence that announces itself (smoke, pain, bad smell) is survivable — you notice and correct. A consequence that is **silent and delayed** (CO, botulinum, Ascaris, methemoglobinemia, a weak roof joint) gives no such mercy. Fear those most.

---

## 4. Water & Drinking Safety

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Bio-sand filter maturation before drinking | **L** | 10–14 days ripening; **dual barrier always** (filter + boil/SODIS) | Skip ripening or skip the second barrier → filter passes bacteria/viruses → cholera, dysentery, giardia | Illness 6h–3 days; **cholera CFR 25–50% untreated** | [Bio-Sand Filtration](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/02_Bio_Sand_Filtration.md) |
| Schmutzdecke must never dry out | **L** | Keep 5 cm water above sand at all times | Sand bed dries → biolayer dies silently → filter looks fine, filters nothing → 10–14 days to re-ripen with no protection meanwhile | **Silent** — no visible change | [Bio-Sand Filtration](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/02_Bio_Sand_Filtration.md) |
| Boil to a true rolling boil | **L** | Full rolling boil (altitude lowers temp — boil longer high up) | "Almost boiling" leaves heat-tolerant cysts → giardia/crypto | Days–weeks; chronic diarrhea, dehydration | [Arrival Protocol](Outcome_1_Locating_Refugia/01_The_Journey/12_Journey_Scenarios_and_Contingencies/05_Arrival_Protocol_First_72_Hours.md) |
| Nitrate in infant drinking water | **L** | <10 mg/L nitrate-N for infants & pregnancy | Old manure/latrine leachate or fertilized-runoff water → methemoglobinemia ("blue baby") → oxygen starvation | Hours in infants; **can be fatal**, and **odorless/tasteless** | [Water Contaminant Testing](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/07_Water_Contaminant_Testing_and_Remediation.md) |
| Test/avoid arsenic & heavy metals | **L** | Avoid suspect geology; do not rely on boiling (concentrates it) | Boiling arsenic water *increases* concentration → years of exposure → cancers, neuropathy | **Silent, years** | [Water Contaminant Testing](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/07_Water_Contaminant_Testing_and_Remediation.md) |
| Filter flow rate | **C** | Test: outflow clear, ~0.4–0.6 L/min through a mature filter | Too fast = under-treated (retest); too slow = clogged (clean & re-ripen). Calibrate by clarity + timing, not a fixed number | Correctable | [Bio-Sand Filtration](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/02_Bio_Sand_Filtration.md) |

## 5. Sanitation & Humanure

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Latrine/humanure setback from water | **L** | **30 m** minimum; **50 m** in sand/gravel; always *downhill* of water | Closer or uphill → fecal plume reaches well/spring → whole-settlement dysentery/cholera | Days; can infect everyone at once | [Immediate Sanitation](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/03_Immediate_Sanitation.md) |
| Day-One sanitation | **L** | Latrine operational **before the first night** | Open defecation for even a day → flies → fecal-oral loop established in camp | 2–5 days to first cases | [Arrival Protocol](Outcome_1_Locating_Refugia/01_The_Journey/12_Journey_Scenarios_and_Contingencies/05_Arrival_Protocol_First_72_Hours.md) |
| Thermophilic compost temperature × time | **L** | **55 °C for 15 consecutive days** (settlement standard); turn ≥3× so all mass passes the hot core | Cooler/shorter → *Ascaris* eggs survive (most heat-resistant pathogen) → re-infection through crops | **Silent** until illness weeks later | [Thermophilic Sanitation Math](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/06_Thermophilic_Sanitation_Math.md) |
| Humanure curing before soil use | **L** | **12 months** after the *last* addition, then pass the 3-tier check (time + smell/worms + ≥80% seed germination) | Applying early → live pathogens on food crops | Weeks; recurring outbreaks | [Humanure Integration](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/05_Humanure_Integration.md) |
| Carbon cover after every deposit | **C→L** | 5–10 cm dry cover **every time** (this frequency is Law; the exact depth is craft) | Skipping cover → anaerobic, fly-breeding, odor, no thermophilic heat | Days (flies); the compost simply never works | [Humanure Composting](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/04_Humanure_Composting.md) |
| Minimum pile volume for heat | **L** | ≥1 m³ | Smaller pile loses heat faster than it makes it → never reaches 55 °C → pathogens survive | Silent | [Humanure Composting](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/04_Humanure_Composting.md) |
| First-3-years crop restriction | **L** | Humanure only on grain/fruit trees/above-ground fruit — **never root crops eaten raw** | Contact between residual pathogens and raw-eaten crops | Weeks | [Humanure Integration](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/05_Humanure_Integration.md) |

## 6. Food Preservation & Storage

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Fermentation/anaerobic-storage acidity | **L** | **pH < 4.6** (ferment reaches 3.5–4.0 in 7–14 days at 18–22 °C with 2–3% salt) | Above 4.6 in an anaerobic jar → *C. botulinum* grows → botulinum toxin → paralysis, respiratory arrest | 12–72 h; **odorless, tasteless, no spoilage cue**; often fatal without a ventilator | [Long-Term Food Preservation](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/04_Long_Term_Food_Preservation.md) |
| Fermentation salt ratio | **L** | 2–3% salt by weight | Too little → pathogens outcompete *Lactobacillus* before acid drops → spoilage/illness; too much → ferment stalls (stays unsafe) | Days | [Long-Term Food Preservation](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/04_Long_Term_Food_Preservation.md) |
| Drying completeness | **C→L** | Test: **snaps, does not flex** (~<15%; jerky <10%) | Under-dried → mold/bacteria in storage → mycotoxins, spoilage. The *test* is the law; the % is the guide | Weeks | [Long-Term Food Preservation](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/04_Long_Term_Food_Preservation.md) |
| Discard mold-toxin grain | **L** | Discard ergot (dark curved kernels) & visibly molded grain; do **not** just cook it off | Ergot → gangrene/convulsions; aflatoxin → liver failure/cancer. Heat does not destroy these toxins | Ergot: hours–days; aflatoxin: silent, years | [Food Toxins & Storage Safety](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/09_Food_Toxins_and_Storage_Safety.md) |
| Root cellar temperature | **C** | Test: hold **1–5 °C**; Q10 rule — every +10 °C ≈ doubles spoilage | Warm cellar (10–15 °C) → stores last 2–3 mo not 6–8 → winter famine gap. Calibrate with a thermometer + vent control | Slow; discovered mid-winter | [Refugia Pantry Physics](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/08_Refugia_Pantry_Physics.md) |
| Cellar/pantry ventilation | **L** | Low intake + high exhaust, always open | Sealed cellar → CO₂ pools from respiration → asphyxiation of anyone entering (>10% CO₂ = unconsciousness) | Minutes; **silent** | [Refugia Pantry Physics](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/08_Refugia_Pantry_Physics.md) |
| Winter caloric reserve | **L** | Population × days × 2,500 kcal × 1.25 margin (≈28 M kcal / 50 people / 180 days) | Under-store → run out before first harvest → starvation, targeting children/elderly first | The hungry gap; predictable to the week | [Refugia Pantry Physics](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/08_Refugia_Pantry_Physics.md) |
| Arrival timing vs. the growing season | **L** | Arrive at the growing-season start (spring, or the rains); never arrive into the gap season without a full carried reserve | Autumn/dry-season arrival on rations → nothing to plant → stores run out mid-gap-season → **starvation, no recovery once the season closes** | Silent for months, then absolute (Feb/dry-season) | [First-Year Food Security & Arrival Timing](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/10_First_Year_Food_Security_and_Arrival_Timing.md) |
| First-harvest yield assumption | **L** | Plan the reserve at **0.3–0.6× expected** (new-ground first-year reality) | Planning at full yield → 40% harvest → reserve 60% short, discovered in autumn too late to grow more | Discovered at harvest; fatal by late gap season | [First-Year Food Security & Arrival Timing](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/10_First_Year_Food_Security_and_Arrival_Timing.md) |
| Acorn / wild-food processing | **L** | Leach acorns (cold 1–3 days running water, or 3–5 hot changes) | Unleached → tannin poisoning; misID → hemlock/death-cap death | Hours | [Emergency Nutrition](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/06_Emergency_Nutrition.md) |
| Never feed honey to infants <12 mo | **L** | Zero honey under 1 year | Honey carries *C. botulinum* spores → infant botulism | Days; often fatal | [Deficiency Diseases & Heat Illness](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/10_Deficiency_Diseases_and_Heat_Illness.md) |

## 7. Soil, Seed & Biochar

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Charge biochar before soil use | **L** | Soak in compost/urine **2+ weeks** first | Raw biochar scavenges soil nitrogen → crop nitrogen-starves → yield crash in the year you can least afford it | One growing season | [Terra Preta & Biochar](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/02_Terra_Preta_and_Biochar.md) |
| Seed population for cross-pollinators | **L** | Corn **≥200 plants**; isolate 300 m–1 km | Fewer → inbreeding depression → variety collapses in 3–5 generations (irreversible loss of your food genetics) | Years; **irreversible** | [Heirloom Seed Banking](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/03_Heirloom_Seed_Banking.md) |
| Three-copy seed rule | **L** | Active + sealed reserve + trade copy of every variety | One store lost to damp/pest/fire → variety extinct if it was the only copy | Instant, on loss; irreversible | [Heirloom Seed Banking](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/03_Heirloom_Seed_Banking.md) |
| Seed storage dryness/cool | **C** | "100 Rule": moisture % + temp °F < 100; Harrington: −1% moisture or −5 °C ≈ ×2 life | Warm/damp storage → viability quietly decays → dead seed discovered at planting | Silent until spring | [Heirloom Seed Banking](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/03_Heirloom_Seed_Banking.md) |
| Biochar feedstock dryness (pyrolysis) | **C** | Test: snap-dry (<15%); pieces 2–5 cm | Wet feedstock → gasification fails, makes smoke not char. Test, don't guess | Immediate (batch fails) | [Pyrolysis Engineering](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/07_Pyrolysis_Engineering_and_TLUD_Gasifiers.md) |

## 8. Health & Medicine

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Escalate a non-improving infection | **L** | Botanical antimicrobials fail → **escalate if no improvement in 48 h** or redness expands >2 cm | Waiting on garlic/honey past their ceiling → cellulitis → sepsis | Sepsis in 7–14 days; **~80% fatal** without systemic antibiotics | [Temperate Antibiotic Kit](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/03_Temperate_Antibiotic_Kit.md) |
| Do not close a wound after the golden period | **L** | Close within **6–8 h**; after that, leave open | Sealing contamination inside → abscess → sepsis | Days | [Advanced Trauma Care](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/04_Advanced_Trauma_Care.md) |
| Tourniquet for arterial bleed | **L** | Apply if bright-red spurting doesn't stop in 30 s pressure; **tight enough to stop arterial flow** | Too loose → occludes veins only → *increases* blood loss; delay → death | **<5 min** for femoral/brachial | [Advanced Trauma Care](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/04_Advanced_Trauma_Care.md) |
| Newborn first breath | **L** | Stimulate to breathe within the **"golden minute"** (60 s) | No breathing → brain damage at ~4 min, death ~10 min | Minutes | [Midwifery & Childbirth](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/07_Midwifery_and_Childbirth.md) |
| Postpartum hemorrhage response | **L** | Act at **>500 mL** loss (massage → bladder → compression ladder) | Delay → exsanguination | **15–30 min** to death | [Midwifery & Childbirth](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/07_Midwifery_and_Childbirth.md) |
| Keep newborns warm & dry | **L** | Skin-to-skin; do **not** routine-bathe wet-and-cold | Newborns lose heat ~4× adults (0.1 °C/min wet) → hypothermia | 10–15 min | [Midwifery & Childbirth](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/07_Midwifery_and_Childbirth.md) |
| Medicinal-plant dose ceilings | **L** | Willow bark: not <12 y, stop on dark stools; comfrey: never internal/prolonged; pennyroyal/foxglove: named toxics | Overdose → GI hemorrhage (salicylate), liver failure (comfrey), abortion (pennyroyal), fatal arrhythmia (foxglove) | Hours–weeks | [Ancient Medicine](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/06_Ancient_Medicine.md) |
| Topical allicin (garlic) time limit | **L** | ≤15–30 min on skin; use crushed garlic within ~2 h | Longer contact → chemical burn | Under an hour | [Temperate Antibiotic Kit](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/03_Temperate_Antibiotic_Kit.md) |
| Anti-scurvy intake in winter | **L** | Daily vitamin-C source (pine-needle tea, rose hips, sprouts) | None → scurvy (collagen fails) → hemorrhage, death | **6–12 weeks** | [Deficiency Diseases & Heat Illness](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/10_Deficiency_Diseases_and_Heat_Illness.md) |
| Nixtamalize maize if it's a staple | **L** | Treat maize with wood-ash lime before eating as a staple | Untreated maize as >70% of diet → niacin locked → **pellagra** (dermatitis, diarrhea, dementia, death) | Weeks–months | [Deficiency Diseases & Heat Illness](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/10_Deficiency_Diseases_and_Heat_Illness.md) |
| Morning light / dark-at-night | **C** | 30+ min morning sun; red-only, <50 lux, below eye level after dark | Chronic disruption → immune drop, poor sleep, mood collapse. Calibrate to your latitude/season | Weeks (cumulative) | [Spectral Management](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/09_Spectral_Management_and_Circadian_Health.md) |

## 9. Shelter, Fire & Heat

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Never seal all ventilation with a fire burning | **L** | Always keep a working smoke hole / chimney draft | CO builds (binds hemoglobin ~200× O₂) → sleeping occupants never wake | **1–2 h; odorless, silent, fatal** | [Shelter & Thermal Grounding](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/04_Shelter_and_Thermal_Grounding.md) |
| Rocket-stove riser insulation | **C→L** | Riser must reach 540–650 °C (insulate, e.g. wood ash) | Uninsulated → incomplete combustion → smoke → CO + chronic respiratory harm indoors | Immediate smoke (a warning) → chronic | [Thermal Mass Cooking](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/05_Thermal_Mass_Cooking.md) |
| Thatch roof pitch | **C** | Floor of **45–50°**; steeper sheds better | Below floor → water soaks in → rot, leak, collapse. Above floor is fine (Craft upward, Law at the floor) | Seasons | [Shelter & Thermal Grounding](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/04_Shelter_and_Thermal_Grounding.md) |
| Foundation above grade + drainage | **L** | Stone/gravel base **≥30 cm** above grade | Rising damp → sill rot / wall erosion → collapse (the most common cause of building failure) | Years; then sudden | [Structural Engineering](Outcome_5_Decadal_Resilience/09_The_Mechanics/06_Advanced_Structural_Engineering.md) |
| Do not mortar before a hard freeze | **L** | No mortar if <5 °C within 48 h | Mortar freezes pre-carbonation → 50–70% strength loss → joint/wall failure later | Delayed; sudden collapse | [Structural Engineering](Outcome_5_Decadal_Resilience/09_The_Mechanics/06_Advanced_Structural_Engineering.md) |
| Heat-illness limits (hot climates/work) | **L** | Rest/shade/water; act on hot-dry skin + confusion | Ignored → heat stroke (core >40 °C) → organ failure | 30 min–hours; can be fatal | [Deficiency Diseases & Heat Illness](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/10_Deficiency_Diseases_and_Heat_Illness.md) |

## 10. Chemistry, Ceramics & Defense

| Instruction | Tier | Exact value / test | Deviate → mechanism → consequence | Onset | Module |
|:---|:--|:---|:---|:---|:---|
| Lye/quicklime handling | **L** | PPE; add lye *to* water; never near aluminum; flush eyes 15 min | Splash → deep burns, **blindness**; lye + aluminum → explosive hydrogen | Seconds | [Foundational Chemistry](Outcome_5_Decadal_Resilience/09_The_Mechanics/07_Foundational_Chemistry.md) |
| Ceramic wedging & drying before firing | **L** | ≥100 spiral kneads (no bubbles on cut); bone-dry 2–4 weeks | Trapped air/moisture → vessel explodes in kiln → lost ware/kiln → no water-storage vessels → contaminated water → disease | Immediate (explosion); disease cascade in weeks | [Ceramic Synthesis](Outcome_5_Decadal_Resilience/09_The_Mechanics/08_Ceramic_Synthesis.md) |
| Prescribed-burn weather window | **L** | ALL of: <25 °C, >40% RH, <10 km/h wind, favorable direction, no forecast shift 12 h | Any parameter marginal → fire escapes control line → becomes the wildfire you were preventing → settlement destroyed | Minutes once loose | [Wildfire Defensible Space](Outcome_3_Perimeter_Defense/07_Passive_Defense/03_Wildfire_Defensible_Space.md) |
| Crown spacing (defensible space) | **L** | ≥3 m edge-to-edge (6 m conifers) | Too close → surface fire climbs into canopy → crown fire → structures ignite → <15 min to evacuate | Minutes in an event | [Wildfire Defensible Space](Outcome_3_Perimeter_Defense/07_Passive_Defense/03_Wildfire_Defensible_Space.md) |
| Quarantine new livestock | **L** | ≥14 days isolation before joining herd | Skip → foot-and-mouth/avian flu/anthrax enters herd → mass die-off → protein & traction collapse | Days–weeks | [Livestock & Mechanical Animals](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/02_Livestock_and_Mechanical_Animals.md) |
| Security-duty rotation | **L (social)** | Rotate the watch; never a permanent warrior class | Fixed guard class → monopoly on force → rules the settlement (every historical case) | Months–years; hard to reverse | [Active Threat Rationale](Outcome_3_Perimeter_Defense/07a_Active_Threat_Response/01_Rationale_and_Importance.md) |

---

## 11. The Meta-Failure: Scripture or Suggestion

There are two ways to misuse this entire manual, and both are covered by the project's own epistemics ([The Scientific Method](Outcome_5_Decadal_Resilience/11_The_Next_Generation/08_The_Scientific_Method.md)):

*   **Treating the manual as scripture** — obeying every number as sacred, including the Tier-C craft ranges, refusing to adapt to your actual soil and wood and weather. This ossifies into the dogma the project is built to outlive, and it wastes the attention you need for the Law-tier numbers. *The book is a hypothesis; your calibrated test is the evidence.*
*   **Treating the manual as suggestion** — rounding off the Tier-L laws because they are inconvenient, "improving" on thresholds you do not understand, trusting your eye where a physical law demands a measurement. This is the error that fills graves.

The correct stance is the one this document is built to enable: **know which is which.** Obey the laws to the letter *because you understand what they defend against*; calibrate the crafts by their tests *because you understand what varies*; adapt the preferences freely *because you understand they are yours*.

## 12. Building the Habit (how a settlement makes this stick)

1.  **Post the Law-tier list where the work happens.** The canning laws by the crocks; the compost temperature-and-time by the bins; the CO rule by every hearth; the lye rule by the ash barrel. Bare numbers on a wall save lives that buried numbers in a book do not.
2.  **Teach the consequence, not just the rule, to every apprentice.** A person who can recite *why* pH 4.6 matters will never round it. Recitation of the rule alone predicts nothing; recitation of the consequence predicts obedience. This is a direct application of the [Master/Apprentice](Outcome_5_Decadal_Resilience/10_The_Society/01_Rationale_and_Importance.md) doctrine.
3.  **Measure the Law tier; never eyeball it.** Build and keep the cheap instruments — a compost thermometer, pH cabbage-juice or litmus, a way to time a boil. A settlement that cannot measure its Law-tier thresholds is flying blind past cliffs.
4.  **When you deviate, write down what happened.** Every deviation is an experiment. If it was survivable, you learned a tolerance; if it was not, the next reader must learn it from your record, not their own body. Add confirmed consequences to this ledger. *That is how the ledger stays alive — and how you repay the people whose deaths taught the entries already here.*

> Every number in the Law column was paid for once, historically, in lives. The point of writing it down is that it should never have to be paid for again.

## Glossary Reference

*See [Glossary.md](Glossary.md) for full definitions of:*

*   **Allicin**
*   **Bio-Sand Filtration**
*   **Biochar**
*   **Pathogen**
*   **Pyrolysis**
*   **Refugia**
*   **Schmutzdecke**
*   **Terra Preta**

