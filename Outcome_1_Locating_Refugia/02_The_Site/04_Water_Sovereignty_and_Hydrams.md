# Water Sovereignty: The Hydraulic Ram Pump Guide

**Alignment:** Outcome 1: Locating and Connecting Optimal Refugia

> **CAUTION**: Hydraulic ram pumps generate high-pressure water hammer pulses. Do not place hands near the waste valve during operation — the valve closes with significant force. Ensure all pipe connections are rated for the maximum water hammer pressure (up to 30 bar in the drive pipe). Test the system at low flow before opening to full supply.

---

## Theoretical Foundation

The hydraulic ram pump is among the most elegant machines ever devised — it uses the energy of flowing water to lift a fraction of that water to a height far above its source, with no external power, no fuel, and no moving parts beyond two simple valves. Understanding the physics behind this device is essential for building one that actually works.

### Water Hammer and the Joukowsky Equation

The ram pump operates on a phenomenon called **water hammer** — the enormous pressure spike that occurs when flowing water is suddenly stopped. When a valve slams shut on a moving column of water, a pressure wave travels back through the pipe at the speed of sound in water (approximately 1,400 m/s in a rigid steel pipe). The magnitude of this pressure spike is described by the Joukowsky equation:

    ΔP = ρ × c × ΔV

Where:
- ΔP = pressure rise (Pascals)
- ρ = water density (1,000 kg/m³)
- c = wave speed in water (~1,400 m/s in rigid pipe)
- ΔV = velocity change (m/s)

For water flowing at 2 m/s that is stopped instantaneously:

    ΔP = 1,000 × 1,400 × 2 = 2,800,000 Pa = 28 bar

This is an extraordinary pressure — 28 times atmospheric pressure — generated from nothing more than water flowing downhill and a valve slamming shut. This pressure spike is what drives water uphill. The hydraulic ram pump is, at its core, a device that harvests water hammer energy in a controlled, repeating cycle.

```text
  HYDRAM SIDE-VIEW CROSS-SECTION
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SPRING/                                          STORAGE TANK
  STREAM     Drive Pipe (rigid, sloping down)       /  [====]
    |~~|    ___________________________________    /   |    |
    |  |===|  water flows --->  v=2 m/s        |  /    | 30m|
    |  |   |___________________________________|=/     |  up|
    |__|        slope = h                  |   |       [====]
                                     +---------+         |
             supply head h = 3m      | RAM BODY|    delivery
                                     |         |    pipe
                                     | [D.V.]--+---> (to tank)
                                     |    |    |
                                     | [AIR  ] |
                                     | [CHAMB] |
                                     |    |    |
                                     | [W.V.] <--- waste valve
                                     +----|----+     "clack"
                                       spillback
                                       to stream
  D.V. = Delivery Check Valve    W.V. = Waste Valve (weighted)
```

### The Drive Pipe as Energy Accumulator

The drive pipe is not merely a conduit — it is the energy storage element of the system. The kinetic energy of the water column flowing through it is:

    KE = ½ × m × v²

For a 20 m drive pipe of 50 mm internal diameter with water flowing at 2 m/s:

    Cross-sectional area = π × 0.025² = 0.00196 m²
    Volume = 20 × 0.00196 = 0.0393 m³
    Mass = 0.0393 × 1,000 = 39.3 kg
    KE = ½ × 39.3 × 2² = 78.6 Joules per cycle

At a cycle rate of 60 beats per minute, the pump processes 78.6 J × 60 = 4,716 J/s = 4.7 kW of pulsed hydraulic power. This is a substantial amount of energy extracted from a modest stream.

The critical design constraint follows directly: the drive pipe **must** be rigid. Steel pipe is ideal; thick-walled Schedule 40 PVC is acceptable. Any flexibility in the pipe absorbs the water hammer energy as elastic deformation of the pipe wall rather than transmitting it as pressure to the delivery valve. A flexible garden hose as a drive pipe will cycle endlessly and deliver nothing.

### Efficiency and the D'Aubuisson Formula

The standard measure of hydraulic ram efficiency is the D'Aubuisson formula:

    η = (q × H) / (Q × h)

Where:
- η = efficiency (dimensionless, typically 0.6 to 0.8)
- q = delivery flow rate (L/min)
- Q = total flow rate entering the pump (L/min)
- H = delivery head — vertical rise from pump to storage tank (m)
- h = supply head — vertical fall from source to pump (m)

Rearranging to find delivery flow:

    q = η × Q × h / H

**Worked example:** A ram pump with 2 m supply head and 20 m delivery head, processing 20 LPM total flow at 70% efficiency:

    q = 0.70 × 20 × 2 / 20 = 1.4 LPM

That is 1.4 litres per minute, continuously, day and night. Over 24 hours:

    1.4 × 60 × 24 = 2,016 litres per day

At a survival water ration of 50 litres per person per day (drinking, cooking, basic hygiene), this single pump supplies 40 people. From a 2-metre waterfall and some scavenged pipe.

### The Air Chamber as Pulse Smoother

Without an air chamber, each water hammer cycle delivers a sharp pressure spike followed by zero flow. The delivery pipe would experience violent pulsing that stresses joints and fittings to failure. The air chamber solves this by trapping a volume of air above the delivery valve.

During the pressure spike, water is forced into the chamber, compressing the trapped air. This stores energy as compressed gas per **Boyle's Law**:

    P₁V₁ = P₂V₂

Between pulses, when the waste valve reopens and drive pipe pressure drops, the compressed air expands and pushes water steadily up the delivery pipe. The result is a reasonably smooth, continuous flow from a pulsed input.

However, air slowly dissolves into pressurized water according to **Henry's Law** — the solubility of a gas in a liquid is proportional to the partial pressure of that gas above the liquid. Over weeks of operation, the air chamber gradually fills with water, losing its buffering capacity. A waterlogged air chamber is the single most common failure mode of hydraulic ram pumps. Monthly inspection and recharging of the air chamber is mandatory.

```text
  ONE PUMP CYCLE (~1.5 seconds)
  =====================================================================
  Pressure
  in drive     Joukowsky spike
  pipe (bar)       ΔP = 28 bar
                      |
   30 |               *
      |              *|*
      |             * | *  <-- delivery valve opens,
      |            *  |  *     water forced into air chamber
   20 |           *   |   *
      |          *    |    *
      |         *     |     *
   10 |        *      |      *        air chamber slowly
      |       *       |       **      releases stored pressure
      |      *        |         ***
    0 |*****          |            ****************************
      |  ^            |            ^                    ^
      +--|------------|------------|--------------------|--->
      0.0s          0.3s        0.5s                 1.5s  Time
         |            |            |                    |
     waste valve   valve slams  delivery valve      waste valve
     OPEN: water   SHUT: water  closes: pressure    REOPENS:
     accelerates   hammer spike drops, air chamber   cycle
     in drive pipe (Joukowsky)  sustains flow        repeats
```

### Historical Context

The hydraulic ram was invented by **Joseph Michel Montgolfier** — the same Montgolfier of hot air balloon fame — in 1796 in Lyon, France. His original design was refined by his son-in-law, and by the mid-1800s thousands of rams were in continuous operation across Europe and the Americas, supplying water to farms, country estates, and small towns.

Many of these pumps operated continuously for 50 years or more with no maintenance beyond occasional valve replacement. The Blake Ram, manufactured in the United States, and the Green & Carter Ram from England were produced by the tens of thousands. The technology was displaced in the 20th century not because it failed, but because electric pumps were faster and could lift larger volumes. In a post-infrastructure context, the electric pump is useless and the hydraulic ram reclaims its place as the most reliable zero-energy water lifting device ever invented.

---

## Core Principles

1. **The Rigid Pipe Rule.** The drive pipe must be absolutely rigid along its entire length. Any flexibility — whether from thin-walled plastic, rubber couplings, or unsupported spans that can flex under pulse pressure — absorbs water hammer energy as elastic deformation rather than transmitting it to the delivery valve. A pump with a flexible drive pipe will cycle audibly but deliver nothing. Use steel pipe, galvanized iron, or Schedule 40 PVC rigidly supported at 1-metre intervals.

2. **The Head Ratio Constraint.** The practical delivery height is 10 to 20 times the supply head. A 2 m supply head can lift water 20–40 m. Beyond a ratio of 20:1, efficiency drops below 50% and the delivered volume becomes impractically small. If you need to lift water higher than 20× your available fall, consider staging two rams in series or finding a source with greater fall.

3. **The Air Chamber Discipline.** Check and recharge the air chamber monthly. A waterlogged chamber first manifests as increasingly violent pulsing in the delivery pipe, then as a dramatic drop in delivery flow, and finally as cessation of pumping altogether. To recharge: close the supply, drain the pump body, allow air to re-enter the chamber, then restart. Some designs incorporate a snifter valve that automatically admits a small air bubble on each cycle — this is worth the added complexity.

4. **The Screen Imperative.** Install a debris screen at the water intake — a 2 mm mesh stainless steel or brass screen across the drive pipe inlet. A single leaf, twig, or pebble lodged in the waste valve prevents it from seating properly. The valve must seal completely on each cycle to generate the water hammer pulse; even a partial seal bleeds off the pressure spike. In autumn leaf-fall or during storms, check the screen daily.

5. **The Continuous Operation Principle.** A hydraulic ram runs 24 hours a day, 7 days a week, 365 days a year, with no fuel, no operator, and no electricity. Design the entire system for unattended operation: include an overflow at the storage tank so it cannot burst when full, route waste valve discharge back to the stream so water is not lost to the watershed, and install the pump in a sheltered pit to protect it from debris and freezing.

---

## Materials Needed and Sourcing

| Material | Purpose | How to Find / Source |
| :--- | :--- | :--- |
| **Drive Pipe** | Build Momentum | Must be rigid (Steel or thick-walled PVC). Min. 10-20 meters long. |
| **Pump Body** | The Engine | Scavenge heavy-duty iron or brass tee-fittings (1" to 2" diameter). |
| **Waste Valve** | The "Clack" | A weighted, normally-open brass check valve (modified). |
| **Check Valve** | Delivery | A standard, one-way swing check valve. |
| **Pressure Vessel** | The Buffer | A small fire extinguisher tank, or a large capped pipe (min. 5L volume). |
| **Delivery Pipe** | Transit | Smaller diameter flexible or rigid pipe (e.g., 1/2" poly-pipe). |

---

## Assembly Instructions

### Step 1: Calculating the Head Ratio

Before building, ensure your site qualifies:

1. **Supply Head (h):** Measure the vertical drop from your water source to the pump location.
2. **Delivery Head (H):** Measure the vertical rise from the pump to your target tank.
3. **Rule:** The Hydram can reliably lift water to a height (H) that is **10 to 20 times** the supply head (h). (e.g., a 2 m drop can lift water 20–40 m uphill).

```text
  HEAD RATIO: ELEVATION CROSS-SECTION
  ====================================
  Delivery Tank  . . . . . . . . . . . . . . . .  +30m elevation
       [====]    :                                :
       |    | <--:-- delivery head H = 30m        :
       |    |    :    (ram to tank)                :
       [====]    :                                :
          \      :                                :
  delivery \     :                                :
  pipe      \    :                                :
  Source     \   :  +3m elevation                 :
  [~~pool~~]  \ :...|                             :
       \       \|   |                             :
  drive \   [RAM PUMP] . . . . . 0m (datum)       :
  pipe   \      :                                 :
          \_____|   supply head h = 3m            :
                :                                 :
                :   Ratio H/h = 30/3 = 10:1       :
                :   At 70% efficiency, q = 0.7*Q*h/H
                :   If Q=20 LPM: q = 0.7*20*3/30 = 1.4 LPM
```

### Step 2: Installing the Drive Pipe

1. Connect the drive pipe to your source (spring or stream).
2. Run the pipe in a straight, downward line to the pump location.
3. **Crucial:** The drive pipe must be rigid. If it flexes, the water hammer energy is lost.

### Step 3: Assembling the Pump Body

1. Connect the Drive Pipe to a heavy Iron Tee.
2. **The Waste Valve:** Mount the normally-open check valve on the bottom or side outlet of the tee. This is where water will initially spill out.
3. **The Delivery Valve:** Connect the standard check valve facing the direction of the storage tank, on the outlet opposite the drive pipe.
4. **The Pressure Vessel:** Mount your air chamber directly above or after the delivery valve. This chamber must contain trapped air to act as a shock absorber.

### Step 4: Starting and Tuning the Pump

1. Open the source water. Water will flow out of the waste valve freely.
2. **The Prime:** Use your foot to push the waste valve shut. It will pop back open as the water flow resumes.
3. **Find the Beat:** Keep pushing it shut every time it opens. You are training the system to cycle.
4. **Automatic Mode:** After several manual cycles, the valve will start clacking on its own — a sharp **"clack-THUMP, clack-THUMP"** rhythm. The clack is the waste valve slamming shut; the THUMP is the water hammer pulse hitting the delivery valve and forcing water into the air chamber.
5. **Tuning the Cycle Rate:** Adjust the weight on the waste valve until the cycle rate falls between 40 and 80 beats per minute. Too fast (>80/min) means the waste valve closes before the water column reaches full velocity — insufficient water hammer. Too slow (<40/min) means excessive water is wasted through the open valve between cycles.
6. **Measure and Optimise:** Count the delivery flow (litres per minute at the storage tank) at several different cycle rates by adding or removing weight from the waste valve. Record the results and set the valve to the rate that maximises delivery.
7. **Listen for Health:** A healthy ram produces a crisp, two-part sound on each cycle. A dull, mushy thud instead of a sharp THUMP indicates the air chamber is waterlogged and needs recharging.

---

## Visual Illustration

### Pump Body Detail

```text
SOURCE [Head 'h']
      \
       \  [ DRIVE PIPE ] (Rigid steel or Schedule 40 PVC)
        \_________________
                          |
                  [ AIR CHAMBER ] (Cushions the blow)
                  |      ^      |
                  | [ CHECK V. ]|-----> [ DELIVERY PIPE ] [Height 'H']
                  |_____________|
                          |
                  [ WASTE VALVE ] <--- The "Clack" (Water spills here)
```

### Complete System Layout (Source to Storage)

```text
  ~~ STREAM / SPRING ~~
         |
    [INTAKE SCREEN]  <-- 2mm mesh, clean weekly
         |
    [SETTLING POOL]  <-- Optional: lets silt drop out
         |
         v
    ============================================
    |          DRIVE PIPE (rigid, straight)     |
    |   Length = 5-10x supply head              |
    |   Diameter = 1.5" to 2" (40-50mm)        |
    |   Fall = supply head 'h' (1-10m)         |
    ============================================
         |
         v
    +---------------------------+
    |       PUMP BODY           |
    |   (Galvanized Iron Tee)   |
    |                           |
    |  Drive --> [TEE] --> Delivery Check Valve
    |             |              |
    |        Waste Valve    Air Chamber
    |        (weighted)    (5-10L volume)
    |             |              |
    |        Spill to        Delivery Pipe
    |        stream          (0.5-1" / 15-25mm)
    +---------------------------+
                                 |
                                 |  (rises H = 10-20x h)
                                 v
                          +-----------+
                          | STORAGE   |
                          | TANK      |
                          | (with     |
                          | overflow  |
                          | back to   |
                          | stream)   |
                          +-----------+
                                 |
                          Gravity feed to
                          settlement
```

---

## Practical Implementation

### Site Assessment for Hydram Viability

Follow this decision tree before committing materials and labour:

1. **Is there a flowing water source with more than 1 m of available fall?** If no — a hydram is not viable at this site. Consider a spring-box with gravity feed directly to the settlement if the spring is at sufficient elevation, or manual water carrying.

2. **Is the total source flow greater than 5 LPM?** If no — the flow is too low for a practical ram pump. Even at high efficiency, the delivered volume will be negligible. Consider rainwater harvesting or well-digging instead.

3. **Can a rigid pipe be run from source to pump site in a reasonably straight line?** If no — every bend in the drive pipe reduces water hammer efficiency. Keep bends to fewer than 2 total, and use long-radius sweep fittings (not sharp elbows). If the terrain forces multiple bends, reposition the pump site.

4. **Is the required delivery height less than 20 times the supply head?** If no — efficiency will be poor. Consider staging two rams: the first lifts water to an intermediate reservoir, the second lifts from there to the final elevation. Each stage must independently satisfy the 20:1 ratio.

### Sizing Calculator

The following table provides sizing guidance for common supply head values. The rule for drive pipe length: **5 to 10 times the supply head** for optimal performance.

| Supply Head (m) | Drive Pipe Length (m) | Drive Pipe Dia. (mm) | Source Flow Needed (LPM) | Delivery at 10× Head (LPM) | Delivery at 20× Head (LPM) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 5–10 | 40 | 10 | 0.7 | 0.35 |
| 2 | 10–20 | 40–50 | 15 | 1.05 | 0.53 |
| 3 | 15–30 | 50 | 20 | 1.4 | 0.7 |
| 5 | 25–50 | 50–65 | 30 | 2.1 | 1.05 |
| 10 | 50–100 | 65–80 | 50 | 3.5 | 1.75 |

*Delivery values assume 70% D'Aubuisson efficiency. Actual performance varies with pipe condition, valve quality, and installation precision. Always measure and verify after commissioning.*

### Construction from Scavenged Materials

In a post-infrastructure context, purpose-built ram pump components will not be available. The following substitutions are proven effective:

**(a) The Waste Valve** — Source a brass swing check valve from plumbing salvage (commonly found in water heater installations and commercial buildings). The stock valve will be too light to generate proper water hammer timing. Add weight to the flap by bolting a stainless steel nut and bolt (or a short length of lead pipe) to the valve disc. Start with approximately 50 g of added weight and increase until the cycle rate falls into the 40–80 beats/minute range. The valve must swing freely — test by holding it vertically and flicking the disc; it should swing open and closed with no sticking.

**(b) The Delivery Check Valve** — A standard brass spring check valve, unmodified. This valve must seal reliably under the high momentary pressures of water hammer. Inspect the rubber seat for cracks or deformation. A leaking delivery valve bleeds pressurised water back through the pump body, drastically reducing delivery volume.

**(c) The Pressure Vessel (Air Chamber)** — The ideal scavenged component is a small **fire extinguisher** (2.5–5 kg size). Discharge the contents (safely, outdoors), remove the valve assembly, and weld or thread-adapt the neck to accept your delivery pipe fitting. Alternative: a 100 mm diameter PVC pipe, 400 mm long, capped at both ends with one inlet at the bottom. The chamber must hold a minimum of 5 litres of air volume at atmospheric pressure. Larger is better — a 10 L chamber smooths delivery flow more effectively.

**(d) The Pump Body** — A galvanized iron tee fitting in 1.5" or 2" size forms the central junction. The drive pipe connects to the straight-through port. The waste valve mounts on one branch. The delivery valve and air chamber mount on the remaining branch (use a reducer if necessary). All connections must be threaded or flanged — no push-fit or compression fittings, which will fail under water hammer pressure.

**Pipe Sizing Summary:**
- Drive pipe: 1.5–2 inch (40–50 mm) internal diameter, rigid
- Delivery pipe: 0.5–1 inch (15–25 mm), can be flexible polyethylene

### Alternative Zero-Energy Water Lifting Methods

When a hydraulic ram is not viable (insufficient flow, insufficient fall, or no suitable pipe available), consider these alternatives:

**(a) The Siphon.** If the water source is higher than the delivery point but separated by a ridge, a siphon can move water over the ridge with no energy input. The inlet must be higher than the outlet. The pipe must be completely filled with water (primed) and the highest point of the pipe must be less than approximately 8 m above the water surface (the theoretical limit is 10.3 m at sea level, but dissolved gases and temperature reduce this). Siphons are maintenance-free once established but cannot lift water above the source elevation.

**(b) The Chain Pump.** A continuous loop of chain (or rope) threaded through a vertical pipe, with discs or rubber washers attached at regular intervals. As the chain is pulled upward (by hand crank or animal power), each disc traps a column of water between itself and the next disc, lifting water continuously. Output: approximately 5–15 LPM depending on pipe diameter and crank speed. Effective for lifts up to 10 m. The chain pump was the standard water-lifting device across Asia for millennia.

**(c) The Archimedes Screw.** An inclined helical screw inside a cylindrical housing. Rotating the screw (by hand crank, water wheel, or animal power) lifts water along the helix. Effective for low-lift, high-volume applications: irrigation ditches, pond filling. Practical lift: 1–5 m. Can be built from sheet metal wrapped around a wooden core.

**(d) The Noria.** A water wheel with buckets or compartments attached to its rim, powered by the current of a river. As the wheel turns, buckets scoop water at the bottom and discharge it at the top into an aqueduct. No external power required — the river itself turns the wheel. Effective for lifts equal to the wheel diameter (typically 2–8 m). Norias have been in continuous use in Syria and Spain for over 2,000 years.

---

## Common Failure Modes

1. **Flexible drive pipe.** The pump cycles audibly — you can hear the waste valve clacking — but little or no water reaches the storage tank. The water hammer energy is being absorbed by elastic deformation of the pipe wall. Replace with rigid steel or Schedule 40 PVC. Ensure all joints are rigid; a single flexible coupling in the drive line can reduce delivery by 80%.

2. **Waterlogged air chamber.** Delivery flow becomes violently pulsed, with surges and dead periods. Eventually delivery stops entirely even though the pump continues cycling. The trapped air has dissolved into the water. To fix: close the supply valve, drain the pump body completely, allow air to re-enter the chamber, then restart. Prevent recurrence by checking the air volume monthly — tap the chamber with a wrench and listen. A chamber with adequate air returns a hollow ring; a waterlogged chamber produces a dull thud.

3. **Debris in waste valve.** The pump either stops cycling or cycles weakly with poor delivery. A leaf, twig, pebble, or sediment grain is preventing the waste valve from seating fully. Each incomplete seal bleeds off the water hammer pressure. Clear the debris and install a 2 mm intake screen if not already present. In silty water, add a small settling pool upstream of the intake.

4. **Insufficient supply head.** The pump cycles erratically — sometimes catching a rhythm, sometimes stalling. If the supply head is less than 1 m, the water velocity in the drive pipe is too low to generate adequate water hammer. Solutions: extend the drive pipe to increase effective head (a longer pipe at shallow slope can work), or relocate the pump lower relative to the source. Minimum practical supply head: 1 m.

5. **Air leak in delivery line.** The pump runs and cycles normally, but water flow at the storage tank is less than calculated or absent entirely. The delivery pipe has a leak — water hammer pressure is escaping through a joint or crack rather than pushing water uphill. Test by pressurising the delivery line and applying soap solution to every joint and fitting. Bubbles indicate the leak. Tighten, re-thread, or replace the faulty section.

---

## Maintenance Guide

- **Air Buffer:** Over weeks, the air in the pressure vessel dissolves into the water under pressure (Henry's Law). If the clack becomes violent, the delivery pulses erratically, or flow stops, drain the pump body to let fresh air back into the chamber. Establish a monthly schedule for this check.
- **Valve Seating:** Inspect the waste valve seat and the delivery check valve seat quarterly. Look for scoring, pitting, or deposits that prevent a clean seal. A brass valve seat can be restored by lapping with fine valve grinding compound.
- **Intake Screen:** Clean the intake screen weekly during leaf-fall and storm seasons, monthly otherwise. A blocked screen starves the pump of water.
- **Drive Pipe Supports:** Inspect pipe supports annually. A drive pipe that has shifted or sagged introduces flexibility into the system. Re-secure any loose supports.
- **Delivery Pipe Inspection:** Walk the delivery pipe route seasonally, checking for leaks (wet spots on the ground), animal damage, or frost heave displacement.

---

## Vocabulary of the Foundation

- **Hydraulic Ram (Hydram):** A pump that uses the kinetic energy of flowing water, arrested suddenly by a closing valve, to lift a portion of that water to an elevation higher than the source. Requires no external power.
- **Water Hammer:** The pressure surge generated when a fluid in motion is forced to stop suddenly. In plumbing it is a destructive nuisance; in the ram pump it is the operating principle.
- **Joukowsky Equation:** ΔP = ρcΔV. Relates the pressure spike from water hammer to the fluid density, wave propagation speed, and velocity change. The foundational equation of ram pump physics.
- **Drive Pipe:** The rigid pipe carrying water from the source to the pump body. Functions as the kinetic energy accumulator. Must be straight, rigid, and 5–10 times the supply head in length.
- **Waste Valve:** The normally-open valve at the pump body that allows water to flow freely, building velocity in the drive pipe. When flow velocity reaches a critical speed, hydrodynamic drag on the valve disc forces it shut, triggering water hammer. Also called the impulse valve or clack valve.
- **Check Valve:** A one-way valve that permits flow in one direction only. In the ram pump, the delivery check valve opens during the water hammer pressure spike to admit pressurised water into the air chamber and delivery pipe, then closes to prevent backflow.
- **Air Chamber (Pressure Vessel):** A sealed vessel containing trapped air, mounted after the delivery check valve. Compresses during water hammer pulses (storing energy) and expands between pulses (releasing stored energy as steady flow). Essential for smooth delivery and protection of the delivery pipe from pressure cycling.
- **Supply Head:** The vertical distance (elevation difference) between the water source intake and the pump location. Determines the kinetic energy available in the drive pipe. Minimum practical value: 1 m.
- **Delivery Head:** The vertical distance from the pump to the storage tank. The useful work output of the pump. Practical maximum: 20 times the supply head.
- **D'Aubuisson Efficiency:** η = (q × H) / (Q × h). The standard efficiency metric for hydraulic ram pumps, relating the ratio of useful output power (delivery flow × delivery head) to input power (total flow × supply head). Well-built rams achieve 60–80%.
- **Siphon:** A continuous tube that moves liquid from a higher reservoir over an intermediate high point and down to a lower outlet, powered only by the weight of the liquid in the descending leg. Cannot lift water above the source elevation.
- **Noria:** A water-powered wheel with attached buckets or compartments that lifts water from a river to an aqueduct. The river current provides the motive force. An ancient technology still in use.
- **Chain Pump:** A mechanical water-lifting device consisting of an endless chain carrying discs through a vertical pipe. Manual or animal-powered. Effective for moderate lift (up to 10 m) and continuous flow.

---

## Cross-References

- [01_Rationale_and_Importance.md](01_Rationale_and_Importance.md) — gravity-fed water supply as a fundamental site selection criterion; the hydram enables sites where gravity alone cannot deliver water to the settlement elevation.
- [05_Hydrological_Analysis_and_Watershed_Math.md](05_Hydrological_Analysis_and_Watershed_Math.md) — water budget calculations determining how much water the settlement needs daily, which directly sizes the hydram delivery requirements.
- [../01_The_Journey/04_Terrestrial_Navigation/05_Geometric_Trail_Engineering.md](../01_The_Journey/04_Terrestrial_Navigation/05_Geometric_Trail_Engineering.md) — pipe routing along terrain contours follows the same geometric principles as trail engineering; slope calculation and obstacle avoidance.
- [../../Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/01_Rationale_and_Importance.md](../../Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/01_Rationale_and_Importance.md) — water quality requirements for drinking and sanitation; the hydram delivers raw source water that may still require treatment.
- [../../Outcome_5_Decadal_Resilience/09_The_Mechanics/02_Mechanical_Power.md](../../Outcome_5_Decadal_Resilience/09_The_Mechanics/02_Mechanical_Power.md) — mechanical power systems including water wheels, which share design principles with hydram installations and can supplement water-lifting capacity.

---

## Further Study

- Watt, S. B. *A Manual on the Hydraulic Ram for Pumping Water.* Intermediate Technology Development Group (ITDG) / Practical Action Publishing, 1975. The standard field manual for ram pump construction in developing contexts. Includes construction drawings and sizing tables.
- Calvert, N. G. "The Hydraulic Ram." *Proceedings of the Institution of Mechanical Engineers*, 1957. Rigorous engineering analysis of ram pump dynamics with experimental validation.
- Lansford, W. M., and Dugan, W. G. *An Analytical and Experimental Study of the Hydraulic Ram.* University of Illinois Engineering Experiment Station, Bulletin No. 326, 1941. The most thorough academic study of ram pump performance, with extensive test data across varying head ratios and pipe configurations.
- Jeffery, T. D., Thomas, T. H., Smith, A. V., Glover, P. B., and Fountain, P. D. *Hydraulic Ram Pumps: A Guide to Ram Pump Water Supply Systems.* Intermediate Technology Publications / Practical Action, 1992. Updated field guide incorporating lessons from decades of ram pump installations in Africa, Asia, and South America.
- Development Technology Unit (DTU), University of Warwick. Hydraulic ram research papers and technical reports, 1990s–2000s. Available from the DTU archive. Includes computational modelling of water hammer dynamics and optimization of valve timing.

---

## Glossary Reference

*See [../../Glossary.md](../../Glossary.md) for full definitions of:*

- **Hydraulic Ram Pump (Hydram)**
- **Water Hammer**
- **Refugia**
- **Thermal Belt**
