import os

md_content = """# Long-Term Food Preservation: Surviving the Winter

**Alignment:** Outcome 2: Absolute Biological Sovereignty

## 1. Why This Is Important (The Rationale)
Outcome 2 requires Absolute Biological Sovereignty. Growing food is only half the equation; a settlement must survive the dormant winter months when the soil yields nothing. Without industrial refrigeration, failure to preserve the autumn harvest results in decadal collapse. 

---

## 2. Zero-Energy Preservation Methods: Detailed Execution

### The Root Cellar (Geothermal Cooling)
The earth maintains a constant temperature of ~50-55°F (10-13°C) year-round once you dig below the frost line (typically 4-6 feet deep). 

**Step-by-Step Construction:**
1. **Location:** Dig a subterranean chamber on a north-facing slope (to avoid solar gain). Ensure it is above the water table to prevent flooding.
2. **Insulation:** Roof the chamber with thick logs and cover it with at least 3 feet of packed earth.
3. **Dual Ventilation (Critical):** Install a low intake pipe near the floor to pull in cool night air. Install a high exhaust pipe near the ceiling. This creates a passive thermal draft that pushes the warm, ethylene-rich air out.
4. **Storage:** Do not wash root vegetables (potatoes, carrots). The dirt protects them. Store them buried in slightly damp sand or sawdust to prevent them from shriveling. Keep them low in the cellar.
5. **Separation:** Apples emit high levels of ethylene gas as they ripen, which will cause potatoes to instantly sprout and rot. Store apples on the highest shelves near the exhaust pipe, or in a completely separate cellar.

### Lacto-Fermentation (Biological Preservation)
Before canning, humanity relied on beneficial bacteria.

**Step-by-Step Execution:**
1. **Prep:** Shred cabbage finely. Weigh the total mass of the cabbage.
2. **The Brine:** Calculate exactly 2% to 3% of the cabbage's weight in coarse, non-iodized salt.
3. **Massage:** Vigorously massage the salt into the shredded cabbage for 10 minutes until it breaks down the cell walls and creates its own liquid brine.
4. **Packing:** Pack the cabbage extremely tightly into a glass jar or ceramic crock.
5. **Submersion:** The cabbage *must* be completely submerged under its own liquid. Place a heavy "follower" (a boiled river stone or a smaller jar filled with water) on top to keep it weighed down.
6. **The Seal:** Cover with a cloth to keep bugs out but let gas escape. Leave it in a dark, cool place for 3 weeks. The *Lactobacillus* bacteria will consume the sugars, producing lactic acid which preserves the food indefinitely and prevents botulism.

### Salt-Curing and Smoking (Meat Preservation)
Meat spoils rapidly due to bacterial action. Moisture and oxygen must be removed.

**Step-by-Step Execution:**
1. **Dry Curing:** Slice meat thin. Pack it in a wooden box entirely surrounded by coarse salt for several days. The salt draws out the moisture via osmosis, denying bacteria the water they need to reproduce.
2. **Cold Smoking:** Build a small teepee or wooden shack. Hang the salted meat near the ceiling.
3. **The Smolder:** Build a small fire using hardwood (hickory or apple, never pine). Smother the fire with slightly damp sawdust so it produces heavy smoke but *zero flame*. 
4. **The Cure:** Keep the shack filled with dense smoke for 3-5 days. The smoke contains phenols and formaldehydes that act as an anti-microbial barrier on the surface of the meat.

---

## 🔬 Scientific Validation & Research Context
*   **Lactic Acid Efficacy:** Microbiological studies confirm that a pH level below 4.6 (achieved via lacto-fermentation) completely inhibits the growth of *Clostridium botulinum*, the bacteria responsible for fatal botulism.
*   **Ethylene Management:** Agricultural science validates that storing ethylene-producing crops (like apples) next to ethylene-sensitive crops (like potatoes) causes rapid sprouting and rot. A root cellar's dual-vent system physically purges this hormone from the storage environment.

---
## 🚀 Practical Implementation Guide for Beginners

### 1. Step-by-Step Action Plan
*   **Phase 1: The Prototype Cellar:** Do not dig a massive room. Dig a 4-foot deep hole, place an old chest freezer or heavy-duty trash can inside, and cover it with a thick layer of straw and dirt. Test if it keeps root vegetables from freezing during the first winter.
*   **Phase 2: The First Ferment:** Shred a head of cabbage, weigh it, and massage exactly 2% of its weight in salt into it until it creates its own liquid. Pack it tightly in a glass jar, ensuring it is completely submerged. Wait 3 weeks.
*   **Phase 3: The Smokehouse:** Build a small teepee of branches, cover it in a tarp (leaving a small top vent), and maintain a slow-smoldering hickory fire underneath strips of salted meat for 3-5 days.

### 2. Troubleshooting & Failure Modes
*   **Fermentation Mold:** If fuzzy mold grows on the top of your fermentation jar, the vegetables were exposed to oxygen. Skim the mold off, ensuring the food beneath the brine is safe, and add a heavy "follower" (like a boiled rock) to keep everything submerged.
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>01 Long-Term Food Preservation - Module 06 - Project Aadhiyandham</title>
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
        <h1>Long-Term Food Preservation: Surviving the Winter</h1>
        <p class="alignment" style="color: #2c3e50; font-weight: bold; background-color: #e8f4f8; padding: 5px 10px; border-radius: 4px; display: inline-block;">Alignment: Outcome 2: Absolute Biological Sovereignty</p>
    </header>

    <div class="breadcrumbs"><a href="../../index.html">Index</a> &gt; <a href="../01_Rationale_and_Importance.html">06 The Ecosystem</a> &gt; <span>Food Preservation</span></div>

    <section>
        <h2>1. Why This Is Important (The Rationale)</h2>
        <p>Outcome 2 requires Absolute Biological Sovereignty. Growing food is only half the equation; a settlement must survive the dormant winter months when the soil yields nothing. Without industrial refrigeration, failure to preserve the autumn harvest results in decadal collapse.</p>

        <hr>

        <h2>2. Zero-Energy Preservation Methods: Detailed Execution</h2>

        <div class="how-to">
            <h3>The Root Cellar (Geothermal Cooling)</h3>
            <p>The earth maintains a constant temperature of ~50-55°F (10-13°C) year-round once you dig below the frost line (typically 4-6 feet deep).</p>

            <div class="diagram-container">
                <h3>High-Resolution Diagram: Dual-Vent Geothermal Root Cellar</h3>
                <svg width="600" height="400" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
                    <!-- Sky and Ground Surface -->
                    <rect x="0" y="0" width="600" height="150" fill="#e0f7fa"/>
                    <path d="M 0 150 L 200 150 L 350 50 L 600 50 L 600 400 L 0 400 Z" fill="#8d6e63"/>
                    
                    <!-- Frost Line -->
                    <line x1="0" y1="200" x2="600" y2="200" stroke="#fff" stroke-width="2" stroke-dasharray="10,5"/>
                    <text x="10" y="195" font-size="12" fill="#fff" font-weight="bold">Frost Line (approx 4ft)</text>
                    
                    <!-- Subterranean Chamber -->
                    <rect x="250" y="180" width="300" height="180" fill="#f4e1d2" stroke="#5d4037" stroke-width="6"/>
                    <rect x="250" y="150" width="300" height="30" fill="#795548"/> <!-- Heavy Timber Roof -->
                    <text x="350" y="170" font-size="14" fill="#fff" font-weight="bold">Timber Roof + 3ft Earth</text>
                    
                    <!-- Shelves and Produce -->
                    <line x1="250" y1="220" x2="400" y2="220" stroke="#5d4037" stroke-width="4"/> <!-- Top Shelf -->
                    <circle cx="280" cy="210" r="8" fill="#d32f2f"/> <!-- Apples -->
                    <circle cx="300" cy="210" r="8" fill="#d32f2f"/>
                    <text x="260" y="200" font-size="10" font-weight="bold">Apples (Ethylene producers)</text>
                    
                    <line x1="250" y1="300" x2="400" y2="300" stroke="#5d4037" stroke-width="4"/> <!-- Bottom Shelf -->
                    <rect x="260" y="280" width="40" height="20" fill="#a1887f"/> <!-- Sand Box -->
                    <circle cx="280" cy="280" r="5" fill="#fbc02d"/> <!-- Potatoes -->
                    <text x="260" y="270" font-size="10" font-weight="bold">Potatoes in damp sand</text>
                    
                    <!-- Dual Ventilation System -->
                    <!-- Intake Pipe (Low) -->
                    <rect x="180" y="120" width="20" height="220" fill="#90a4ae"/>
                    <polygon points="180,120 200,120 190,100" fill="#90a4ae"/> <!-- Hood -->
                    <rect x="200" y="320" width="50" height="20" fill="#90a4ae"/> <!-- Pipe entering room -->
                    
                    <path d="M 170 80 Q 190 100 170 120" fill="none" stroke="#2196F3" stroke-width="3" marker-end="url(#arrow-blue)"/>
                    <text x="30" y="110" font-size="12" font-weight="bold" fill="#2196F3">Cold Air Intake (Sinks)</text>
                    
                    <!-- Exhaust Pipe (High) -->
                    <rect x="500" y="30" width="20" height="150" fill="#90a4ae"/>
                    <polygon points="500,30 520,30 510,10" fill="#90a4ae"/> <!-- Hood -->
                    
                    <path d="M 490 200 Q 510 160 510 100" fill="none" stroke="#e67e22" stroke-width="3" marker-end="url(#arrow-orange)"/>
                    <text x="530" y="80" font-size="12" font-weight="bold" fill="#e67e22">Warm Air / Ethylene Exhaust</text>

                    <!-- Core Temperature Label -->
                    <text x="380" y="280" font-size="20" font-weight="bold" fill="#3e2723">Constant 55°F</text>

                    <defs>
                        <marker id="arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#2196F3" />
                        </marker>
                        <marker id="arrow-orange" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#e67e22" />
                        </marker>
                    </defs>
                </svg>
            </div>

            <div class="instruction-step"><strong>Step 1 (Location):</strong> Dig a subterranean chamber on a north-facing slope to avoid solar gain.</div>
            <div class="instruction-step"><strong>Step 2 (Insulation):</strong> Roof the chamber with thick logs and cover it with at least 3 feet of packed earth.</div>
            <div class="instruction-step"><strong>Step 3 (Dual Ventilation - CRITICAL):</strong> Install a low intake pipe near the floor for cool air, and a high exhaust pipe near the ceiling for warm air and ethylene gas.</div>
            <div class="instruction-step"><strong>Step 4 (Storage):</strong> Do not wash root vegetables. Store them buried in damp sand on lower shelves.</div>
            <div class="instruction-step"><strong>Step 5 (Separation):</strong> Store apples (high ethylene emitters) on the highest shelves near the exhaust pipe, far from potatoes.</div>
        </div>

        <div class="how-to">
            <h3>Lacto-Fermentation (Biological Preservation)</h3>
            <p>Before canning, humanity relied on beneficial bacteria.</p>
            <div class="instruction-step"><strong>Step 1 (Prep):</strong> Shred cabbage finely. Weigh the total mass.</div>
            <div class="instruction-step"><strong>Step 2 (The Brine):</strong> Calculate exactly 2% to 3% of the cabbage's weight in coarse, non-iodized salt.</div>
            <div class="instruction-step"><strong>Step 3 (Massage):</strong> Vigorously massage the salt into the cabbage for 10 minutes until it creates its own liquid brine.</div>
            <div class="instruction-step"><strong>Step 4 (Submersion - CRITICAL):</strong> Pack tightly into a jar. The cabbage <em>must</em> be completely submerged under its own liquid. Use a weight to keep it down.</div>
            <div class="instruction-step"><strong>Step 5 (The Seal):</strong> Cover with a breathable cloth and store in a cool, dark place for 3 weeks to allow lactic acid to form.</div>
        </div>

        <div class="how-to">
            <h3>Salt-Curing and Smoking (Meat Preservation)</h3>
            <div class="instruction-step"><strong>Step 1 (Dry Curing):</strong> Slice meat thin and pack it completely surrounded by coarse salt to draw out moisture.</div>
            <div class="instruction-step"><strong>Step 2 (The Smolder):</strong> Build a slow, smoldering fire using hardwood (hickory/apple). <em>Zero flame allowed</em>.</div>
            <div class="instruction-step"><strong>Step 3 (The Cure):</strong> Hang the salted meat in a shack filled with dense smoke for 3-5 days to create an anti-microbial barrier.</div>
        </div>

        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <ul>
                <li><strong>Lactic Acid Efficacy:</strong> Microbiological studies confirm that a pH level below 4.6 (achieved via lacto-fermentation) completely inhibits the growth of <em>Clostridium botulinum</em>, the bacteria responsible for fatal botulism.</li>
                <li><strong>Ethylene Management:</strong> Agricultural science validates that storing ethylene-producing crops (like apples) next to ethylene-sensitive crops (like potatoes) causes rapid sprouting and rot. A root cellar's dual-vent system physically purges this hormone from the storage environment.</li>
            </ul>
        </div>

        <div class="practical-guide" style="margin: 2em 0; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
            <h2>🚀 Practical Implementation Guide for Beginners</h2>
            <h3>1. Step-by-Step Action Plan</h3>
            <ul>
                <li><strong>Phase 1: The Prototype Cellar:</strong> Do not dig a massive room. Dig a 4-foot deep hole, place an old chest freezer or heavy-duty trash can inside, and cover it with a thick layer of straw and dirt. Test if it keeps root vegetables from freezing during the first winter.</li>
                <li><strong>Phase 2: The First Ferment:</strong> Shred a head of cabbage, weigh it, and massage exactly 2% of its weight in salt into it until it creates its own liquid. Pack it tightly in a glass jar, ensuring it is completely submerged. Wait 3 weeks.</li>
                <li><strong>Phase 3: The Smokehouse:</strong> Build a small teepee of branches, cover it in a tarp (leaving a small top vent), and maintain a slow-smoldering hickory fire underneath strips of salted meat for 3-5 days.</li>
            </ul>
            <h3>2. Troubleshooting & Failure Modes</h3>
            <ul>
                <li><strong>Fermentation Mold:</strong> If fuzzy mold grows on the top of your fermentation jar, the vegetables were exposed to oxygen. Skim the mold off, ensuring the food beneath the brine is safe, and add a heavy "follower" (like a boiled rock) to keep everything submerged.</li>
            </ul>
        </div>

    </section>

    <div class="nav">
        <span>Previous: <a href="../04_Livestock_and_Mechanical_Animals.html">04 Livestock</a></span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

with open("06_The_Ecosystem/05_Food_Preservation/01_Long_Term_Preservation.md", "w", encoding="utf-8") as f:
    f.write(md_content)

with open("html/06_The_Ecosystem/05_Food_Preservation/01_Long_Term_Preservation.html", "w", encoding="utf-8") as f:
    f.write(html_content)
