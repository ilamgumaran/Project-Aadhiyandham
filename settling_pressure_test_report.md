# Settling Pressure Test Report: The First Years on the Ground

**Status:** Living document — revise whenever evidence or experience contradicts it.
**Companions:** [CONSEQUENCES_OF_DEVIATION.md](CONSEQUENCES_OF_DEVIATION.md) (the precision-tier ledger this report feeds) · [pressure_test_report.md](pressure_test_report.md) (the whole-plan master audit) · [WHAT_IF_INDEX.md](WHAT_IF_INDEX.md)

> This report red-teams the **settling phase** — everything from the 72-hour arrival to a stable multi-year settlement: water, sanitation, food, soil, storage, health, shelter, defense, and the crafts (chemistry, ceramics, structure). It extends the master audit, which found the *journey* was the thinnest phase; the settling phase is the opposite — deeply covered, with excellent thresholds — so this audit is less about missing systems and more about **two subtler failure classes**: (1) genuine lethal gaps hidden inside strong coverage, and (2) the pervasive pattern that modules state *what breaks* but not *what it does to people*, so readers under-weight instructions whose consequences they cannot see. Both are now addressed; this report records where and how.

---

## 1. Method and Headline Findings

Each settling system was tested against: *What does it assume? What breaks the assumption — how likely, how lethal, how fast, and does it warn you? Does the manual answer it?* Closed gaps are marked **[CLOSED → module]**; remaining gaps **[OPEN]**.

**Three headline findings:**

*   **Finding A — The consequence gap (systemic).** The modules are rich in exact thresholds but routinely stop the failure-mode analysis at the *technical* failure ("soap won't trace," "vessel dissolves," "filter clogs") without tracing the *human cascade* ("no soap → fecal-oral disease → deaths"). Readers therefore cannot feel the weight of an instruction, and negotiate away the ones whose danger is invisible. **[CLOSED → [CONSEQUENCES_OF_DEVIATION.md](CONSEQUENCES_OF_DEVIATION.md)]** plus a MODULE_TEMPLATE change requiring every future failure mode to state its consequence and precision tier.
*   **Finding B — The precision-tier gap (systemic).** Nothing told readers which numbers are Law (exact, deviation kills) versus Craft (a range you calibrate by a test). This causes both fatal errors — rounding off a Law, and burning out chasing false precision on a Craft. **[CLOSED → the three-tier system in the ledger]**.
*   **Finding C — Silent-poison gaps (specific).** Inside strong water/food coverage sat three lethal blind spots united by a single treacherous property — *they defeat the senses and defeat boiling*: chemical water contaminants (nitrate, arsenic), grain/food toxins (ergot, aflatoxin, botulism-by-taste), and nutritional deficiency diseases. **[CLOSED → three new modules]**, detailed below.

---

## 2. Water & Drinking Safety

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 2.1 | Pathogen doctrine (filter + boil dual barrier, Schmutzdecke, setbacks) is excellent and threshold-rich. | — | **Adequate — strongest system in the manual.** |
| 2.2 | **The chemical blind spot.** Every water module targeted *living* contamination; nitrate, arsenic, and heavy metals — which boiling does not remove and, for arsenic, *concentrates* — were absent. A clear, sweet, pathogen-free spring can carry a fatal geological or nitrate load. Highest specific risk: infant **methemoglobinemia** ("blue baby") from nitrate, and chronic arsenic from suspect geology. | Critical | **[CLOSED → [Water Contaminant Testing & Remediation](Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/07_Water_Contaminant_Testing_and_Remediation.md)]** — source-signature assessment, the "boiling betrays you" teaching, rainwater as the chemical-safe infant fallback. |
| 2.3 | **The counterintuitive-fact risk.** "The water is treated therefore safe" is *actively harmful* for chemicals — people boil themselves a higher arsenic dose. This must be taught as a named exception, not left implicit. | High | **[CLOSED → new module §4; ledger §4]** — flagged as a Law-tier teaching for two keepers minimum. |
| 2.4 | Well/spring re-testing cadence (a source that was safe becoming unsafe: new uphill latrine, wet year) was not scheduled. | Medium | **[CLOSED → new module §5 re-test cadence]** |

## 3. Sanitation & Humanure

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 3.1 | Thresholds are outstanding and among the manual's best: 30 m setback (50 m sand), 55 °C × 15 days, 12-month cure, three-tier verification, Ascaris as the benchmark organism. | — | **Adequate — exemplary.** |
| 3.2 | **Consequence weighting.** The thresholds are stated as engineering, but the *human* result of missing them (an Ascaris outbreak returning through the salad weeks later, whole-settlement dysentery from a too-close latrine) was under-stated, and these are the most silent-onset failures in the manual. | High | **[CLOSED → ledger §5 with onset column; the "silent" flag]** |
| 3.3 | Animal-manure pathogens (E. coli O157, Crypto) and manure hot-composting standards get less treatment than humanure. | Medium | **[CLOSED → [Livestock module, Zoonotic Disease and Manure Safety](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/02_Livestock_and_Mechanical_Animals.md)]** — hot-compost to 55 °C, age before food-crop use, 30 m water setback. |
| 3.4 | Urine diversion (huge N/P recovery, and lower pathogen load) is mentioned but not built out. | Low (opportunity) | **[OPEN]** Value is nutrient-recovery, not safety. |

## 4. Food, Soil & Storage

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 4.1 | Preservation and pantry physics are threshold-rich and correct (pH 4.6, aw bands, Q10 rule, caloric-reserve arithmetic, seed viability). | — | **Adequate — strong.** |
| 4.2 | **Grain and food toxins that survive cooking.** Ergot (gangrene/convulsions/abortion), aflatoxin and storage molds (liver failure/cancer), and botulism-by-tasting were absent or scattered. They share the deadliest property in food safety: **they defeat both the senses and the cooking pot**, so the reasonable "waste not / cook it off" instinct kills. | Critical | **[CLOSED → [Food Toxins & Storage Safety](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/09_Food_Toxins_and_Storage_Safety.md)]** — the "can I fix this batch?" decision table; discard-batch discipline as law. |
| 4.3 | **Nitrate in greens and held food** (infant methemoglobinemia; nitrite from warm-held cooked vegetables). | High | **[CLOSED → new food-toxin module §6]** |
| 4.4 | First-crop failure (30–60% of plan, historically the norm) and the seasonal-arrival trap (autumn arrival without a larder = death) were flagged in the master audit; deserved one explicit place. | High | **[CLOSED → [First-Year Food Security & Arrival Timing](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/10_First_Year_Food_Security_and_Arrival_Timing.md)]** — the caloric-chain ledger, the 0.3–0.6 first-year yield discount, the arrival-window table by climate, and the overwinter-in-place default. |
| 4.5 | Crop disease/pest response (blight, rust, quarantine of infected seed) not covered. | Medium | **[CLOSED → [Crop Disease & Pest Response](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/11_Crop_Disease_and_Pest_Response.md)]** — diversity as master defense, roguing, the seed-line-outranks-harvest sacrifice decision. |

## 5. Health & the Body

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 5.1 | Acute care is superb and consequence-explicit already: sepsis 48-h escalation rule (~80% fatal untreated), golden-period wound closure, tourniquet, PPH 15–30 min, golden-minute newborn, dental abscess 10–14 days, CO poisoning 1–2 h. These modules are the *model* for how the rest should read. | — | **Adequate — the benchmark.** |
| 5.2 | **Deficiency diseases named but never elaborated.** Scurvy, pellagra, beriberi, rickets, B12, iodine were listed as "preventable" with no timeline, sign, or the specific technique (nixtamalization, whole grain, sprouting, animal-fat/B12) that prevents each. These are *knowledge diseases* that strike exactly the food-stressed new settlement, on a monotonous winter diet. | Critical | **[CLOSED → [Deficiency Diseases & Heat Illness](Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/10_Deficiency_Diseases_and_Heat_Illness.md)]** — timelines, early signs, the staple traps, the deficiency calendar. |
| 5.3 | **The B12 constraint on the vision's agrarian idealism.** A near-total plant diet depletes B12 over 1–3 years → irreversible neuropathy. The manual's aesthetic leaned plant-ward without stating this hard limit. | High | **[CLOSED → new module §3.5; stated as a planning constraint]** |
| 5.4 | **Heat illness** was only a one-line "dangerous above 40 °C." The life-defining transition (sweating fails, confusion begins → heat stroke → death in hours) and the work/rest/shade rule were missing. | High | **[CLOSED → new module §4]** |
| 5.5 | **Medical honesty ceiling.** Zero-tech medicine cannot save appendicitis, obstructed labor, sepsis, major trauma. The modules carry honest caveats; the settlement's real mitigations are prevention culture and *knowing the ceiling*. | High (unavoidable) | **Stated; consistent across modules.** |
| 5.6 | Zoonotic disease (brucellosis, Q fever, bovine TB) beyond the 14-day quarantine line is thin. | Medium | **[CLOSED → [Livestock module, Zoonotic Disease and Manure Safety](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/02_Livestock_and_Mechanical_Animals.md)]** — the endemic zoonoses, milk-heating rule, and barrier-care defenses. |
| 5.7 | Infant botulism (no honey under 12 months) was cross-referenced but not stated plainly at point of use. | Medium | **[CLOSED → stated in new modules; ledger §6]** |

## 6. Shelter, Fire & Structure

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 6.1 | Carbon-monoxide risk is explicitly and well covered (1–2 h, odorless, "never seal all ventilation with a fire burning"). Structural failure modes (green-timber splitting, foundation damp, mortar freeze, lime blindness) are consequence-explicit — another benchmark section. | — | **Adequate — strong.** |
| 6.2 | **House fire (as distinct from wildfire and CO)** — smoke inhalation, burn injury, thatch ignition from the indoor hearth, escape/egress. | Medium-High | **[CLOSED → [Fire Safety and the Hearth](Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/07_Fire_Safety_and_the_Hearth.md)]** — hearth containment, two-exit egress drilled in the dark, water/sand + the fat-fire exception, seed/reserve stored away from flame. |
| 6.3 | Winter freeze of water lines and stored water (dehydration risk, burst vessels) is not addressed in any defense/shelter module. | Medium | **[OPEN]** Logged. |
| 6.4 | Consequence weighting on structural Craft-vs-Law: thatch pitch, crown spacing, mortar-freeze are correctly exact, but readers weren't told these are *Law* while air-dry times are *Craft*. | Medium | **[CLOSED → ledger §9–10 tier tags]** |

## 7. Defense & the Social Perimeter

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 7.1 | Passive/active/animal defense is well-designed, and the over-militarization ("warrior-class trap") analysis is one of the manual's intellectual high points. | — | **Adequate — strong.** |
| 7.2 | **Human-consequence quantification.** Defense failure modes describe *breach* ("perimeter breached," "crop loss") but rarely the mortality cascade ("crops lost → X kcal short → winter famine → deaths begin [month], children first"). This blunts the reader's sense of stakes exactly where stakes are highest. | High | **[CLOSED → ledger §10 + this report; What-If entries trace the cascades]** |
| 7.3 | **Rotation is a Law, not a preference.** The single most important *social* Law-tier instruction — never let a permanent warrior class form — was argued powerfully but not labeled as the non-negotiable it is. | High | **[CLOSED → ledger §10 marks it Tier-L (social)]** |
| 7.4 | Early-warning failure (tripwire neglect → surprise → insufficient response time) lacks an explicit "you have X minutes" consequence. | Medium | **[OPEN — small]** Logged; conceptually covered by the interim-perimeter doctrine in the Arrival Protocol. |

## 8. The Crafts (Chemistry, Ceramics, Materials)

| # | Finding | Severity | Status |
|:--|:---|:---|:---|
| 8.1 | Immediate hazards are excellently consequence-explicit: lye → blindness, lye+aluminum → explosion, exploding bricks/vessels, quartz-inversion cracking. | — | **Adequate — model sections.** |
| 8.2 | **The craft-to-survival cascade** is weak: "soap won't trace," "vessel dissolves" stop at the product, not the downstream ("no soap → hygiene collapse → disease"; "no watertight vessel → contaminated water → outbreak"). A failed craft is a survival failure one or two steps later. | Medium-High | **[CLOSED → ledger §10 traces the cascades; template change requires it going forward]** |

## 9. The Two Systemic Fixes (what this revision changed everywhere)

1.  **The consequence ledger + precision tiers.** [CONSEQUENCES_OF_DEVIATION.md](CONSEQUENCES_OF_DEVIATION.md) collects every Law-tier settling instruction with its mechanism, its human consequence, and — the crucial column — its *onset and whether it warns you*. It teaches the three tiers (Law / Craft / Preference) so readers stop making the two fatal errors: rounding off a Law, and chasing false precision on a Craft.
2.  **The template change.** [MODULE_TEMPLATE.md](MODULE_TEMPLATE.md) §8.2 now *requires* every failure mode to state (a) the consequence traced to human impact and (b) the precision tier of the instruction it violates. This propagates the fix to all future modules instead of leaving it as a one-time audit.

## 10. Single Points of Failure (settling phase, consolidated)

1.  **Water discipline, weeks 1–4** — pathogens (boil/filter) *and* the newly-covered chemicals (test/relocate). The highest-probability lethal failure of the whole project.
2.  **The silent poisons** — botulism, aflatoxin, ergot, nitrate, CO, Ascaris: all defeat the senses, several defeat boiling. Prevention-only; the senses will not save you.
3.  **The monotonous winter diet** — scurvy and the staple traps; solved in autumn by planning diversity, not in February by wishing for it.
4.  **The first-winter food margin** — arrive at the growing-season start, discount the first harvest to 0.3–0.6, bank the reserve before the gap season. **[CLOSED → [First-Year Food Security & Arrival Timing](Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/10_First_Year_Food_Security_and_Arrival_Timing.md)]**
5.  **The lone skill-keeper of a *reason*** — these are knowledge failures: the settlement that forgets *why* it nixtamalizes maize or cures compost 12 months gets the disease back. The [dogma antidote](Outcome_5_Decadal_Resilience/11_The_Next_Generation/08_The_Scientific_Method.md) is the defense.
6.  **Internal conflict / militarization** — the social single-point-of-failure, now labeled Law-tier.

## 11. Open Ledger (settling phase, priority order)

Urine-diversion nutrient recovery (opportunity, not safety) · early-warning "minutes to respond" quantification. *(House-fire safety, first-year food-margin/arrival-window, crop disease/pest response, animal-manure composting, zoonotic disease, and winter water-freeze — all closed since first publication.)*

*A settling phase is where optimism meets biology. The manual's biology is strong; this revision's job was to make sure the reader *feels* the parts of it that kill silently — and knows which numbers to obey to the letter, and why. The rest is the oldest instruction in the manual: build the prototype, test it on your own ground, and write down what the ground teaches you.*

## Glossary Reference

*See [Glossary.md](Glossary.md) for full definitions of:*

*   **Pathogen**
*   **Schmutzdecke**

