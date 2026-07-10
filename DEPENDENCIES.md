# Cross-Module Dependency Map

This document maps the dependencies between sections, showing which modules must be completed (or understood) before others can be effectively implemented. Use this to plan the implementation sequence for a new refugia.

---

## Critical Path: Arrival to Stability

The minimum viable sequence for a newly arrived community:

```text
01 The Journey ──► 02 The Site ──► 03 Water & Sanitation ──► 04 Food & Soil
                                          │                        │
                                          ▼                        ▼
                                   07 Passive Defense        06 Ecological Harmony
                                          │                        │
                                          ▼                        ▼
                                   05 Health & Body ────────► 08 The Mind
                                                                   │
                                                                   ▼
                                                         09 The Mechanics
                                                               │
                                                    ┌──────────┼──────────┐
                                                    ▼          ▼          ▼
                                              10 Society  12 Archive  13 Horizon
                                                    │          │
                                                    ▼          ▼
                                              11 Next Gen  14 Cultural Tech
```

---

## Section-Level Dependencies

### Outcome 1: Locating Refugia
| Section | Depends On | Provides To |
|---|---|---|
| 01/00 Before Departure (Phase Zero) | None (the true entry point) | 01 The Journey (a ready group), 04 Food (departure↔arrival-timing), 08a Group Dynamics |
| 01/00.05 Physical Conditioning | 01/12 Party Playbooks (rehearsal walk, capacity) | 01 The Journey (bodies that meet the plan), settlement labor |
| 01 The Journey | 01/00 Before Departure (group, skills, decision) | 02 The Site |
| 01/12 Journey Scenarios & Contingencies | 01 Journey (transit, packing, family protocols) | 02 The Site (arrival handoff), 07 Passive Defense (interim perimeter), 07a Active Threat (encounter de-escalation) |
| 02 The Site | 01 The Journey | 03, 04, 07 (site selection informs all construction) |
| 02/08 Location Recording | 02 The Site (sentinels, terrain) | 01 Journey (route encoding), 14a Diplomacy (inter-settlement sharing) |
| 02/09 Geological Stability | 02 The Site (topography), 06 Field Mineralogy | 07 Initial Layout (safe building zones), 09 Mechanics (mineral sourcing) |
| 02/10 Climate Thresholds | 09 Micro-Climate Forecasting, 05 Hydrology | 04 Food (crop selection), 03 Water (drought planning) |
| 02/11 Soil & Water Baselines | 06 Field Mineralogy, 05 Hydrology | 04 Food (nutrient management), 03 Water (filtration design) |
| 03 Candidate Atlas | All of 02 The Site (evaluation framework) | 01, 02 (location evaluation criteria) |

### Outcome 2: Biological Sovereignty
| Section | Depends On | Provides To |
|---|---|---|
| 03 Water & Sanitation | 02 The Site (water source identification) | 04 Food (irrigation), 05 Health (clean water for medicine) |
| 03/07 Water Contaminant Testing | 02 Field Mineralogy & Water Baselines (geology), 03 Immediate Sanitation (setbacks) | 04 Food (safe irrigation/infant food), 05 Health (methemoglobinemia prevention) |
| 03/08 Urine Diversion & Nutrient Recovery | 03/04 Humanure Composting, 03/05 Humanure Integration | 04/02 Terra Preta (biochar charging), soil fertility |
| 04 Food & Soil | 02 The Site (soil analysis), 03 Water | 05 Health (nutrition), 06 Ecological (crop-ecosystem integration) |
| 04/09 Food Toxins & Storage Safety | 04 Long-Term Preservation, 08 Pantry Physics | 05 Health (poisoning prevention), 05/10 Deficiency Diseases |
| 04/10 First-Year Food Security & Arrival Timing | 06 Emergency Nutrition, 08 Pantry Physics, 02/10 Climate Thresholds | 01/12 Arrival Protocol (arrival-window & Phase-0 planting), 01 Journey (departure timing) |
| 04/11 Crop Disease & Pest Response | 03 Heirloom Seed (diversity/clean reserve), 02 Terra Preta, 06 Ecological Harmony | 04/10 First-Year Food Security (bridges on crop loss), 04/09 Food Toxins (field→storage toxins) |
| 04/12 Salt Production & Sourcing | 02 Site (coast/brine/rock geology) | 04/04 Long-Term Preservation (cure/ferment ratios), 06/02 Livestock (salt licks), 01/05 Trade (salt as commodity) |
| 06/08 Fishing & Aquaculture | 06/01 Ecological Harmony, 04/06 Emergency Nutrition | 04/04 Preservation (dried/salted fish), 04/02 Terra Preta (pond-water fertility) |
| 06/09 Small Livestock (Poultry & Rabbits) | 06/02 Livestock, 04/06 Emergency Nutrition (fat imperative) | 04/02 Terra Preta (manure), 09/05 Textiles (fur/pelts), 07 Defense (fowl alarms) |
| 06/10 Beekeeping | 06/01 Ecological Harmony, 05/03 Antibiotic Kit (medicinal honey) | 04 crops (pollination yield), 09/07 Chemistry (wax) |
| 06/07 Fire Safety and the Hearth | 06/04 Shelter (CO/ventilation), 04/05 Thermal Mass Cooking | 07 Wildfire Defensible Space (shared ember/spacing logic) |
| 05 Health & Body | 03 Water, 04 Food, 09 Chemistry (antiseptics) | 08 The Mind (physical health enables mental health) |
| 05/10 Deficiency Diseases & Heat Illness | 04 Food (dietary diversity), 09 Chemistry (ash-lye for nixtamalization) | 11 Next Gen (child development depends on nutrition) |
| 05/11 Epidemic & Quarantine Protocol | 03 Sanitation, 08 Natural Burial, 09 Chemistry (soap) | 14a First Contact, 08a Integration of Newcomers (both governed under epidemic) |
| 05/12 Hygiene, Laundry & Parasite Control | 09 Chemistry (soap), 03 Sanitation | 05/11 Epidemic (prevents the outbreaks); vector/rodent control |
| 09/10 Lighting (Lamps & Candles) | 09/07 Chemistry (tallow/fat), 06/10 Beekeeping (wax) | 05/09 Circadian Health (dim warm night light), extended useful day |
| 06 Ecological Harmony | 02 The Site, 04 Food & Soil | 07 Passive Defense (landscape design), 04 Food (silvopasture feedback) |

### Outcome 3: Perimeter Defense
| Section | Depends On | Provides To |
|---|---|---|
| 07 Passive Defense | 02 The Site (topography), 06 Ecology (defensive planting) | 08 The Mind (security enables psychological safety) |
| 07a Active Threat Response | 07 Passive Defense | Community security |
| 07b Animal Coexistence | 06 Ecological Harmony, 07 Passive Defense | 04 Food (crop protection) |

### Outcome 4: Psychological Centeredness
| Section | Depends On | Provides To |
|---|---|---|
| 08 The Mind | 03 Water, 04 Food, 05 Health, 07 Defense (basic needs met) | 10 Society (healthy individuals form healthy governance) |
| 08/06 Raja Yoga (Inner Laboratory) | 08 The Mind (Centered Null baseline), 11/08 Scientific Method (epistemics) | 14 Cultural Tech (the solitary channel beside ritual/play) |
| 08a Group Dynamics | 08 The Mind, 10 The Society | Community resilience |
| 08b Childhood Development | 08 The Mind | 11 The Next Generation (psychological readiness for learning) |

### Outcome 5: Decadal Resilience
| Section | Depends On | Provides To |
|---|---|---|
| 09 The Mechanics | 02 The Site (water power), 03 Water (hydrams) | 04 Food (milling), 05 Health (surgical tools), 13 Horizon |
| 10 The Society | 08 The Mind, 09 Mechanics (shared labor models) | 11 Next Gen (governance context for curriculum) |
| 11 The Next Generation | 08 The Mind, 08b Childhood Dev, 10 Society, 12 Archive | 13 Horizon (trained minds for advanced tech) |
| 12 The Archive | 09 Mechanics (papermaking tools), 07 Chemistry (ink) | 11 Next Gen (knowledge substrate), 14b Knowledge Exchange |
| 13 The Horizon | 09 Mechanics (furnaces), 11 Next Gen (scientific literacy) | Long-term technological advancement |

### Outcome 6: Flourishing Civilization
| Section | Depends On | Provides To |
|---|---|---|
| 14 Cultural Technology | 08 The Mind, 10 The Society | Community identity, multi-generational morale |
| 14a Inter-Settlement Diplomacy | 01 The Journey (routes), 14 Cultural Tech | 14b Knowledge Exchange |
| 14b Knowledge Exchange | 12 The Archive, 14a Diplomacy | Cross-community innovation |

---

## Shared Material Dependencies

These materials are required by multiple sections. Sourcing them is a cross-cutting concern:

| Material | Produced By | Required By |
|---|---|---|
| **Charcoal / Biochar** | 04 Food (pyrolysis) | 03 Water (filtration), 09 Mechanics (smelting), 07 Chemistry (soap) |
| **Clay** | 02 The Site (field mineralogy) | 09 Mechanics (furnaces), 09 Ceramics (pottery), 06 Structural (brick) |
| **Lime** | 09 Mechanics (kiln) | 06 Structural Engineering (mortar), 03 Water (pH adjustment) |
| **Cordage / Rope** | 09 Cordage module | 05 Health (traction splints), 06 Structural (timber framing), 09 Textiles (looms) |
| **Iron / Steel** | 09 Mechanics (bloomery) | 04 Food (tools), 05 Health (surgical), 13 Horizon (advanced tech) |
| **Soap / Lye** | 09 Chemistry (potash) | 05 Health (surgical hygiene), 05 Textiles (fiber processing) |
| **Paper / Ink** | 12 The Archive | 11 Next Gen (curriculum), 14b Knowledge Exchange |

---

## Implementation Phases

### Phase 1: First 100 Days (Sections 01-04, 07)
Arrival, site selection, water security, food establishment, basic perimeter.

### Phase 2: Stabilization (Sections 05, 06, 08)
Health systems, ecological integration, psychological grounding.

### Phase 3: The Recycling Cliff (Sections 09, 10, 12)
Material synthesis before scavenged resources degrade. Governance formalization. Knowledge archiving.

### Phase 4: Generational Transfer (Sections 11, 13, 14)
Education, advanced technologies, cultural identity, inter-settlement networking.

## Glossary Reference

*See [Glossary.md](Glossary.md) for full definitions of:*

*   **Biochar**
*   **Bloomery**
*   **Centered Null**
*   **Pyrolysis**
*   **Recycling Cliff**
*   **Refugia**
*   **Silvopasture**

