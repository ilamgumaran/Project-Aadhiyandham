import os

md_content = """# Advanced Structural Engineering: Post-Scavenge Construction

**Alignment:** Outcome 5: Decadal and Generational Resilience

## 1. Why This Is Important (The Rationale)
Outcome 5 establishes Decadal and Generational Resilience. In the early years of a settlement, construction relies heavily on scavenged modern materials (plywood, steel nails, asphalt shingles). However, within 20 years, these materials will degrade and the "Recycling Cliff" will hit. True structural resilience means the ability to build permanent, weather-proof, multi-story buildings using only local geology and biology. 

---

## 2. Zero-Tech Fasteners: Timber Framing
The reliance on modern iron nails is a vulnerability. When the nails rust, the building falls.

### The Mortise and Tenon Joint
This is the foundational joint of generational building, requiring zero metal.

**Step-by-Step Execution:**
1. **The Tenon (The Peg):** On the end of your first beam, use a cross-cut saw to cut a shoulder, and a chisel to remove the cheek wood, leaving a protruding rectangular "peg" exactly in the center.
2. **The Mortise (The Hole):** On your second beam, trace the exact dimensions of your Tenon. Use a hand-auger (brace and bit) to drill out the majority of the wood inside the traced rectangle. Use a chisel to square the corners until the hole is perfectly clean.
3. **The Test Fit:** Insert the Tenon into the Mortise. It should be a friction fit, requiring light taps from a wooden mallet to seat fully.
4. **Draw-Boring (The Lock):** Pull the joint apart. Drill a 1-inch hole completely through the Mortise cheeks. Insert the Tenon back in, and stick an awl through the hole to mark where it hits the Tenon. Pull the Tenon out, and drill its hole *slightly closer* to the shoulder (about 1/8th of an inch).
5. **The Trunnel (Tree-Nail):** Carve a hardwood peg (oak or hickory) that is completely dry. Drive it through the offset holes. As the peg fights through the misaligned holes, it physically yanks the two beams together with massive force, locking them permanently.

---

## 3. Permanent Masonry: Fired Brick and Lime Mortar
Mud and wattle melt in heavy rain. For permanent civil infrastructure (forges, granaries, aqueducts), masonry is required.

### Firing Clay Bricks (The Clamp Kiln)
You do not need a pre-existing brick oven to fire bricks; you build the oven *out* of the bricks you are firing.

**Step-by-Step Execution:**
1. **The Mix:** Dig subsoil rich in clay. Mix it with sand (to prevent shrinkage) and water until it holds its shape. Press it into wooden molds (9x4x2 inches).
2. **Air Drying (Critical):** Stack the raw bricks in the shade for at least 3 weeks. If you fire a wet brick, the trapped water turns to steam and explodes like a grenade.
3. **Building the Clamp:** On flat ground, build a solid foundation of fired bricks (or stone). Stack your raw, dry bricks in a large pyramid. Leave several 2-foot wide tunnels running completely through the base of the pyramid.
4. **The Casing:** Cover the entire exterior of the pyramid with mud to insulate it and trap the heat.
5. **The Firing:** Fill the base tunnels with hardwood and light them. You must maintain this fire continuously for 3 to 5 days, reaching internal temperatures of ~1000°C (1800°F).
6. **Cooling:** Do not open the clamp immediately. Let it cool slowly for a week to prevent the ceramic from cracking due to thermal shock. 

### Creating Lime Mortar
**Step-by-Step Chemistry:**
1. **The Burn:** Heat limestone rocks (Calcium Carbonate) in a kiln at 900°C to drive off the CO2, creating caustic Quicklime.
2. **Slaking:** Drop the Quicklime into water (wear goggles). It will boil violently. The resulting paste is Slaked Lime.
3. **The Mix:** Mix 1 part Slaked Lime with 3 parts sharp sand. Use it to lay your fired bricks. The mortar will absorb CO2 from the air over the next 6 months, turning back into solid limestone.

---

## 🔬 Scientific Validation & Research Context
*   **Thermal Expansion Coefficients:** Engineering studies validate that using iron fasteners in green wood causes "nail sickness." The iron rusts due to the tannic acid in the wood, and the differing thermal expansion rates cause the wood around the nail to rot. Timber framing relies on uniform organic materials expanding at the exact same rate.
*   **The Lime Cycle:** The chemical equation for lime mortar (`Ca(OH)2 + CO2 -> CaCO3 + H2O`) proves that the mortar literally absorbs atmospheric carbon to become stone. It is structurally superior to modern cement for historical masonry because it is permeable; it allows moisture to escape rather than trapping it inside the wall where it can freeze and shatter the brick.

---
## 🚀 Practical Implementation Guide for Beginners

### 1. Step-by-Step Action Plan
*   **Phase 1: The Joinery Prototype:** Do not build a house first. Cut a 4x4 beam. Attempt to carve a basic Mortise and Tenon joint and secure it with a wooden peg. If you cannot make a tight joint on the ground, you cannot make it 10 feet in the air.
*   **Phase 2: The Lime Burn:** Locate local limestone, chalk, or sea shells. Build a small, very hot hardwood fire and burn the shells for 12 hours. Carefully drop the white, calcined shells into a bucket of water (wear eye protection, it will boil violently). You have just made slaked lime.

### 2. Troubleshooting & Failure Modes
*   **Exploding Bricks:** If your bricks explode inside the clamp kiln, they were not completely dry before firing. The internal moisture turned to steam and ruptured the ceramic. Dry them in the shade for two additional weeks next time.
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>01 Advanced Structural Engineering - Module 07 - Project Aadhiyandham</title>
    <link rel="stylesheet" href="../../style.css">
    <style>
        .diagram-container {
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
        }
        .diagram-container svg {
            max-width: 100%;
            height: auto;
        }
        .instruction-step {
            margin-bottom: 15px;
            padding-left: 15px;
            border-left: 3px solid #2ecc71;
        }
    </style>
</head>
<body>
    <header>
        <p><a href="../../index.html">Main Index</a></p>
        <h1>Advanced Structural Engineering: Post-Scavenge Construction</h1>
        <p class="alignment" style="color: #2c3e50; font-weight: bold; background-color: #e8f4f8; padding: 5px 10px; border-radius: 4px; display: inline-block;">Alignment: Outcome 5: Decadal and Generational Resilience</p>
    </header>

    <div class="breadcrumbs"><a href="../../index.html">Index</a> &gt; <a href="../01_Rationale_and_Importance.html">07 The Mechanics</a> &gt; <span>Advanced Structural Engineering</span></div>

    <section>
        <h2>1. Why This Is Important (The Rationale)</h2>
        <p>Outcome 5 establishes Decadal and Generational Resilience. In the early years of a settlement, construction relies heavily on scavenged modern materials (plywood, steel nails, asphalt shingles). However, within 20 years, these materials will degrade and the "Recycling Cliff" will hit. True structural resilience means the ability to build permanent, weather-proof, multi-story buildings using only local geology and biology.</p>

        <hr>

        <h2>2. Zero-Tech Fasteners: Timber Framing</h2>
        <p>The reliance on modern iron nails is a vulnerability. When the nails rust, the building falls.</p>
        
        <div class="how-to">
            <h3>The Mortise and Tenon Joint</h3>
            <p>This is the foundational joint of generational building, requiring zero metal.</p>

            <div class="diagram-container">
                <h3>High-Resolution Diagram: Mortise and Tenon (Draw-Bored)</h3>
                <svg width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
                    <!-- Tenon Beam (Left) -->
                    <rect x="50" y="100" width="150" height="100" fill="#d7ccc8" stroke="#8d6e63" stroke-width="2"/>
                    <rect x="200" y="125" width="80" height="50" fill="#a1887f" stroke="#5d4037" stroke-width="2"/>
                    <text x="70" y="155" font-size="14" font-weight="bold">Beam A</text>
                    <text x="210" y="155" font-size="12" fill="#fff" font-weight="bold">TENON</text>
                    
                    <!-- Offset Hole in Tenon -->
                    <circle cx="250" cy="150" r="10" fill="#fff" stroke="#d32f2f" stroke-width="2" stroke-dasharray="4,2"/>
                    <line x1="250" y1="180" x2="250" y2="220" stroke="#d32f2f" stroke-width="2"/>
                    <text x="180" y="240" font-size="12" fill="#d32f2f" font-weight="bold">Offset Hole (Draw-bore)</text>

                    <!-- Mortise Beam (Right) -->
                    <rect x="350" y="50" width="100" height="200" fill="#d7ccc8" stroke="#8d6e63" stroke-width="2"/>
                    <rect x="350" y="125" width="40" height="50" fill="#5d4037" />
                    <text x="360" y="270" font-size="14" font-weight="bold">Beam B</text>
                    <text x="360" y="115" font-size="12" font-weight="bold">MORTISE</text>
                    
                    <!-- Peg Hole in Mortise -->
                    <circle cx="370" cy="150" r="10" fill="none" stroke="#2c3e50" stroke-width="2"/>
                    
                    <!-- Trunnel (Peg) -->
                    <rect x="365" y="10" width="10" height="60" fill="#795548" rx="2"/>
                    <polygon points="365,70 375,70 370,80" fill="#795548"/>
                    <text x="385" y="40" font-size="12" font-weight="bold">Trunnel (Peg)</text>
                    
                    <!-- Assembly Arrows -->
                    <path d="M 290 150 L 330 150" fill="none" stroke="#e67e22" stroke-width="4" marker-end="url(#arrow)"/>
                    <path d="M 370 90 L 370 120" fill="none" stroke="#e67e22" stroke-width="4" marker-end="url(#arrow)"/>
                    
                    <defs>
                        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#e67e22" />
                        </marker>
                    </defs>
                </svg>
            </div>

            <div class="instruction-step"><strong>Step 1 (The Tenon):</strong> On the end of your first beam, cut a shoulder and remove the cheek wood to leave a protruding rectangular "peg" perfectly in the center.</div>
            <div class="instruction-step"><strong>Step 2 (The Mortise):</strong> Trace the Tenon onto the second beam. Drill out the core wood using a hand-auger, then square the corners with a chisel.</div>
            <div class="instruction-step"><strong>Step 3 (The Test Fit):</strong> Insert the Tenon into the Mortise. It should be a tight friction fit.</div>
            <div class="instruction-step"><strong>Step 4 (Draw-Boring):</strong> Drill a hole through the Mortise. Insert the Tenon, mark the hole, pull it out, and drill the Tenon's hole 1/8th inch <em>closer to its shoulder</em>.</div>
            <div class="instruction-step"><strong>Step 5 (The Trunnel):</strong> Drive a dry hardwood peg through the misaligned holes. The offset physically yanks the two beams together with massive force.</div>
        </div>

        <hr>

        <h2>3. Permanent Masonry: Fired Brick and Lime Mortar</h2>
        <p>Mud and wattle melt in heavy rain. For permanent civil infrastructure (forges, granaries, aqueducts), masonry is required.</p>

        <div class="how-to">
            <h3>Firing Clay Bricks (The Clamp Kiln)</h3>
            <p>You do not need a pre-existing brick oven to fire bricks; you build the oven <em>out</em> of the bricks you are firing.</p>
            
            <div class="diagram-container">
                <h3>High-Resolution Diagram: The Clamp Kiln</h3>
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg">
                    <!-- Ground -->
                    <rect x="0" y="200" width="600" height="50" fill="#795548"/>
                    
                    <!-- Fire Tunnels -->
                    <path d="M 150 200 A 30 50 0 0 1 210 200 Z" fill="#212121"/>
                    <polygon points="160,200 200,200 180,160" fill="#e67e22"/> <!-- Fire -->
                    
                    <path d="M 270 200 A 30 50 0 0 1 330 200 Z" fill="#212121"/>
                    <polygon points="280,200 320,200 300,160" fill="#e67e22"/> <!-- Fire -->
                    
                    <path d="M 390 200 A 30 50 0 0 1 450 200 Z" fill="#212121"/>
                    <polygon points="400,200 440,200 420,160" fill="#e67e22"/> <!-- Fire -->
                    
                    <!-- Brick Pyramid (Clamp) -->
                    <polygon points="100,200 500,200 300,50" fill="none" stroke="#d32f2f" stroke-width="4"/>
                    <path d="M 120 180 L 480 180 M 140 160 L 460 160 M 160 140 L 440 140 M 180 120 L 420 120 M 200 100 L 400 100" stroke="#d32f2f" stroke-width="2" stroke-dasharray="10,5"/>
                    
                    <!-- Mud Casing -->
                    <path d="M 90 200 L 300 40 L 510 200" fill="none" stroke="#8d6e63" stroke-width="10"/>
                    <text x="310" y="80" font-size="12" font-weight="bold" fill="#5d4037">Insulating Mud Casing</text>
                    
                    <!-- Labels -->
                    <line x1="210" y1="180" x2="250" y2="150" stroke="#333" stroke-width="2"/>
                    <text x="260" y="145" font-size="14" font-weight="bold">Raw, Dry Bricks</text>
                    
                    <line x1="420" y1="180" x2="480" y2="150" stroke="#333" stroke-width="2"/>
                    <text x="490" y="145" font-size="14" font-weight="bold">Fire Tunnel (Wood)</text>
                </svg>
            </div>

            <div class="instruction-step"><strong>Step 1 (The Mix):</strong> Dig subsoil rich in clay. Mix with sand and water. Press into wooden molds (9x4x2 inches).</div>
            <div class="instruction-step"><strong>Step 2 (Air Drying - CRITICAL):</strong> Stack the raw bricks in the shade for at least 3 weeks. If you fire a wet brick, it explodes like a grenade.</div>
            <div class="instruction-step"><strong>Step 3 (Building the Clamp):</strong> Stack your raw, dry bricks in a large pyramid on a flat surface, leaving 2-foot wide tunnels running through the base.</div>
            <div class="instruction-step"><strong>Step 4 (The Casing):</strong> Cover the entire exterior of the pyramid with mud to insulate it and trap the heat.</div>
            <div class="instruction-step"><strong>Step 5 (The Firing):</strong> Fill the base tunnels with hardwood and light them. Maintain this fire continuously for 3 to 5 days to reach ~1000°C.</div>
            <div class="instruction-step"><strong>Step 6 (Cooling):</strong> Let it cool slowly for a week to prevent the ceramic from cracking due to thermal shock.</div>
        </div>

        <div class="how-to">
            <h3>Creating Lime Mortar</h3>
            <div class="instruction-step"><strong>Step 1 (The Burn):</strong> Heat limestone rocks in a kiln at 900°C to drive off CO2, creating caustic Quicklime.</div>
            <div class="instruction-step"><strong>Step 2 (Slaking):</strong> Drop Quicklime into water (wear goggles). The resulting paste is Slaked Lime.</div>
            <div class="instruction-step"><strong>Step 3 (The Mix):</strong> Mix 1 part Slaked Lime with 3 parts sharp sand. The mortar will absorb CO2 over 6 months, turning back into solid limestone.</div>
        </div>

        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <ul>
                <li><strong>Thermal Expansion Coefficients:</strong> Engineering studies validate that using iron fasteners in green wood causes "nail sickness." The iron rusts due to the tannic acid in the wood, and the differing thermal expansion rates cause the wood around the nail to rot. Timber framing relies on uniform organic materials expanding at the exact same rate.</li>
                <li><strong>The Lime Cycle:</strong> The chemical equation for lime mortar (<code>Ca(OH)2 + CO2 -> CaCO3 + H2O</code>) proves that the mortar literally absorbs atmospheric carbon to become stone. It is structurally superior to modern cement for historical masonry because it is permeable; it allows moisture to escape rather than trapping it inside the wall where it can freeze and shatter the brick.</li>
            </ul>
        </div>

        <div class="practical-guide" style="margin: 2em 0; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
            <h2>🚀 Practical Implementation Guide for Beginners</h2>
            <h3>1. Step-by-Step Action Plan</h3>
            <ul>
                <li><strong>Phase 1: The Joinery Prototype:</strong> Do not build a house first. Cut a 4x4 beam. Attempt to carve a basic Mortise and Tenon joint and secure it with a wooden peg. If you cannot make a tight joint on the ground, you cannot make it 10 feet in the air.</li>
                <li><strong>Phase 2: The Lime Burn:</strong> Locate local limestone, chalk, or sea shells. Build a small, very hot hardwood fire and burn the shells for 12 hours. Carefully drop the white, calcined shells into a bucket of water (wear eye protection, it will boil violently). You have just made slaked lime.</li>
            </ul>
            <h3>2. Troubleshooting & Failure Modes</h3>
            <ul>
                <li><strong>Exploding Bricks:</strong> If your bricks explode inside the clamp kiln, they were not completely dry before firing. The internal moisture turned to steam and ruptured the ceramic. Dry them in the shade for two additional weeks next time.</li>
            </ul>
        </div>

    </section>

    <div class="nav">
        <span>Previous: <a href="../05_Textiles_and_Leather/01_Textile_Synthesis.html">05 Textiles and Leather</a></span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

with open("07_The_Mechanics/06_Advanced_Structural_Engineering/01_Structural_Engineering.md", "w", encoding="utf-8") as f:
    f.write(md_content)

with open("html/07_The_Mechanics/06_Advanced_Structural_Engineering/01_Structural_Engineering.html", "w", encoding="utf-8") as f:
    f.write(html_content)
