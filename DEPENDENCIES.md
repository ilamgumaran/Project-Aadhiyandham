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
| 01 The Journey | None (entry point) | 02 The Site |
| 02 The Site | 01 The Journey | 03, 04, 07 (site selection informs all construction) |
| 03 Candidate Atlas | None (reference data) | 01, 02 (location evaluation criteria) |

### Outcome 2: Biological Sovereignty
| Section | Depends On | Provides To |
|---|---|---|
| 03 Water & Sanitation | 02 The Site (water source identification) | 04 Food (irrigation), 05 Health (clean water for medicine) |
| 04 Food & Soil | 02 The Site (soil analysis), 03 Water | 05 Health (nutrition), 06 Ecological (crop-ecosystem integration) |
| 05 Health & Body | 03 Water, 04 Food, 09 Chemistry (antiseptics) | 08 The Mind (physical health enables mental health) |
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
