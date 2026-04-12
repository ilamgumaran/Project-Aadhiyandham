# Non-Motorized Coastal Piloting

**Alignment:** Outcome 1 — Locating and Connecting Optimal Refugia

> **CAUTION**: Coastal waters contain hazards invisible from the surface — submerged rocks, shifting sandbars, tidal races. Always carry a lead line and sound ahead when entering unfamiliar waters. Never approach a lee shore in onshore wind conditions.

---

## Theoretical Foundation

Coastal piloting is the discipline of fixing position and navigating safely using only the geometry of visible landmarks, the curvature of the Earth, and the depth of the water beneath the keel. It requires no electronics, no magnetic compass (though one helps), and no charts (though charts multiply accuracy). Every technique below rests on elementary trigonometry and the physics of light traveling in straight lines through the lower atmosphere.

### The Transit (Range)

When two fixed objects on shore — a front mark and a rear mark — appear exactly aligned from the observer's perspective, the observer lies on a unique straight line (azimuth) connecting those two objects, extended seaward. This line is called a **transit** (British usage) or **range** (American usage). Its critical property: it requires no instrument at all; the human eye detects misalignment of two objects to approximately 0.01 degrees (about 0.5 metres lateral error at 3 km).

**The geometry of sensitivity.** Let the front mark be at distance d1 from the observer and the rear mark at distance d2 (where d2 > d1). If the observer moves laterally by a small displacement delta-x, the angular separation between the two marks changes by approximately:

```
delta-theta (radians) = delta-x * (1/d1 - 1/d2)
```

This sensitivity is maximized when d1 is small relative to d2 — that is, when the front mark is close and the rear mark is far. A front mark at 200 m and a rear mark at 2000 m gives ten times the sensitivity of two marks both at 2000 m. Practical consequence: always choose the closest identifiable object as your front mark.

**Universality.** Every maritime culture developed transit navigation independently. Polynesian navigators aligned reef passages with mountain peaks. Norse sailors aligned cairns on headlands. Tamil fishermen aligned temple towers with coconut palms. The transit is the most reliable position line available to any navigator, past or present.

### The Three-Point Fix (Cocked Hat)

Three transits or three compass bearings to known landmarks define three position lines. In theory they intersect at a single point. In practice, observation errors cause the three lines to form a small triangle — the **cocked hat**. The navigator's true position lies within or very near this triangle.

**Accuracy criteria:**
- The cocked hat should be less than 500 m on a side for acceptable coastal piloting.
- If larger, retake all bearings and replot.
- Angular separation between the three landmarks should be between 60 and 120 degrees for optimum geometric strength.
- Separations of 30 degrees or 150 degrees produce elongated, unreliable triangles.

**Error distribution.** If all three bearings have equal random error sigma, the area of the cocked hat scales as sigma-squared. Halving your observation error reduces the triangle area by a factor of four.

### Vertical Sextant Angle (VSA)

If the height of a landmark is known (a cliff, mountain, lighthouse), measuring the vertical angle between its peak and the waterline yields distance:

```
Distance = Height / tan(angle)
```

At small angles (less than 5 degrees), this simplifies to:

```
Distance (m) = Height (m) * 57.3 / angle (degrees)
```

**Worked example.** A mountain 500 m tall subtends a vertical angle of 2 degrees:

```
Distance = 500 / tan(2 deg) = 500 / 0.0349 = 14,326 m = 14.3 km
```

This measurement can be taken with a simple **protractor-and-plumb-bob sextant** — a protractor with a weighted string hanging from the center pivot, and a sighting tube or straw along the straight edge. Accuracy: plus or minus 0.25 degrees with care, yielding distance accuracy of roughly plus or minus 12 percent at small angles.

**VSA distance table for common angles and heights:**

| Landmark Height | 0.5 deg | 1.0 deg | 2.0 deg | 5.0 deg |
|:---------------:|:-------:|:-------:|:-------:|:-------:|
| 100 m           | 11.5 km | 5.7 km  | 2.9 km  | 1.1 km  |
| 250 m           | 28.6 km | 14.3 km | 7.2 km  | 2.9 km  |
| 500 m           | 57.3 km | 28.6 km | 14.3 km | 5.7 km  |
| 1000 m          | 114.6 km| 57.3 km | 28.6 km | 11.4 km |

*Note: At distances beyond about 20 km, atmospheric refraction and curvature corrections become significant.*

### Horizon Distance

The geometric distance to the horizon from an eye height h (in metres) above sea level is:

```
d (km) = 3.57 * sqrt(h)
```

**Practical values:**

| Platform                     | Eye Height (m) | Horizon Distance (km) |
|:-----------------------------|:--------------:|:---------------------:|
| Seated in canoe              | 0.7            | 3.0                   |
| Kneeling in canoe            | 1.0            | 3.6                   |
| Standing in small boat       | 2.0            | 5.0                   |
| Standing on deck of large boat| 4.0           | 7.1                   |
| Top of 10 m cliff            | 10.0           | 11.3                  |
| Top of 30 m bluff            | 30.0           | 19.6                  |

This distance governs when landmarks appear over or disappear below the horizon. A 500 m mountain becomes visible at roughly 80 km in clear air (its height contributes to the detection range: d = 3.57 * (sqrt(h_eye) + sqrt(h_landmark))). This is the outer limit of visual coastal piloting.

### Dead Reckoning on Water

Dead reckoning (DR) is the estimation of current position from the last known fix, projected forward by course steered plus speed multiplied by elapsed time.

**Speed estimation — the chip log method:**
1. Drop a chip of wood (or any floating debris) at the bow.
2. Count the seconds until it passes the stern.
3. Speed = vessel length / elapsed time.

Example: vessel length is 5 m, chip takes 2.5 seconds to travel stern-to-bow:

```
Speed = 5 m / 2.5 s = 2.0 m/s = 3.9 knots
```

**Current correction.** Current adds vectorially to vessel speed through the water. A 2-knot current at 90 degrees to your heading pushes you 1 nautical mile (1.85 km) sideways per hour. After 3 hours, you are 5.6 km off your intended track — enough to miss an island entirely.

**DR accuracy degrades with time.** A 10 percent speed estimation error and a 5-degree heading error compound to roughly 1 nautical mile of position uncertainty after 5 nautical miles of travel. Fix position whenever landmarks are visible.

### Historical Navigation Methods

**Polynesian stick charts (Marshall Islands).** Islanders constructed frameworks of bent palm-rib sticks tied together, encoding ocean swell patterns, wave refraction around islands, and relative island positions. Shells tied to the framework represented islands. These were mnemonic devices studied on land before voyages — not carried aboard. They encoded information about swell direction changes that indicated proximity to land beyond the horizon.

**Viking sun compass and sunstone.** Norse navigators used a wooden disc with gnomon to track the sun's azimuth, calibrated by the hyperbolic shadow curves for specific latitudes. The legendary "sunstone" was a calcite (Iceland spar) crystal that polarizes light — when held toward an overcast sky, the crystal reveals the sun's direction through the polarization pattern of scattered light, even when the sun itself is invisible.

**Arab kamal.** A rectangular wooden card (approximately 5 x 3 cm) attached to a knotted string. The navigator holds the string taut between teeth and card, with the card at arm's length, bottom edge on the horizon, top edge on Polaris. Each knot corresponds to the latitude of a known port. When the correct knot is between the teeth and Polaris sits on the top edge, the navigator is at that port's latitude. Accuracy: approximately plus or minus 1 degree of latitude (plus or minus 111 km) — sufficient for east-west ocean crossings.

---

## Core Principles

1. **The Transit is King.** Two aligned landmarks give the most accurate position line available to the coastal pilot — no instruments required, no calibration, no error from magnetic deviation. Whenever a natural transit exists, use it in preference to any compass bearing.

2. **Never Trust a Single Line.** One bearing or one transit defines a line, not a position. You could be anywhere along that line. Always cross a first line with a second (and ideally a third) to obtain a fix. A single line of position is useful only for confirming you have not drifted off a known track.

3. **The Danger Bearing.** Before entering an area with a known hazard (reef, rock, shoal), pre-calculate a critical bearing to a visible landmark. While underway, monitor that bearing. If it crosses the pre-calculated threshold, you have entered the danger zone. This is a defensive technique — it tells you when to turn away, not where you are.

4. **The Running Fix.** When only one landmark is visible, take a bearing, sail a known distance on a known course, then take a second bearing to the same landmark. The two bearing lines, with the first one advanced by the distance and course made good, intersect to give a fix. Accuracy depends on the accuracy of your dead reckoning between the two bearings.

5. **Pilotage is Continuous.** Fix your position every 15 to 30 minutes in coastal waters. A 2-knot current moves you 1 km in 15 minutes. Complacency kills. Between fixes, maintain a dead reckoning plot. If you cannot fix your position for more than 30 minutes, slow down or stop until you can.

---

## Practical Implementation

### Building a Kamal (Star Altitude Measurer)

**Materials:** A rectangular piece of flat wood, bone, or stiff card (approximately 3 cm wide by 5 cm tall), a length of cord (approximately 50 cm), and access to a night sky with Polaris visible.

**Construction (30 minutes):**
1. Drill or punch a small hole in the exact center of the card's bottom edge.
2. Thread the cord through the hole and knot it on the far side.
3. To calibrate: on a night when you know your latitude, hold the card at arm's length with the cord taut between your front teeth and the card. Adjust until the bottom edge rests on the horizon and the top edge touches Polaris.
4. Tie a knot in the cord at the point where it exits your teeth. Label this knot with your current latitude.
5. Travel to a location one degree of latitude away (111 km north or south) and repeat, tying another knot.
6. Interpolate additional knots at equal spacing.

**Use at sea:** Hold the string taut between teeth and card. Slide the string until Polaris sits on the top edge and the horizon on the bottom edge. Read the knot position. Accuracy: plus or minus 0.5 degrees of latitude with practice (plus or minus 56 km).

### Building a Pelorus (Bearing Circle)

**Materials:** A flat board (approximately 30 cm diameter), a nail or dowel for the pivot, a straight sighting bar (30 cm long with small sight-holes or notches at each end), protractor or compass rose template.

**Construction:**
1. Draw or transfer a compass rose (0 to 360 degrees) onto the board, with 0 degrees at the top.
2. Drive the pivot nail through the exact center.
3. Mount the sighting bar on the pivot so it rotates freely.
4. Mount the board on the vessel's centerline with the 0-degree mark pointing precisely forward along the keel.

**Use:** Sight along the bar toward a landmark. Read the angle on the compass rose where the bar crosses it. This gives a relative bearing (angle from the bow). If you know the vessel's heading (from a compass or from a known course), convert to a true bearing: True Bearing = Heading + Relative Bearing.

**Accuracy:** Plus or minus 2 degrees with careful use. Sufficient for coastal piloting when combined with transits.

### The Sighting Triangle Procedure

Step-by-step procedure for taking a three-point fix:

1. **Select landmarks.** Identify three charted landmarks at angular separations of 60 to 120 degrees from each other.
2. **Take the middle bearing first.** The landmark closest to the beam (roughly perpendicular to your course) changes bearing most slowly — take it first as the reference.
3. **Take the most-abeam bearing second.** The landmark directly abeam changes bearing fastest with forward motion — take it next to minimize time lag.
4. **Take the third bearing.** Complete the triangle.
5. **Plot on chart.** Draw each bearing line from the landmark. The three lines should form a small triangle (the cocked hat).
6. **Evaluate.** If the cocked hat is less than 500 m on a side, your position is within it — take the center as your fix. If larger than 500 m, discard and retake all three bearings.
7. **Record.** Log the time, bearings, and plotted position. This becomes your new DR starting point.

**Time budget.** The entire procedure — sight, plot, evaluate — should take no more than 5 minutes. If it takes longer, vessel motion degrades accuracy.

### Danger Bearing — Worked Example

Consider the following situation:

```
                        N
                        |
        LIGHTHOUSE (L)  |
             *          |
            / \         |
           /   \        |
          /     \       |
    REEF /  045  \      |
   ~~~~~~/~~~~~~~~\~~~~~|~~~~~~~  (Reef line)
        /    SAFE  \    |
       /   WATER    \   |
      /              \  |
     /                \ |
    V                  \|
  VESSEL (heading NE)   
```

**Procedure:**
1. From the chart, identify the reef boundary and the lighthouse position.
2. Draw a line from the lighthouse tangent to the reef edge. Measure this bearing: 045 degrees True.
3. This is the **danger bearing**: 045 degrees.
4. **Rule:** While underway, continuously observe the lighthouse bearing. If the lighthouse bears **less than 045 degrees** (i.e., more northward), you are **inside the reef line** — danger. If it bears **greater than 045 degrees**, you are in safe water.
5. If the bearing approaches 045 degrees, alter course to seaward immediately.

### The Lead Line (Depth Sounding)

A weight (1 to 3 kg of lead, stone, or iron) attached to a line marked at regular intervals. The oldest and most reliable navigation instrument in existence.

**Traditional marks (Royal Navy system):**

| Depth (fathoms) | Depth (metres) | Mark                            |
|:---------------:|:--------------:|:--------------------------------|
| 2               | 3.7            | Leather with 2 strips           |
| 3               | 5.5            | Leather with 3 strips           |
| 5               | 9.1            | White cloth                     |
| 7               | 12.8           | Red cloth                       |
| 10              | 18.3           | Leather with hole               |
| 13              | 23.8           | Blue cloth                      |
| 15              | 27.4           | White cloth                     |
| 17              | 31.1           | Red cloth                       |
| 20              | 36.6           | Cord with 2 knots               |

**The arming.** Press tallow (animal fat), beeswax, or sticky clay into a hollow in the bottom of the lead weight. When it strikes the seabed, it picks up a sample: sand, mud, shell fragments, gravel, or rock. This **bottom sample** is compared with known bottom characteristics for the area:

- Sticky grey mud = river estuary or sheltered bay.
- Coarse sand with shell = shallow bank, possibly near reef.
- Fine sand = open coast, moderate depth.
- Rock chips or no sample = hard bottom, possibly reef.

**Depth plus bottom type combined give a surprisingly reliable position estimate**, especially when visibility is poor. A sequence of soundings (e.g., "12 metres, mud... 8 metres, sand... 5 metres, shell") traces a profile that can be matched to a known approach channel.

### Night Piloting

When darkness eliminates most visual landmarks, piloting shifts to three methods:

**1. Silhouette bearings.** Known hills and peaks remain visible as dark shapes against the star field. Identify which stars will pass behind which peaks at specific times (this can be predicted from star charts and almanacs). A star disappearing behind a peak's edge gives a precise bearing to that peak.

**2. The lead line.** Becomes the primary navigation tool at night. Take continuous soundings. A consistent depth profile (e.g., following the 10-metre contour) can guide you along a coast even in total darkness.

**3. Sound and smell.** Breaking waves on a reef are audible at 1 to 2 km. Surf on a beach carries further downwind. The smell of vegetation, woodsmoke, or tidal mudflats indicates proximity to land. These are not precise, but they are life-saving early warnings.

**Night piloting rule:** Never approach an unfamiliar coast at night. Heave to or anchor offshore until dawn provides visual references.

---

## Common Failure Modes

1. **Misidentified Landmarks.** Two similar hills, two similar headlands, two church towers — confusion is easy and the resulting fix is entirely wrong. Mitigation: always use transit pairs (two landmarks in alignment), not single marks. A misidentified single mark gives a wrong line; a misidentified transit pair is much harder to mistake because the relative geometry must match.

2. **Current Set Ignored.** The vessel drifts off course between fixes, and the navigator assumes the DR track is accurate. A 1.5-knot current (common in tidal waters) displaces the vessel 2.8 km per hour. Mitigation: always estimate current from tidal data, observed drift of flotsam, or the difference between successive fixes and DR positions. Apply the correction vector to all DR projections.

3. **Fog and Low Visibility.** All visual piloting fails simultaneously. The navigator has no bearings, no transits, no VSA, no horizon. Mitigation: fall back immediately to depth sounding (the lead line) and dead reckoning. Reduce speed. Sound fog signals. If depth soundings do not match expectations, anchor and wait.

4. **Refraction Error.** Atmospheric heating (especially afternoon sun on water) bends light rays, distorting the apparent position of landmarks and the horizon. Landmarks may appear elevated, depressed, or laterally shifted. Mirage effects can make distant objects appear closer or create phantom images. Mitigation: take critical bearings in early morning or evening when the air column is most stable. Apply a refraction correction of approximately 8 percent to horizon-distance calculations in hot conditions.

5. **Parallax of Near Objects.** A landmark very close to the vessel (under 500 m) shifts its apparent bearing rapidly with small changes in vessel position. The navigator takes a bearing, the vessel drifts 20 m, and the bearing has changed by several degrees. Mitigation: use distant rear marks for transits (the angular shift decreases with distance). For pelorus bearings, always prefer landmarks at greater than 1 km range.

---

## Vocabulary of the Foundation

- **Transit (Range):** The alignment of two fixed objects as observed from a vessel, defining a line of position. No instruments required. The most accurate position line available to the visual navigator.

- **Cocked Hat:** The small triangle formed by three lines of position that fail to intersect at a single point due to observation error. The navigator's true position is within or very near this triangle. Size indicates fix quality.

- **Vertical Sextant Angle (VSA):** The measured angle between the peak of a landmark of known height and the waterline, used to calculate distance to the landmark via trigonometry.

- **Dead Reckoning (DR):** The estimation of current position by advancing a known previous position using course steered, speed through the water, and elapsed time. Does not account for current unless explicitly corrected.

- **Danger Bearing:** A pre-calculated bearing to a visible landmark that defines the boundary of a hazard zone. If the observed bearing crosses the danger bearing, the vessel has entered unsafe water.

- **Running Fix:** A position fix obtained from two bearings to the same landmark taken at different times, with the first bearing advanced along the course and distance made good between observations.

- **Kamal:** A traditional Arab navigation instrument consisting of a calibrated card on a knotted string, used to measure the altitude of Polaris (or other stars) for latitude determination.

- **Pelorus:** A sighting device consisting of a compass rose and pivoting sight bar, mounted on the vessel's centerline, used to measure relative bearings to landmarks.

- **Lead Line:** A weighted, marked line used for measuring water depth (sounding) and sampling bottom sediment. The oldest navigation instrument still in use.

- **Fathom:** A unit of depth equal to 6 feet (1.83 metres). Originally defined as the span of a man's outstretched arms — the natural unit for hauling line hand-over-hand.

- **Set and Drift:** Set is the direction toward which a current flows. Drift is the speed of the current. Together they define the current vector that must be applied to dead reckoning calculations.

- **Bearing:** The horizontal angle between a reference direction (true north, magnetic north, or the vessel's heading) and the direction to an observed object, measured clockwise from 000 to 360 degrees.

---

## Cross-References

- [01_Rationale_and_Importance.md](01_Rationale_and_Importance.md) — Why maritime sovereignty matters for post-infrastructure communities.
- [03_Riverine_Logic.md](03_Riverine_Logic.md) — Inland waterway navigation: current reading, river piloting, and portage route selection.
- [../04_Terrestrial_Navigation/02_Map_and_Compass_Guide.md](../04_Terrestrial_Navigation/02_Map_and_Compass_Guide.md) — Compass bearing techniques applicable to pelorus use and shore-based triangulation.
- [../04_Terrestrial_Navigation/03_Celestial_Navigation_Sun.md](../04_Terrestrial_Navigation/03_Celestial_Navigation_Sun.md) — Solar and stellar positioning methods that extend piloting range beyond coastal waters.
- [../02_Orienting_and_Positioning.md](../02_Orienting_and_Positioning.md) — Triangulation fundamentals: the geometric principles underlying all position fixing.

---

## Further Study

- **Lewis, David.** *We, the Navigators: The Ancient Art of Landfinding in the Pacific.* University of Hawaii Press, 1972. The definitive study of Polynesian non-instrument navigation, based on voyages with traditional navigators.
- **Cotter, Charles H.** *A History of Nautical Astronomy.* Hollis & Carter, 1968. Comprehensive treatment of the development of celestial and coastal navigation from antiquity through the twentieth century.
- **Bowditch, Nathaniel.** *The American Practical Navigator.* Originally published 1802; continuously updated and still in print (U.S. Government publication). The standard reference for all aspects of marine navigation, including piloting, celestial navigation, and dead reckoning.
- **Crowley, Tony.** *The Barefoot Navigator: Wayfinding with the Skills of the Ancients.* Adlard Coles Nautical, 2006. Practical guide to navigation without modern instruments, with emphasis on techniques accessible to the amateur.
- **Gatty, Harold.** *Nature Is Your Guide: How to Find Your Way on Land and Sea by Observing Nature.* E.P. Dutton, 1958. Natural navigation using wind, waves, clouds, birds, and ocean swells — the environmental cues that complement visual piloting.

---

## Glossary Reference

*See [../../../Glossary.md](../../../Glossary.md) for full definitions of all technical terms used in this module.*
