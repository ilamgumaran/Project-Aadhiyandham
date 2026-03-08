import os

md_content = """# Advanced Trauma Care and Midwifery: Zero-Tech Medical Protocols

**Alignment:** Outcome 2: Absolute Biological Sovereignty

## 1. Why This Is Important (The Rationale)
Outcome 2 requires Absolute Biological Sovereignty. While the "Temperate Antibiotic Kit" addresses baseline infection and illness, a settlement will inevitably face acute physical trauma. Without a functional industrial hospital, the inability to set a broken bone, stop arterial bleeding, or safely deliver a child turns an accident into a generational tragedy. 

---

## 2. Advanced Trauma Protocols: Detailed Execution

### 1. Hemorrhage Control (The Windlass Tourniquet)
In zero-tech environments, massive blood loss is the primary cause of preventable death. An improvised cloth is not enough; you must establish mechanical advantage.

**Step-by-Step Application:**
1. **Identify the Bleed:** Bright red, spurting blood indicates arterial bleeding. Dark, steadily flowing blood is venous. Both can be fatal if not stopped within 2-3 minutes.
2. **Fabric Selection:** Find a strong piece of fabric (canvas, leather belt, or a folded triangular bandage) at least 2 inches wide. *Never use thin wire, paracord, or shoelaces*, as they will cut through the skin and cause nerve damage before stopping the blood flow.
3. **Placement (High and Tight):** Wrap the fabric around the limb *above* the wound. If you cannot see the exact source of the bleed through clothing, place the tourniquet as high up the limb as possible (upper thigh or armpit).
4. **The Half-Knot:** Tie a simple half-knot over the top of the limb.
5. **The Windlass:** Place a strong, rigid stick (hardwood, metal wrench, or thick tool handle) over the half-knot, and tie a square knot *over* the stick to secure it.
6. **The Twist:** Begin twisting the stick. This mechanically shortens the fabric, crushing the muscle tissue against the bone to pinch the severed artery closed. Twist until the bleeding stops completely. 
7. **Secure the Windlass:** Tie the ends of the stick down to the limb using another strip of cloth so it cannot unwind.
8. **Time:** Write the exact time of application on the patient's forehead (e.g., "TQ 14:30") using blood, dirt, or a marker. Tissue necrosis begins after 2 hours.

### 2. Orthopedic Stabilization (The Traction Splint)
A fractured femur can sever the femoral artery if the bone shifts. The massive thigh muscles will immediately spasm, pulling the jagged bone ends over each other. 

**Step-by-Step Application:**
1. **Manual Traction:** Have the strongest person available grasp the patient's ankle and steadily, firmly pull the leg straight down, aligning it with the healthy leg. This is excruciating but necessary. *Do not release this pull until the splint is fully secured.*
2. **Measure the Splints:** Find two sturdy branches or planks. The outside splint should reach from the armpit to past the foot. The inside splint should reach from the groin to past the foot.
3. **Padding:** Pad the rigid splints with clothing, moss, or leaves, especially around bony prominences (knees, ankles).
4. **Binding:** Using cloth strips, tie the splints to the leg at four points: (1) Ankle, (2) Below the knee, (3) Above the knee, (4) Thigh/Groin. *Never tie a knot directly over the break itself.*

---

## 3. Midwifery and Childbirth
The continuation of the settlement depends entirely on the safe delivery of the next generation without surgical intervention.

**Step-by-Step Execution:**
1. **The Gravity Position:** The mother should not lie flat on her back. Midwifery in a refugia relies on gravity. Utilize a squatting, kneeling, or supported-standing position. This opens the pelvic outlet by an additional 20-30%.
2. **Catching, Not Pulling:** As the infant crowns, the midwife should support the perineum with a warm, damp cloth to prevent tearing, and simply support the baby's head as it emerges. *Never pull the infant.*
3. **The Golden Hour:** Immediately after birth, before cleaning, place the infant skin-to-skin on the mother's bare chest and cover them both. This regulates the infant's heart rate, stabilizes their body temperature, and introduces them to the mother's biome.
4. **Delayed Cord Clamping:** Do not cut the umbilical cord immediately. Wait until it turns white and stops pulsing (usually 3-5 minutes). This allows up to 30% of the infant's total blood volume to transfer from the placenta, preventing neonatal anemia.
5. **Sterile Cutting:** Tie off the cord tightly in two places using boiled string, and cut *between* the ties using a flame-sterilized blade. 

---

## 🔬 Scientific Validation & Research Context
*   **The Windlass Tourniquet:** Research from the Committee on Tactical Combat Casualty Care (CoTCCC) validates that improvised tourniquets without a mechanical windlass fail to achieve complete arterial occlusion in over 90% of cases, leading to a false sense of security and death by slow hemorrhage.
*   **Delayed Cord Clamping:** The World Health Organization (WHO) explicitly recommends delayed cord clamping (1-3 minutes minimum) for all births to improve maternal and infant health and nutrition outcomes.

---
## 🚀 Practical Implementation Guide for Beginners

### 1. Step-by-Step Action Plan
*   **Phase 1: The Trauma Kit:** Assemble a dedicated zero-tech trauma bag today. It must contain: 2x commercially made windlass tourniquets (do not improvise these unless forced), 10 yards of compressed cotton gauze, and heavy-duty trauma shears.
*   **Phase 2: The Drill:** Conduct a mock drill. Have a community member simulate a severe leg wound. Time how long it takes for a responder to apply the tourniquet and achieve mechanical tightness. If it takes longer than 60 seconds, the drill is a failure.

### 2. Troubleshooting & Failure Modes
*   **Infection Post-Trauma:** If a wound is packed to stop bleeding, the gauze *must* be removed and the wound irrigated with sterilized (boiled) water within 24 hours. Leaving bloody gauze in a deep cavity guarantees systemic sepsis.
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>01 Advanced Trauma and Midwifery - Module 04 - Project Aadhiyandham</title>
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
        <h1>Advanced Trauma Care and Midwifery: Zero-Tech Medical Protocols</h1>
        <p class="alignment" style="color: #2c3e50; font-weight: bold; background-color: #e8f4f8; padding: 5px 10px; border-radius: 4px; display: inline-block;">Alignment: Outcome 2: Absolute Biological Sovereignty</p>
    </header>

    <div class="breadcrumbs"><a href="../../index.html">Index</a> &gt; <a href="../01_Rationale_and_Importance.html">04 The Body</a> &gt; <span>Trauma and Midwifery</span></div>

    <section>
        <h2>1. Why This Is Important (The Rationale)</h2>
        <p>Outcome 2 requires Absolute Biological Sovereignty. While the "Temperate Antibiotic Kit" addresses baseline infection and illness, a settlement will inevitably face acute physical trauma. Without a functional industrial hospital, the inability to set a broken bone, stop arterial bleeding, or safely deliver a child turns an accident into a generational tragedy.</p>

        <hr>

        <h2>2. Advanced Trauma Protocols: Detailed Execution</h2>

        <div class="how-to">
            <h3>1. Hemorrhage Control (The Windlass Tourniquet)</h3>
            <p>In zero-tech environments, massive blood loss is the primary cause of preventable death. An improvised cloth is not enough; you must establish mechanical advantage.</p>
            
            <div class="diagram-container">
                <h3>High-Resolution Diagram: Windlass Tourniquet Mechanics</h3>
                <svg width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
                    <!-- Leg -->
                    <path d="M 100 150 Q 300 130 500 150 Q 500 250 300 250 Q 100 250 100 150 Z" fill="#fcdbb6" stroke="#e0b894" stroke-width="2"/>
                    <text x="120" y="140" font-size="14" font-weight="bold" fill="#555">Upper Thigh</text>
                    
                    <!-- Bleed -->
                    <circle cx="450" cy="200" r="10" fill="#d32f2f"/>
                    <path d="M 450 200 L 480 180 M 450 200 L 490 200 M 450 200 L 480 220" stroke="#d32f2f" stroke-width="3" stroke-linecap="round"/>
                    
                    <!-- Tourniquet Band -->
                    <rect x="250" y="135" width="40" height="120" fill="#455a64" rx="5"/>
                    <path d="M 250 135 L 290 135 L 290 255 L 250 255 Z" fill="none" stroke="#263238" stroke-width="3"/>
                    
                    <!-- Windlass Stick -->
                    <rect x="200" y="110" width="140" height="20" fill="#8d6e63" rx="5" transform="rotate(-15 270 120)"/>
                    <circle cx="270" cy="140" r="15" fill="#607d8b"/>
                    
                    <!-- Arrows for twisting -->
                    <path d="M 230 90 A 40 40 0 0 1 310 90" fill="none" stroke="#e67e22" stroke-width="4" marker-end="url(#arrow)"/>
                    
                    <defs>
                        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#e67e22" />
                        </marker>
                    </defs>

                    <!-- Annotations -->
                    <line x1="320" y1="60" x2="280" y2="100" stroke="#333" stroke-width="2"/>
                    <text x="330" y="55" font-size="14" font-weight="bold">1. Mechanical Windlass (Stick)</text>
                    
                    <line x1="230" y1="280" x2="260" y2="240" stroke="#333" stroke-width="2"/>
                    <text x="180" y="295" font-size="14" font-weight="bold">2. 2-Inch Wide Band</text>
                    
                    <text x="440" y="250" font-size="14" font-weight="bold" fill="#d32f2f">Arterial Bleed</text>
                </svg>
            </div>

            <div class="instruction-step"><strong>Step 1 (Identify):</strong> Bright red, spurting blood indicates arterial bleeding. Dark, steadily flowing blood is venous. Both can be fatal if not stopped within 2-3 minutes.</div>
            <div class="instruction-step"><strong>Step 2 (Fabric):</strong> Find a strong piece of fabric (canvas, leather belt) at least 2 inches wide. <em>Never use thin wire or paracord</em>.</div>
            <div class="instruction-step"><strong>Step 3 (Placement):</strong> Wrap the fabric around the limb <em>above</em> the wound, "High and Tight" (upper thigh or armpit).</div>
            <div class="instruction-step"><strong>Step 4 (Half-Knot):</strong> Tie a simple half-knot over the top of the limb.</div>
            <div class="instruction-step"><strong>Step 5 (Windlass):</strong> Place a strong, rigid stick over the half-knot, and tie a square knot <em>over</em> the stick.</div>
            <div class="instruction-step"><strong>Step 6 (Twist):</strong> Begin twisting the stick to mechanically crush the artery closed. Twist until bleeding stops completely.</div>
            <div class="instruction-step"><strong>Step 7 (Secure):</strong> Tie the ends of the stick down to the limb so it cannot unwind.</div>
            <div class="instruction-step"><strong>Step 8 (Time):</strong> Write the exact time of application on the patient's forehead (e.g., "TQ 14:30").</div>
        </div>

        <div class="how-to">
            <h3>2. Orthopedic Stabilization (The Traction Splint)</h3>
            <p>A fractured femur can sever the femoral artery if the bone shifts. The massive thigh muscles will immediately spasm, pulling the jagged bone ends over each other.</p>
            <div class="instruction-step"><strong>Step 1 (Manual Traction):</strong> Have the strongest person available grasp the patient's ankle and steadily pull the leg straight down. <em>Do not release this pull until the splint is fully secured.</em></div>
            <div class="instruction-step"><strong>Step 2 (Measure):</strong> Find two sturdy branches. The outside splint should reach from the armpit to past the foot. The inside splint should reach from the groin to past the foot.</div>
            <div class="instruction-step"><strong>Step 3 (Padding):</strong> Pad the rigid splints with clothing, moss, or leaves around bony prominences.</div>
            <div class="instruction-step"><strong>Step 4 (Binding):</strong> Tie the splints to the leg at four points: (1) Ankle, (2) Below the knee, (3) Above the knee, (4) Thigh/Groin. <em>Never tie a knot directly over the break itself.</em></div>
        </div>

        <hr>

        <h2>3. Midwifery and Childbirth</h2>
        <p>The continuation of the settlement depends entirely on the safe delivery of the next generation without surgical intervention.</p>
        <div class="how-to">
            <div class="instruction-step"><strong>Step 1 (The Gravity Position):</strong> Midwifery in a refugia relies on gravity. Utilize a squatting, kneeling, or supported-standing position to open the pelvic outlet by 20-30%.</div>
            <div class="instruction-step"><strong>Step 2 (Catching, Not Pulling):</strong> Support the perineum with a warm, damp cloth to prevent tearing, and support the baby's head as it emerges. <em>Never pull the infant.</em></div>
            <div class="instruction-step"><strong>Step 3 (The Golden Hour):</strong> Immediately after birth, place the infant skin-to-skin on the mother's bare chest. This regulates heart rate and introduces the mother's immune biome.</div>
            <div class="instruction-step"><strong>Step 4 (Delayed Cord Clamping):</strong> Do not cut the umbilical cord immediately. Wait until it turns white and stops pulsing (3-5 minutes) to transfer up to 30% of blood volume to the infant.</div>
            <div class="instruction-step"><strong>Step 5 (Sterile Cutting):</strong> Tie off the cord tightly in two places using boiled string, and cut <em>between</em> the ties using a flame-sterilized blade.</div>
        </div>

        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <ul>
                <li><strong>Delayed Cord Clamping:</strong> The World Health Organization (WHO) explicitly recommends delayed cord clamping (1-3 minutes minimum) for all births to improve maternal and infant health and nutrition outcomes.</li>
                <li><strong>The Windlass Tourniquet:</strong> Research from the Committee on Tactical Combat Casualty Care (CoTCCC) validates that improvised tourniquets without a mechanical windlass fail to achieve complete arterial occlusion in over 90% of cases, leading to a false sense of security and death by slow hemorrhage.</li>
            </ul>
        </div>

        <div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
            <h2>🚀 Practical Implementation Guide for Beginners</h2>
            <h3>1. Step-by-Step Action Plan</h3>
            <ul>
                <li><strong>Phase 1: The Trauma Kit:</strong> Assemble a dedicated zero-tech trauma bag today. It must contain: 2x commercially made windlass tourniquets (do not improvise these unless forced), 10 yards of compressed cotton gauze, and heavy-duty trauma shears.</li>
                <li><strong>Phase 2: The Drill:</strong> Conduct a mock drill. Have a community member simulate a severe leg wound. Time how long it takes for a responder to apply the tourniquet and achieve mechanical tightness. If it takes longer than 60 seconds, the drill is a failure.</li>
            </ul>
            <h3>2. Troubleshooting & Failure Modes</h3>
            <ul>
                <li><strong>Infection Post-Trauma:</strong> If a wound is packed to stop bleeding, the gauze <em>must</em> be removed and the wound irrigated with sterilized (boiled) water within 24 hours. Leaving bloody gauze in a deep cavity guarantees systemic sepsis.</li>
            </ul>
        </div>

    </section>

    <div class="nav">
        <span>Previous: <a href="../03_Temperate_Antibiotics.html">03 Temperate Antibiotics</a></span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

with open("04_The_Body/04_Trauma_and_Midwifery/01_Advanced_Trauma_and_Midwifery.md", "w", encoding="utf-8") as f:
    f.write(md_content)

with open("html/04_The_Body/04_Trauma_and_Midwifery/01_Advanced_Trauma_and_Midwifery.html", "w", encoding="utf-8") as f:
    f.write(html_content)
