# Direction: Which Way?

**Alignment:** Outcome 1: Locating and Connecting Optimal Refugia
# திசை: எந்த வழி?

> **SAFE**: Direction-finding using sun and stars is inherently safe. The primary risk is acting on an inaccurate reading — always cross-check solar direction against at least one terrain feature before committing to a route.

Once you know where you are (Positioning), you must decide which way to go. This is called **Navigation**. Direction is the most fundamental element of navigation — more fundamental than distance, more fundamental than speed. If you know which way to walk, you will eventually arrive. If you walk fast in the wrong direction, you are simply lost more efficiently.

நீங்கள் எங்கே இருக்கிறீர்கள் (நிலைப்படுத்துதல்) என்று தெரிந்தவுடன், நீங்கள் எந்தப் பக்கம் செல்ல வேண்டும் என்பதைத் தீர்மானிக்க வேண்டும். இது **வழிசெலுத்தல்** (Navigation) எனப்படும். திசை என்பது வழிசெலுத்தலின் மிக அடிப்படையான கூறு — தூரத்தை விட அடிப்படையானது, வேகத்தை விட அடிப்படையானது.

This module teaches you to determine direction using nothing but the sky — the sun by day, the stars by night, and the moon when neither is clearly available. These methods predate the magnetic compass by millennia and will remain functional long after the last GPS satellite deorbits.

---

## Theoretical Foundation

### Earth's Axial Tilt and the Changing Sun Path

The Earth's rotational axis is not perpendicular to its orbital plane around the sun. It is tilted at approximately **23.44 degrees** from vertical. This tilt is the reason seasons exist, and it is also the reason the sun does not rise in exactly the same place every day.

At the **equinoxes** (approximately March 20 and September 22), the sun rises due East and sets due West at every location on Earth, regardless of latitude. On these two days, the sun's path across the sky is symmetrical about the cardinal East-West line.

At the **summer solstice** (approximately June 21 in the Northern Hemisphere), the sun rises and sets approximately 23.44 degrees *north* of the due-East/due-West line. At the **winter solstice** (approximately December 21), it rises and sets approximately 23.44 degrees *south* of due East/West. The exact offset depends on your latitude — at higher latitudes the angular displacement at the horizon is even larger than 23.44 degrees due to the geometry of the celestial sphere projected onto a flat horizon.

**Practical consequence:** If you use sunrise position alone to determine East, you could be off by more than 23 degrees depending on the date. This is a significant error — over a 10 km walk, a 23-degree error puts you nearly 4 km off course.

```text
        Sun Path Arc: Equinox vs. Solstices (Northern Hemisphere)
                        SOUTH SKY
                     (observer faces S)

                        * NOON *
                      / Jun sol \        <- highest arc (summer)
                    /   ........  \
                  /  ../  NOON  \.. \
                / ../    * * *    \.. \
              /  /  /  Equinox arc  \  \  \
            / ../  / ...............  \  \.. \
     NE   / ../  / ../   NOON    \..  \  \.. \   NW
   rise  / ../  / ../    * * *    \..  \  \.. \  set
  ------/--/---/--/--- Dec sol ----\--\---\--\------
  E    /  /   /  /     (lowest)     \  \   \  \   W
 HORIZON LINE ====================================
       ^  ^   ^                         ^  ^   ^
      Jun Eq Dec                      Dec Eq  Jun
     rise rise rise                  set  set  set
```

### Solar Declination

Solar declination is the angle between the sun's rays and the plane of the Earth's equator. It varies continuously throughout the year:

- At the March equinox: declination = 0 degrees
- At the June solstice: declination = +23.44 degrees (sun is north of the equator)
- At the September equinox: declination = 0 degrees
- At the December solstice: declination = -23.44 degrees (sun is south of the equator)

Solar declination directly determines two things you can observe: (1) where on the horizon the sun rises and sets, and (2) the direction your shadow points at solar noon. When declination is zero, your noon shadow points exactly toward the nearest pole. When declination is nonzero, the shadow still points very close to True North/South at noon, but the sun's rising and setting positions shift along the horizon.

### True North vs. Magnetic North

A magnetic compass does not point to the Geographic North Pole (True North). It points toward the Magnetic North Pole, which is a wandering point currently located in the Canadian Arctic archipelago, roughly 500 km from the geographic pole. The angular difference between True North and Magnetic North at any given location is called **magnetic declination** (not to be confused with solar declination).

Magnetic declination varies dramatically by location:

- **Eastern United States:** approximately 10 to 15 degrees West (the compass needle points west of True North)
- **Western United States:** approximately 10 to 15 degrees East
- **Western Australia:** approximately 2 to 5 degrees East
- **Parts of Siberia and northern Canada:** 20 degrees or more

If you are using a compass and a map together, you must correct for declination or your position fixes will accumulate error. If you have no compass and are using celestial methods described in this module, magnetic declination is irrelevant — the sun and stars indicate True North directly.

**Aadhiyandham principle:** Celestial navigation gives True North. Compass navigation gives Magnetic North. Know which one you are using and never mix them without correction.

### Why the Shadow-Stick Method Works

The Earth rotates 360 degrees in approximately 24 hours, which means the sun appears to move across the sky at a rate of **15 degrees per hour** (360 / 24 = 15). This motion is from East to West. A shadow cast by a vertical stick is the projection of the sun's position onto the ground. As the sun moves from East to West, the shadow tip traces a curved path on the ground from West to East.

At **solar noon** — the moment when the sun reaches its highest point in the sky (zenith transit) — the shadow is at its shortest and points directly toward the nearest geographic pole: True North in the Northern Hemisphere, True South in the Southern Hemisphere.

By marking two shadow-tip positions separated by 15 to 20 minutes, you capture a segment of the shadow's East-West arc. A line drawn between these two marks is an approximate East-West line. The geometry is most accurate near solar noon and at mid-latitudes (30 to 55 degrees), where the sun's arc is well-defined and shadows are neither too long nor too short.

### Stars as Direction Indicators

At night, the stars provide directional information that is in some ways more reliable than the sun, because stellar positions do not shift with the seasons (on human timescales).

**Polaris (the North Star):** Polaris sits within **0.7 degrees** of the True North celestial pole. This means that to a ground observer, Polaris appears virtually stationary while all other stars rotate around it. If you can find Polaris, you have found True North to within one degree — better accuracy than most magnetic compasses in the field.

**The Southern Cross (Crux):** In the Southern Hemisphere, there is no bright star directly at the South Celestial Pole. Instead, navigators use the constellation Crux (the Southern Cross) as a pointer. By extending the long axis of the cross approximately 4.5 times its own length, you arrive at the approximate position of the South Celestial Pole on the sky. Drop a vertical line from that point to the horizon, and that is due South.

**Orion's Belt:** The three stars of Orion's Belt rise due East and set due West, accurate to within approximately 3 degrees, at any latitude where Orion is visible. This makes Orion's Belt one of the most universally useful directional markers in the night sky.

---

## Core Principles

The following five principles form the foundation of all celestial direction-finding. Memorize them.

### Principle 1: The Solar Arc

The sun traverses approximately **15 degrees per hour** across the sky, moving from East to West. This rate is constant regardless of season, latitude, or weather. Even when you cannot see the sun, it is still moving at 15 degrees per hour, and any brief clearing in the clouds gives you a usable data point.

### Principle 2: The Shadow-Length Rule

A shadow cast by a vertical object is **shortest at solar noon**, and at that moment points directly toward **True North** (Northern Hemisphere) or **True South** (Southern Hemisphere). The shortest-shadow moment is the single most reliable daytime directional fix available without instruments.

### Principle 3: The Seasonal Correction

The sun's rising and setting positions shift by up to **plus or minus 23.44 degrees** from due East/West over the course of a year, driven by Earth's axial tilt. A direction estimate based solely on sunrise or sunset must account for the date. At the equinoxes, sunrise/sunset positions are exactly East/West. At the solstices, the offset is at its maximum.

### Principle 4: The Hemisphere Rule

Shadow behavior **reverses** across the equator. In the Northern Hemisphere, the noon shadow points North and the sun is in the southern sky. In the Southern Hemisphere, the noon shadow points South and the sun is in the northern sky. In the tropics (between 23.44 degrees N and 23.44 degrees S), the sun can be directly overhead on certain dates, producing no shadow at all at noon — this is a known failure mode of shadow-based methods.

### Principle 5: The Stellar Constant

Polaris maintains its position within **0.7 degrees** of the True North celestial pole. Unlike the sun, Polaris does not shift with the seasons. Unlike a compass, it is not affected by magnetic anomalies, nearby metal, or electromagnetic interference. On a clear night in the Northern Hemisphere, Polaris is the most accurate directional reference available to an unaided observer.

---

## The Four Cardinal Points / நான்கு முக்கிய திசைகள்

Every path on Earth is defined by these four points:

பூமியிலுள்ள ஒவ்வொரு பாதையும் இந்த நான்கு புள்ளிகளால் வரையறுக்கப்படுகிறது:

1. **North (வடக்கு):** The direction of the North Pole. 0 degrees (or 360 degrees) on a compass rose.
2. **South (தெற்கு):** The direction of the South Pole. 180 degrees on a compass rose.
3. **East (கிழக்கு):** Where the sun rises at the equinoxes. 90 degrees. (சூரியன் உதிக்கும் திசை.)
4. **West (மேற்கு):** Where the sun sets at the equinoxes. 270 degrees. (சூரியன் மறையும் திசை.)

Between these four cardinal directions lie the **intercardinal directions**: Northeast (45 degrees), Southeast (135 degrees), Southwest (225 degrees), and Northwest (315 degrees). For field navigation without instruments, the four cardinal directions are sufficient. Intercardinal precision requires a compass or careful celestial measurement.

```text
              [ NORTH / வடக்கு ]
              0° / 360°
                  ^
                  |
 [ WEST ] <-------+-------> [ EAST ]
 270°             |          90°
 மேற்கு           |          கிழக்கு
                  v
              [ SOUTH / தெற்கு ]
              180°
```

---

## Daytime Orientation: The Sun

### Quick Method: Sunrise/Sunset Check / சூரிய உதயம்/மறைவு சரிபார்ப்பு

1. Face the rising sun. You are facing approximately **East**.
   உதிக்கும் சூரியனை நோக்கி நில்லுங்கள். நீங்கள் தோராயமாக **கிழக்கை** நோக்கி இருக்கிறீர்கள்.
2. Your back is to the **West**. (உங்கள் முதுகு **மேற்கு** நோக்கி இருக்கும்.)
3. Your left hand points **North**. (உங்கள் இடது கை **வடக்கைக்** காட்டும்.)
4. Your right hand points **South**. (உங்கள் வலது கை **தெற்கைக்** காட்டும்.)

**Accuracy warning:** This method is accurate to within 5 degrees only near the equinoxes. At solstices, the sunrise point can be shifted 23+ degrees from due East. Use this as a rough check, not a precision fix.

### The Midday Shadow / நண்பகல் கவனிப்பு

1. At solar noon, look at your shadow.
   சரியாக நண்பகலில், உங்கள் நிழலைப் பாருங்கள்.
2. **Northern Hemisphere:** Your shadow points **True North**.
   **வட அரைக்கோளம்:** உங்கள் நிழல் **உண்மையான வடக்கை** நோக்கி இருக்கும்.
3. **Southern Hemisphere:** Your shadow points **True South**.
   **தென் அரைக்கோளம்:** உங்கள் நிழல் **உண்மையான தெற்கை** நோக்கி இருக்கும்.

**Note:** Solar noon is not necessarily 12:00 on your clock. See the "Common Failure Modes" section below for why, and how to estimate true solar noon.

### The Shadow-Stick Method (Detailed Procedure)

This is the most reliable field method for determining direction without any instruments. It requires only a stick, flat ground, and two small stones.

**Materials:**
- One straight stick, approximately 1 meter tall
- A patch of flat, level ground with direct sunlight
- Two small stones or other markers

**Procedure:**

1. **Plant the stick** vertically in flat ground. Check that it is as close to vertical as possible — lean it slightly and watch which way the shadow moves to verify plumb.

2. **Mark the tip of the shadow** with a stone. This is your first mark. Label it mentally or scratch a "1" beside it.

3. **Wait 15 to 20 minutes.** The shadow tip will move as the sun moves across the sky. The longer you wait, the more accurate the result, but 15 minutes is the practical minimum for a usable reading.

4. **Mark the new shadow tip** with a second stone. This is your second mark.

5. **Draw a line** (scratch it in the dirt, lay a stick, or stretch a cord) between the two marks. This line runs approximately **East-West**.

6. **Determine East and West.** In the Northern Hemisphere, the **first mark is the West end** and the **second mark is the East end** of the line. (The shadow moves from West to East as the sun moves from East to West.) In the Southern Hemisphere, the same convention holds — first mark is West, second is East.

7. **Find North.** Stand on the East-West line with the first mark (West) to your left and the second mark (East) to your right. You are now facing **North** (Northern Hemisphere). In the Southern Hemisphere, reverse: stand with the first mark to your right to face South.

```text
    Shadow-Stick Method (Top-Down View, Northern Hemisphere)

                        N
                        ^
                        |
                        |    stick (.)
                        |
           W <----[1]--------[2]----> E
                   ^    .     ^
                   |         /
              1st shadow   2nd shadow
              tip (West)   tip (East)
              t = 0 min    t = 20 min

     Sun moves E ---> W, so shadow tip moves W ---> E.
     Line from mark [1] to mark [2] = East-West line.
     Stand facing perpendicular to line = North.
```

8. **Optional refinement:** Repeat the procedure, waiting 30 minutes or more between marks, or take a third and fourth mark to average out errors. The more marks you take, the better your East-West line approximates the true arc.

**Accuracy expectations:**

| Condition | Expected accuracy |
|---|---|
| Tropics (0-23° latitude) | ± 10 degrees or worse |
| Mid-latitudes (30-55°) | ± 5 degrees |
| Near solar noon | Best results |
| More than 2 hours from solar noon | Accuracy degrades; shadow arc curvature introduces error |

**Best results** are obtained when the method is performed within **2 hours of solar noon**, at mid-latitudes, on a day with consistent sunshine.

---

## Nighttime Navigation

When the sun is below the horizon, the stars become your compass. On a clear night, stellar navigation can be more accurate than daytime solar methods.

### Finding Polaris via the Big Dipper (Ursa Major)

Polaris is not the brightest star in the sky — a common misconception. It is moderately bright (magnitude 2.0) and is found using the Big Dipper as a pointer:

1. Locate the Big Dipper (also called the Plough). It is one of the most recognizable star patterns in the Northern Hemisphere — seven stars forming a ladle or pot shape.

2. Identify the two stars that form the outer edge of the Dipper's "bowl" — these are called the **pointer stars**, named **Dubhe** (the upper one) and **Merak** (the lower one).

3. Draw an imaginary line from Merak through Dubhe and extend it approximately **5 times the distance** between those two stars. This line leads directly to **Polaris**.

4. Polaris marks True North. Drop a vertical line from Polaris to the horizon — that point on the horizon is due North.

5. Polaris's altitude above the horizon also tells you your approximate latitude: if Polaris is 35 degrees above the horizon, you are near latitude 35 degrees North.

```text
    Finding Polaris Using the Big Dipper (Ursa Major)

                          * Polaris
                          |  (True North)
                          |
                     5x   |  the distance
                          |  between Dubhe
                          |  and Merak
                          |
                   Dubhe  *
                         /    <- "pointer stars"
                  Merak *        (outer bowl edge)
                       |
                       * ------*
                       |  bowl  \
                       *--------* ---*--- handle
                                     \
                                      *

             Big Dipper / Ursa Major
```

### The Southern Cross Method (Southern Hemisphere)

There is no bright "South Star" equivalent to Polaris. Instead:

1. Locate the **Southern Cross (Crux)** — four bright stars forming a distinct cross shape, with the long axis being about 1.5 times the length of the short axis.

2. Identify the **long axis** of the cross (from the top star, Gacrux, through the bottom star, Acrux).

3. Extend this long axis in the direction from Gacrux to Acrux (that is, toward the foot of the cross) by approximately **4.5 times the length** of the long axis.

4. The point you arrive at is approximately the **South Celestial Pole**. There is no bright star there — it is a dark patch of sky.

5. Drop a perpendicular line from that point to the horizon. That point on the horizon is due **South**.

**Caution:** The "False Cross" (formed by stars in Vela and Carina) is a common source of confusion. The true Southern Cross is more compact, and the two bright "pointer stars" (Alpha and Beta Centauri) are nearby — if you see two very bright stars close together near the cross, you have the right one.

### Orion's Belt as an East-West Indicator

The three stars of **Orion's Belt** — Alnitak, Alnilam, and Mintaka — rise due East and set due West to an accuracy of approximately **plus or minus 3 degrees**, regardless of your latitude (as long as Orion is above the horizon). This makes them exceptionally useful:

- If you see Orion's Belt rising above the horizon, it is rising in the East.
- If you see it setting, it is setting in the West.
- Orion is visible from roughly October to March in the Northern Hemisphere and April to September in the Southern Hemisphere.

### Moon-Based Direction

The moon provides a rough directional clue when stars are partially obscured:

- The **illuminated side of the moon always faces roughly toward the sun**. At a first quarter moon (right half illuminated in the Northern Hemisphere), the illuminated side faces West in the evening — meaning the sun set to the West, confirming that direction.
- A crescent moon with its "horns" pointing left (in the Northern Hemisphere) indicates the sun is to the right — that is, the illuminated side points roughly toward where the sun is (below the horizon to the West in the evening, or below the horizon to the East before dawn).
- **Accuracy: very rough** (plus or minus 20 degrees). Use only when no better method is available.

---

## Direction vs. Path / திசை vs பாதை

- **Direction:** The absolute point (e.g., "I must go North").
- **Path:** The real-world trail (e.g., "I must follow the river valley to go North").
- **Aadhiyandham Rule:** Always prioritize the **Path** (Module 01) over the raw direction to conserve energy. A 10 km trail that curves gently northward is almost always preferable to a 7 km straight-line bearing over rough terrain.

---

## Common Failure Modes

### 1. Confusing Magnetic North with True North

If you use a compass for one bearing and the sun for another, you are mixing two different norths. In regions with high magnetic declination (parts of Canada, Siberia, or near magnetic anomalies in volcanic rock), the difference can exceed **20 degrees**. Over a 20 km journey, a 20-degree error puts you nearly 7 km off your intended destination. Always know which "north" you are referencing, and convert if necessary.

### 2. Shadow-Stick Errors in the Tropics Near Equinox

Between latitudes 23.44 degrees N and 23.44 degrees S, the sun can pass nearly or exactly overhead during certain dates. When this happens, shadows become extremely short or vanish entirely at solar noon, making the shadow-stick method unreliable. If you are in the tropics near an equinox, use the shadow-stick method only in the early morning or late afternoon, when shadows are long enough to measure — but accept that accuracy will be degraded.

### 3. Cloud Cover

Heavy overcast prevents direct solar and stellar observation. Fallback methods exist but are far less reliable:

- **Wind patterns:** In some regions, prevailing winds blow from a consistent direction. This requires local knowledge you may not have.
- **Moss growth on trees:** The old adage that moss grows on the north side of trees is unreliable. Moss grows on the side with the most moisture, which depends on local terrain, drainage, and canopy — not compass direction.
- **Terrain flow:** Water flows downhill. If you know a river lies to the north, following a downhill drainage pattern may lead you to it. This is terrain association, not direction-finding, but it can substitute in an emergency.

The best strategy under overcast is to **wait**. If conditions may clear within hours, shelter in place rather than navigating blindly.

### 4. Time-Zone Confusion and Solar Noon

Solar noon — the moment when the sun is highest — does **not** correspond to 12:00 on your clock in most locations. Clock time is set by time zones, which are political constructs spanning up to 15 degrees of longitude (and sometimes more — China uses a single time zone across 60 degrees of longitude). Daylight saving time adds another hour of offset in many countries.

To estimate true solar noon without a clock:

- The shadow-stick method itself reveals solar noon: it is the moment when the shadow is shortest. If you start marking shadows before you think noon should be, the shortest shadow you observe is your best noon reference.
- As a rule of thumb, for every degree of longitude you are from the center of your time zone, solar noon shifts by 4 minutes. If you are 7.5 degrees west of your time zone's central meridian, solar noon is approximately 30 minutes after clock noon.

### 5. Parallax Error with Polaris at Low Latitudes

Near the equator, Polaris sits very low on the northern horizon and may be obscured by haze, terrain, or light pollution. Below about 10 degrees North latitude, consider Polaris unreliable and use Orion's Belt or other stellar methods instead.

---

## Vocabulary of the Foundation

- **Azimuth:** A direction expressed as a clockwise angle from True North, measured in degrees (0 to 360). Due East is azimuth 090, due South is 180, due West is 270.

- **Bearing:** Functionally synonymous with azimuth in most field navigation contexts. Some traditions express bearing relative to North or South (e.g., "N 45 E" or "S 30 W"), but degree-azimuth is more common in modern practice.

- **Declination (magnetic):** The angle between True North and Magnetic North at a given location. Expressed as East or West. A declination of "12 degrees West" means the compass needle points 12 degrees west of True North.

- **Declination (solar):** The angle between the sun's position and the celestial equator, varying from +23.44 degrees to -23.44 degrees over the year. Determines where on the horizon the sun rises and sets.

- **Solar noon:** The moment when the sun crosses the local meridian and reaches its highest point in the sky. The shadow of a vertical object is shortest at this moment.

- **Zenith:** The point on the celestial sphere directly above the observer. When the sun is at your zenith, it is directly overhead and your shadow disappears.

- **Celestial pole:** The point on the celestial sphere directly above a geographic pole. The North Celestial Pole is marked (approximately) by Polaris. The South Celestial Pole has no bright marker star.

- **Cardinal direction:** One of the four principal compass points: North, South, East, West.

- **Intercardinal direction:** The four directions midway between the cardinal directions: Northeast, Southeast, Southwest, Northwest.

---

## Cross-References

- **Module 01.01** — Terrain and Route Selection: How to choose a path once you know your direction.
- **Module 01.02** — Positioning Basics: Determining where you are before deciding which way to go.
- **Module 01.04** — Map Reading Without GPS: Translating direction into movement on a topographical map.
- **Section 02 — The Site** — Site selection criteria once your journey reaches the candidate refugia location.
- **Glossary** — See [../../Glossary.md](../../Glossary.md) for full definitions of key terms including Execution, Preparation, and Refugia.

---

## Further Study

The following references provide significantly deeper treatment of celestial navigation and field orientation:

1. **Harold Gatty, *Finding Your Way Without Map or Compass*** — The foundational modern text on natural navigation, covering sun, stars, wind, ocean swells, and biological indicators.

2. **Tristan Gooley, *The Natural Navigator*** — A comprehensive and accessible guide to reading natural signs for direction, including detailed treatment of shadow behavior, star paths, and weather-based clues.

3. **US Army FM 3-25.26, Chapter 9 (Direction from Celestial Bodies)** — Military field manual covering solar and stellar navigation procedures with precision. Freely available online. The shadow-tip method described in this module is adapted from procedures in FM 3-25.26.

4. **Bob Burns & Mike Burns, *Wilderness Navigation: Finding Your Way Using Map, Compass, Altimeter & GPS*** — Practical guide with excellent coverage of magnetic declination, compass use, and integrating celestial observations with instrument-based navigation.

---

## Practical Implementation Guide for Beginners

### Step-by-Step Action Plan

- **Preparation (Months 1-3):** Begin physical conditioning. Walk 5 miles a day with a 20lb backpack. Acquire baseplate compasses and physical topographical maps. Practice the shadow-stick method weekly to build proficiency — it should become automatic.
- **Execution (Transit):** Never travel at night unless necessary. Establish a buddy system. Take directional readings at least three times per day: morning (sunrise bearing), midday (shadow method), and evening (sunset bearing). Log each reading.
- **Arrival:** When you reach the candidate location, establish a temporary perimeter before resting.

### Troubleshooting in the Field

- **Lost Navigation:** If you lose your bearings, STOP. Do not wander. Use the shadow-stick method to find North and re-orient using a known landmark (river or mountain).
- **Overcast conditions:** If you cannot see the sun or stars, do not guess. Shelter and wait for a clearing. A brief 5-minute break in the clouds is enough to perform a shadow-stick reading.
- **Injury:** Have a designated medic. Prioritize stopping bleeding and stabilizing fractures before continuing.

### Community Resilience

Ensure every adult and capable child knows how to find direction using the sun and stars. A compass can break. A GPS unit can lose power. The sun and Polaris are always there. **Redundancy is survival.**

---

*The sun is the clock and the compass.*
*சூரியன் என்பது கடிகாரமும் திசைகாட்டியும் ஆகும்.*
