# Mechanical Power: Water Wheels, Flywheels, and Line-Shaft Systems

**Alignment:** Outcome 5: Decadal and Generational Resilience

Mechanical power from water is the foundation of pre-industrial manufacturing, and its significance cannot be overstated. A single overshot water wheel of three meters diameter, fed by a modest stream with adequate head, produces 500 to 750 watts of continuous mechanical power. This is equivalent to seven to ten human workers operating around the clock without rest, food, or wages. The arithmetic is decisive: a community that harnesses even a small watercourse gains a manufacturing capability that no amount of manual labor can match.

This is precisely why every medieval manufacturing center, from the iron forges of the Weald to the textile mills of Flanders, was built on a river. The water wheel is not a convenience; it is the irreducible prerequisite for any community that intends to manufacture tools, process grain, saw timber, or forge metal at scale.

The line-shaft system is the mechanism by which a single water wheel's rotational power is distributed to multiple workstations. A horizontal shaft, suspended from ceiling bearings, runs the length of a workshop. Flat belts connect the shaft to individual machines: forge bellows, grinding wheels, lathes, trip hammers, sawmills. Each connection uses a pair of fast-and-loose pulleys that allow any machine to be engaged or disengaged independently.

The entire system is robust, visible, entirely repairable with local materials, and has no component that cannot be fabricated by a competent woodworker and blacksmith. Line-shaft distribution operated continuously from the first century CE through the early twentieth century, when electric motors finally displaced mechanical power transmission.

This module covers the complete engineering chain from water source to working machine: water source assessment and flow measurement, wheel design and construction for the overshot configuration, flywheel energy storage for smoothing variable input, line-shaft distribution and bearing design, and individual machine connection via belt-driven takeoffs.

Every calculation is worked through with realistic numbers. Every construction step uses materials available in a post-industrial or pre-industrial context. The goal is a functioning workshop powered by water, capable of sustained manufacturing operations across decades.

> **CAUTION**: Water wheel construction involves working near flowing water, handling heavy timber, and dealing with rotating machinery. Drowning, crush injuries, and entanglement are the primary hazards. Never work alone near flowing water. Wear close-fitting clothing around all rotating components. Establish lockout procedures before any maintenance: close the sluice gate and wait for the flywheel to stop completely before approaching the shaft. Children must be excluded from the machine hall during operation. A single moment of inattention around a rotating line-shaft can result in death.

---

## Theoretical Foundation

### The Physics of Water Power

The energy available from falling water derives from gravitational potential energy. The fundamental relationship is straightforward: energy equals mass times gravitational acceleration times height, or E = mgh. Water falling through a height h carries energy in direct proportion to its mass and the distance it falls. The engineering task is to capture as much of this energy as possible and convert it into rotational mechanical work.

The power available from a water source is calculated as:

P = rho x g x Q x h x eta

Where rho is water density (1000 kg/m cubed), g is gravitational acceleration (9.81 m/s squared), Q is volumetric flow rate (m cubed/s), h is head or fall height (m), and eta is wheel efficiency as a decimal fraction. This equation is the single most important formula in this module. Every design decision flows from it.

Consider a worked example. A modest stream delivers Q = 0.01 cubic meters per second, roughly equivalent to filling a ten-liter bucket in one second. The available head is 3 meters. Using a well-built overshot wheel with an efficiency of 0.75:

P = 1000 x 9.81 x 0.01 x 3 x 0.75 = 220 watts

This is modest but meaningful: enough to drive a grinding wheel or a small forge bellows continuously, day and night, without human effort.

Double the flow rate to 0.02 cubic meters per second and the power doubles to 441 watts. Increase the head to 5 meters with the original flow and the power rises to 368 watts. The formula rewards both flow and head, but head is the more practical lever because it can be increased through civil engineering (building a dam, extending a flume) without requiring a larger water source.

Three fundamental wheel types exist, distinguished by where the water is delivered to the wheel:

The **overshot wheel** receives water at the top. Water fills buckets attached to the rim, and the weight of the filled buckets drives the wheel downward. This design captures gravitational potential energy directly and achieves efficiencies of 60 to 90 percent. It requires high head (greater than 3 meters) relative to wheel diameter but tolerates low flow. It is the most efficient design and the one recommended for most installations. The overshot wheel turns slowly (typically 5 to 15 RPM at the wheel itself), which reduces wear on bearings and allows the use of wooden gearing without excessive tooth wear.

The **breastshot wheel** receives water at approximately axle height. It captures a combination of potential and kinetic energy, achieving efficiencies of 35 to 65 percent. It is the appropriate compromise when available head is moderate (1.5 to 3 meters). The breastshot design requires a curved masonry or timber breast (a close-fitting wall that follows the curvature of the wheel) to prevent water from escaping before it has done maximum work on the buckets.

The **undershot wheel** sits in the stream with water flowing beneath it, using kinetic energy alone. Efficiencies are low, typically 20 to 40 percent, but construction is the simplest and no elevated flume is required. It suits sites with low head (less than 1.5 meters) and high flow volume. The undershot wheel spins faster than the overshot design, which can be advantageous for machines requiring higher RPM but increases bearing wear proportionally.

The historical depth of this technology is worth noting. Vitruvius described water wheels in *De Architectura* around 25 BCE. The Barbegal aqueduct mill complex near Arles, dating to the second century CE, operated sixteen overshot wheels arranged in two parallel cascades, each wheel feeding its tailrace into the headrace of the wheel below. The complex produced flour for an estimated 12,000 people. This was industrial-scale manufacturing nearly two millennia before the steam engine.

By the medieval period, water wheels powered virtually every manufacturing process in Europe: grain milling, cloth fulling, iron smelting, tanning, paper production, and sawmilling. The Domesday Book of 1086 recorded 5,624 water mills in England alone. The technology is not speculative. It is the most thoroughly proven mechanical power system in human history, with a track record spanning two millennia across every climate that had flowing water.

### Flywheel Energy Storage

A flywheel stores energy in the form of rotational kinetic energy, described by the equation E = one-half times I times omega squared, where I is the moment of inertia of the wheel and omega is the angular velocity in radians per second. For a rim-weighted wheel (the most practical design, where most mass is concentrated at the outer edge), the moment of inertia simplifies to I approximately equals m times r squared, where m is the mass of the rim and r is the radius.

The flywheel serves a critical smoothing function. Water flow is never perfectly constant. Debris passes through the flume, seasonal variation changes the available head and flow, and even moment-to-moment turbulence causes fluctuations. Without a flywheel, these variations translate directly into speed changes at the working machines, causing tool chatter on lathes, uneven grinding, inconsistent hammer blows, and accelerated wear on bearings and belts.

The flywheel absorbs energy during moments of excess flow and releases it during momentary deficits, maintaining a far more constant shaft speed than the water input alone would permit. Think of it as a mechanical capacitor: it charges when input exceeds demand and discharges when demand exceeds input.

A practical sizing rule: the flywheel should store at least ten seconds of working energy at the system's design power output. For a 500-watt system, this means E = 5000 joules. Working backward with a 1.5-meter diameter wheel (radius 0.75 meters) spinning at 60 RPM (omega = 6.28 radians per second):

m = 2E / (r squared x omega squared)
m = 2 x 5000 / (0.5625 x 39.44)
m = approximately 450 kilograms

This is achievable with a heavy timber rim whose segments are drilled and loaded with stones, sand, or scrap iron. The mass can be adjusted after construction by adding or removing ballast material.

Balancing is essential. An unbalanced flywheel generates vibration that increases with the square of the rotational speed. Even mild imbalance causes progressive damage to bearings, loosens joints, and can lead to catastrophic structural failure.

Static balancing is performed by rotating the flywheel slowly and observing where it comes to rest. Weight is added to the point diametrically opposite the rest position. The process is repeated until the wheel will rest at any angular position without preference, indicating that the center of mass coincides with the axis of rotation.

### Line-Shaft Power Distribution

The line-shaft is a horizontal rotating shaft running the length of the workshop, suspended from ceiling-mounted bearing blocks at regular intervals. It receives power from the water wheel (typically through the flywheel) at one end and distributes it to individual machines along its length through belt-driven pulleys.

Power takeoff at each machine uses flat belts (tanned leather, woven hemp, or cotton fabric). The belt wraps around a pulley on the line-shaft and a corresponding pulley on the machine. The speed relationship is governed by the pulley ratio formula:

N1 x D1 = N2 x D2

Where N represents RPM and D represents pulley diameter. A 30-centimeter pulley on the line-shaft driving a 10-centimeter pulley on the machine shaft produces a 3:1 speed increase. This allows a line-shaft turning at a moderate 60 RPM to drive a grinding wheel at 180 RPM or a lathe at higher speeds still, simply by selecting the appropriate pulley diameters.

The fast-and-loose pulley arrangement is the primary safety mechanism and the feature that makes the line-shaft system practical for a multi-machine workshop. Each machine station has two pulleys mounted side by side on its input shaft. The "fast" pulley is keyed or pinned to the machine shaft so that it drives the machine when the belt runs on it. The "loose" pulley sits on a freely rotating bushing and transmits no power.

A belt-shifter fork, operated by a wooden lever within reach of the machine operator, slides the belt from one pulley to the other. Shifting from fast to loose disconnects the machine instantly without stopping the line-shaft.

This allows individual machines to be started, stopped, and maintained independently, and provides the critical safety function of disconnecting a machine in an emergency.

Bearing design determines the lifespan and efficiency of the entire system. Hardwood bearings, made from dense species such as lignum vitae, ironwood, or well-seasoned oak, are the appropriate technology. The bearing block is split horizontally so the upper half can be removed for shaft installation and maintenance.

The bore is cut to the shaft diameter plus one to two millimeters of clearance. Too tight and the shaft binds; too loose and it wobbles, causing vibration. The bearing surface is lubricated with rendered animal fat, linseed oil, or tallow.

The friction coefficient of greased wood on wood is approximately 0.04 to 0.08, compared with 0.2 to 0.5 for dry contact -- a reduction in friction losses of 80 to 90 percent. Bearing life under regular lubrication is one to five years, making bearings a planned replacement item.

The Lowell textile mills (1820s-1890s) powered entire factory floors from single water wheels via line-shafts spanning 10 to 50 meters, with measured transmission efficiencies of 80 to 95 percent.

Power losses come from three sources: bearing friction (3 to 10 percent, the largest component), belt slippage (1 to 3 percent for properly tensioned leather), and windage (negligible at workshop speeds). A well-maintained system delivers 85 to 95 percent of the water wheel's output to the working machines.

### Machine Applications

Each workstation connects to the line-shaft to perform a specific function. The connection type depends on whether the machine requires rotary or reciprocating motion.

Rotary machines (grinders, lathes, mills) connect directly through pulleys with appropriate diameter ratios. Reciprocating machines (bellows, saws, trip hammers) require a crank mechanism to convert rotary to linear motion. The crank throw length determines the stroke distance.

Typical machine connections include:

- **Forge bellows** (reciprocating motion via crank): continuous air blast for metalworking at 50 to 100 liters per minute, consuming approximately 80 to 150 watts
- **Grinding and sharpening wheels**: 200 to 500 RPM for tool maintenance and edge work, consuming approximately 50 to 120 watts
- **Trip hammers**: 40 to 80 strokes per minute for forging, fulling cloth, and crushing ore, consuming approximately 200 to 400 watts
- **Lathes**: 100 to 300 RPM for wood and metal turning, consuming approximately 80 to 200 watts
- **Reciprocating saws** (via crank conversion): timber processing, consuming approximately 200 to 350 watts
- **Grain mills**: 60 to 120 RPM for milling flour and processing grain, consuming approximately 150 to 300 watts

Power budgeting is essential. The total available power from the water wheel must exceed the sum of all simultaneously operating machines. Heavy machines such as the trip hammer and saw each consume 200 to 400 watts and should be run one at a time. Light machines such as the grinder and bellows consume 50 to 150 watts each and can operate concurrently.

A workshop schedule alternating heavy and light tasks throughout the day maximizes the utility of a single water wheel. For example, with a 600-watt wheel: morning hours run the trip hammer (350W) with bellows (100W) for 450W total. Afternoon hours run the saw (300W) alone. The grinder (80W) and lathe (120W) can operate concurrently at any time, as their combined 200W leaves ample capacity. Post this schedule visibly so operators do not inadvertently overload the system.

---

## Core Principles

1. **The Head-Over-Flow Principle** -- For a given power output, it is more efficient to increase the height of water fall (head) than to increase the volume of water flow. An overshot wheel with 5 meters of head and small flow outperforms an undershot wheel with 1 meter of head and large flow. The power equation is linear in both Q and h, but increasing head simultaneously improves wheel efficiency (overshot versus undershot), compounding the advantage. Site selection should prioritize head above all other factors. A site with a 5-meter drop and a trickle will outperform a site with a 1-meter drop and a torrent.

2. **The Flywheel Smoothing Principle** -- All water-powered systems require a flywheel to store rotational energy and smooth power delivery. Without it, variable flow causes tool chatter, uneven grinding, inconsistent forging, and accelerated wear on bearings and belts. The flywheel is not optional; it is a core structural component of the power system, as essential as the wheel itself.

3. **The Single-Source Distribution Principle** -- One well-built water wheel powering one line-shaft serving multiple machines is more efficient, reliable, and maintainable than multiple small wheels each driving individual machines. Centralize the power source; distribute through the shaft. This concentrates maintenance at a single point and simplifies water management.

4. **The Disconnect Safety Principle** -- Every machine connected to the line-shaft MUST have an independent disconnect mechanism via fast-and-loose pulleys. A worker caught in a machine must be freed without stopping the entire workshop. This is non-negotiable safety infrastructure. Any machine connected rigidly to the line-shaft without a disconnect is a death trap.

5. **The Bearing Maintenance Principle** -- Bearings are the consumable component of any mechanical power system. Plan for regular inspection (weekly), lubrication (daily for heavy-use bearings), and replacement (annually for high-load positions). Stock replacement bearing blanks and maintain a supply of lubricant. A seized bearing can halt the entire workshop and, in the worst case, cause a fire. Designate one community member as the millwright responsible for this maintenance.

---

## Practical Implementation

### Site Assessment for Water Power

Begin by measuring the available head: the height difference between the water intake point and the wheel discharge point. Use a line level, a transparent hose water level, or surveying instruments if available. Even a one-meter error in head measurement significantly affects power calculations, so take care with this step.

Measure flow rate by temporarily damming the stream and timing how long it takes to fill a container of known volume. A 20-liter bucket filled in 2 seconds gives Q = 0.01 cubic meters per second. Repeat the measurement at least three times and average the results to account for natural variation.

Calculate available power using P = 1000 x 9.81 x Q x h x 0.7 for initial estimates, using the conservative efficiency factor of 0.7. The minimum viable installation delivers 150 watts sustained, enough for a single grinder or small bellows. The target for a full workshop is 500 watts or more.

Crucially, measure flow in both wet and dry seasons. Design the system for the dry-season minimum flow, as surplus water during the wet season can be wasted over a spillway or stored in a millpond. A system designed for average flow will fail during the dry months precisely when manufacturing continuity matters most.

Record all measurements in a site assessment log with dates, weather conditions, and recent rainfall. A twelve-month flow record is far more valuable than a single measurement. If evaluating multiple stream sites, compare them using the product of head times dry-season flow: the highest value delivers the most reliable power year-round.

### Water Wheel Construction (Overshot Design)

The wheel diameter should be 80 to 90 percent of the available head height. For a 3-meter head, the wheel should be 2.5 to 2.7 meters in diameter. The width of the wheel, measured along the axle, should be 30 to 60 centimeters depending on the volume of flow to be captured.

The wheel carries 24 to 36 buckets around its rim, each holding 2 to 5 liters. Buckets are constructed from split and shaped timber planks or bent sheet metal if available.

Each bucket must be angled so that it fills efficiently as it passes through the water stream at the top of the wheel and empties cleanly as it reaches the bottom. Poorly designed buckets that retain water on the ascending side waste energy by working against the wheel's rotation.

The axle must be hardwood of at least 20 centimeters diameter (oak, ash, or equivalent dense species) or, preferably, salvaged steel pipe or shaft.

The wheel is supported by heavy timber A-frames on both sides, each anchored to stone or poured-concrete foundations set below the frost line. These foundations must resist the lateral forces generated by the water impact and the weight of the wheel itself, which may exceed one metric tonne when fully loaded with water.

The flume or headrace is a channel that delivers water from the upstream intake to the top of the wheel. It must maintain a gentle slope of 1 to 2 percent grade and be sized to carry the full design flow without overtopping. Line the flume with split timber or clay to minimize seepage losses.

A wooden sluice gate at the point where the flume meets the wheel controls the flow, allowing the wheel to be shut down for maintenance or during periods when power is not needed.

The tailrace carries water away from the base of the wheel and must discharge at a point low enough to prevent backwater from submerging the lower buckets, which would reduce efficiency by opposing the wheel's rotation. A drop of at least 30 centimeters between the lowest point of the wheel and the tailrace water level is recommended.

Before committing to construction, build a temporary test rig: install a simple undershot paddle wheel at the site to confirm consistent water delivery over at least two weeks. This low-cost experiment reveals problems (intermittent flow, excessive debris, unstable banks) before the community invests hundreds of labor-hours in a full overshot installation.

### Flywheel Construction

The flywheel diameter should be 1.2 to 1.8 meters. Construction uses a heavy timber hub built up from laminated segments, with a rim assembled from curved or straight timber segments joined by mortise-and-tenon or bolted connections.

Holes are drilled in the rim segments and filled with stones, iron-sand, or scrap iron to increase mass to the design target.

The flywheel mounts on the line-shaft between the water wheel connection and the first machine station. Ensure the flywheel is rigidly keyed to the shaft so that no slippage occurs between the two. The mounting must be strong enough to resist the full torque of the water wheel without loosening over time.

After construction, balance the flywheel using the static method: spin it slowly by hand, observe where it consistently comes to rest, add weight to the point diametrically opposite, and repeat until the wheel shows no positional preference. Document the final weight distribution so that balance can be restored after any future repairs.

Unlike bearings and belts, the flywheel has no sliding contact surfaces and experiences minimal wear. With periodic inspection for rim cracks and verification that ballast has not shifted, a timber flywheel serves for decades.

### Line-Shaft Installation

The shaft should be straight-grained hardwood (ash or oak) of 10 to 15 centimeters diameter, or salvaged steel pipe of similar dimensions. Inspect the shaft for knots, splits, or grain deviation that could cause failure under torsional load. A knot in a shaft under torsion acts as a stress concentrator and will eventually initiate a crack that propagates to fracture. Reject any shaft stock with knots larger than one-quarter of the shaft diameter.

For spans longer than 3 to 4 meters, join sections using iron ferrules or sleeve couplings to maintain rigidity. Each joint must be as strong as the shaft itself in both torsion and bending. A failed coupling under full load will whip the disconnected shaft end with lethal force.

Timber brackets with bearing blocks are mounted to the ceiling structure at intervals of 1.5 to 2 meters. Each bearing block is a split hardwood housing lined with dense end-grain hardwood, bored to shaft diameter plus 1 to 2 millimeters clearance, and lubricated with rendered animal fat or linseed oil.

Belt material should be tanned leather for best performance, though woven hemp or cotton is adequate and rawhide is functional but prone to stretching. Correct belt tension is verified by pressing the belt at its midpoint with moderate finger pressure; it should deflect 10 to 15 millimeters per meter of span. Excessive tension accelerates bearing wear; insufficient tension causes slippage and belt degradation.

For the fast-and-loose pulley arrangement at each machine station, mount two pulleys side by side on the machine's input shaft. The fast pulley is keyed or pinned to the shaft; the loose pulley rotates freely on a greased hardwood bushing. A belt-shifter fork, made from a forked wooden lever pivoting on a fixed bracket, allows the operator to slide the belt from one pulley to the other with a single hand motion.

Alignment is critical. The line-shaft pulleys and machine pulleys must be coplanar; misalignment causes the belt to track to one side and eventually walk off the pulley. Verify alignment by stretching a taut string from the face of the line-shaft pulley to the machine pulley. Both faces should touch the string across their full width. Shim the bearing blocks or machine mounts as needed.

```text
WATER WHEEL AND LINE-SHAFT SYSTEM -- SIDE VIEW

    FLUME (headrace)
    ================>
                     |
                 [SLUICE GATE]
                     |
                     V
              +------+------+
             /   OVERSHOT    \
            /    WATER WHEEL  \
           |    2.5-3m dia.    |
            \   (buckets)     /
             \               /
              +------+------+
                     |
                   AXLE -----> [FLYWHEEL 1.5m, 400-500 kg]
                     |
    =================|==================== LINE-SHAFT ===========
    |        |        |        |        |        |
  [BELLOWS] [GRINDER] [TRIP   [LATHE]  [SAW]   [MILL]
  (crank)            HAMMER]
                     (crank)           (crank)

    Each machine has FAST + LOOSE pulleys for independent disconnect

    TAILRACE
    <================
```

---

## Common Failure Modes

**Bearing Seizure** -- Insufficient lubrication causes the shaft to bind in its bearing, generating heat through friction that can ignite the timber bearing block and surrounding structure. Prevention requires a daily lubrication schedule and weekly bearing inspection. Check for excessive heat by placing a hand near (not on) the bearing during operation. A bearing that is too hot to hold a hand near for five seconds requires immediate shutdown and inspection. Stock replacement bearing blanks so that a worn bearing can be swapped during a scheduled shutdown rather than after a failure.

**Belt Slippage** -- Loose or worn belts slip on pulleys, reducing power transmission efficiency and causing the belt to heat and deteriorate rapidly. Prevention requires weekly belt tension checks using the finger-deflection method. Dress leather belts with neatsfoot oil or beeswax to maintain grip and flexibility. Replace any belt showing cracks, delamination, or significant fraying before it fails under load.

**Flywheel Imbalance** -- An unbalanced flywheel causes progressive vibration that loosens joints, cracks bearing blocks, fatigues the shaft, and can result in catastrophic structural failure as the wheel tears free of its mounts. Prevention begins with careful balancing during construction and rebalancing after any modification or repair. If vibration increases during operation, stop the system immediately and investigate before restarting.

**Flume Blockage** -- Leaves, ice, sediment, and debris block the flume, reducing or stopping water delivery. Prevention requires a trash rack at the flume intake, constructed from iron bars or hardwood stakes spaced 2 to 3 centimeters apart. Inspect and clear daily, and more frequently during autumn leaf-fall or spring floods.

**Seasonal Flow Loss** -- Dry season reduces stream flow below the minimum viable power threshold. Prevention requires building a millpond upstream, sized for at least four hours of continuous operation at design flow rate. The millpond also settles sediment that would otherwise abrade the wheel and flume. In regions with severe dry seasons, consider supplementary power sources (treadmill, animal power) as backup.

**Entanglement Injury** -- Clothing, hair, or tools caught in the rotating shaft, belts, or pulleys. This is the most dangerous failure mode and is frequently fatal. A line-shaft at 60 RPM pulls a caught sleeve into the machinery faster than any human reaction time can respond. Prevention is entirely procedural: tie back all hair, wear close-fitting clothing with no loose sleeves, remove all jewelry. Mark a clear "danger zone" around all rotating components with painted lines or rope barriers. Install belt guards wherever possible. Never reach into running machinery; use the fast-and-loose disconnect first. This rule admits no exceptions. Train every person who enters the workshop in the danger zones before they cross the threshold.

---

## Vocabulary of the Foundation

- **Overshot wheel** -- A water wheel where water is delivered to the top of the wheel, filling buckets that descend under gravity. Achieves the highest efficiency of any wheel type, typically 60 to 90 percent.
- **Breastshot wheel** -- A water wheel where water enters at approximately axle height, combining gravitational and kinetic energy capture. Moderate efficiency of 35 to 65 percent.
- **Undershot wheel** -- A water wheel where water flows beneath the wheel, using kinetic energy only. Lowest efficiency at 20 to 40 percent but requires the simplest construction and lowest head.
- **Head** -- The vertical distance water falls from the intake point to the wheel discharge. Determines the gravitational potential energy available per unit mass of water.
- **Flow rate (Q)** -- The volume of water passing a point per unit time, measured in cubic meters per second. Together with head and efficiency, determines available power.
- **Flywheel** -- A heavy wheel that stores rotational kinetic energy, smoothing power delivery through fluctuations in water flow. Essential for consistent machine operation.
- **Line-shaft** -- A horizontal rotating shaft distributing mechanical power from a single source (the water wheel) to multiple machines along its length via belt-driven pulleys.
- **Fast-and-loose pulleys** -- A paired pulley arrangement allowing individual machines to be connected to or disconnected from the line-shaft without stopping the shaft. The primary safety and operational control mechanism.
- **Headrace/flume** -- The channel delivering water from the source or millpond to the top of the water wheel.
- **Tailrace** -- The channel carrying spent water away from the base of the wheel after it has performed work.
- **Sluice gate** -- An adjustable gate in the flume controlling the volume of water delivered to the wheel. Used for power regulation and shutdown.
- **Bearing** -- The contact surface between a rotating shaft and its stationary support structure. The primary wear component in any mechanical system, requiring regular lubrication and periodic replacement.
- **Trash rack** -- A grid of bars or stakes at the flume intake that prevents leaves, branches, ice, and debris from reaching and damaging the wheel.
- **Millpond** -- A reservoir constructed upstream of the wheel, storing water for use during low-flow periods and settling sediment before it reaches the flume.
- **Belt dressing** -- A substance such as neatsfoot oil, beeswax, or tallow applied to leather drive belts to maintain their grip on pulleys and prevent drying and cracking.

---

## Cross-References

- [01. Rationale: Mechanics](01_Rationale_and_Importance.md) -- manufacturing timeline and power-first principle
- [04. Material Synthesis](04_Material_Synthesis_and_Recycling.md) -- forge bellows powered by the line-shaft
- [06. Advanced Structural Engineering](06_Advanced_Structural_Engineering.md) -- foundations for the wheel structure
- [Outcome 1, Section 02.04: Water Sovereignty](../../Outcome_1_Locating_Refugia/02_The_Site/04_Water_Sovereignty_and_Hydrams.md) -- water source assessment
- [Outcome 1, Section 02.05: Hydrological Analysis](../../Outcome_1_Locating_Refugia/02_The_Site/05_Hydrological_Analysis_and_Watershed_Math.md) -- flow measurement and seasonal variation
- [Outcome 2, Section 06.04: Shelter and Thermal Grounding](../../Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/04_Shelter_and_Thermal_Grounding.md) -- timber construction techniques

---

## Further Study

- Terry S. Reynolds, *Stronger than a Hundred Men: A History of the Vertical Water Wheel* (1983)
- John G. Landels, *Engineering in the Ancient World* (2000) -- Roman water mills
- Rex Wailes, *The English Windmill* (1954) -- complementary wind power
- Oliver Evans, *The Young Mill-Wright and Miller's Guide* (1795) -- classic American millwright manual
- W. Fairbairn, *Treatise on Mills and Millwork* (1861-1863) -- Victorian-era line-shaft engineering

---

## Glossary Reference

*See [../../Glossary.md](../../Glossary.md) for full definitions of:*

- **Bloomery**
- **Recycling Cliff**
- **Refugia**
