import os
import re

# We will write the new Midwifery file and rewrite the Trauma file.

midwifery_md = """# Generational Midwifery and Neonatal Care: The First Year

**Alignment:** Outcome 2: Absolute Biological Sovereignty

## 1. Why This Is Important (The Rationale)
Outcome 2 requires Absolute Biological Sovereignty. The continuation of the settlement depends entirely on the safe delivery and survival of the next generation without surgical intervention (Caesarean sections) or modern neonatal intensive care units (NICUs). Historically, infant and maternal mortality were the greatest limiters of population growth. By combining ancient midwifery practices with modern understandings of hygiene and biome transfer, a community can drastically reduce these risks.

---

## 2. Prenatal Care: Building the Foundation

A healthy birth begins months before labor. The mother's physiology must be supported.

### 2.1. Nutritional Fortification
*   **Folate and Iron:** Neural tube defects and maternal anemia are primary risks. The diet must heavily prioritize dark leafy greens (for folate) and liver/red meat cooked in cast-iron (for highly bioavailable heme iron).
*   **Calcium Harvesting:** If dairy is unavailable, calcium must be sourced from crushed eggshells dissolved in vinegar or bone broth boiled for 48 hours to soften the marrow.

### 2.2. Biomechanical Preparation
*   **The Deep Squat:** Modern sitting shortens the pelvic floor muscles. Pregnant women should spend time daily in a deep, supported squat (Garland pose / *Malasana*). This stretches the perineum and physically opens the pelvic outlet, preparing the body for a zero-intervention birth.

---

## 3. Childbirth: Zero-Tech Delivery

Labor is not a medical emergency; it is a physiological process that requires gravity and calm.

### 3.1. The Gravity Position
The modern practice of a mother lying flat on her back is a recent medical convenience, not a biological optimum. Midwifery in a refugia relies on gravity. 
*   **Action:** Utilize a squatting, kneeling, or supported-standing position. This opens the pelvic outlet by an additional 20-30%, significantly reducing the risk of obstructed labor.

### 3.2. Catching, Not Pulling
*   **Action:** As the infant crowns, the midwife should support the perineum with a warm, damp cloth (sterilized) to prevent tearing, and simply support the baby's head as it emerges. *Never pull the infant.* Let the mother's contractions do the work.

### 3.3. Delayed Cord Clamping
*   **Action:** Do not cut the umbilical cord immediately. Wait until it turns white and stops pulsing (usually 3-5 minutes). This allows up to 30% of the infant's total blood volume, including critical stem cells and iron reserves, to transfer from the placenta, preventing neonatal anemia.
*   **Sterile Cutting:** Tie off the cord tightly in two places using boiled string, and cut *between* the ties using a flame-sterilized blade. 

---

## 4. Postnatal and Neonatal Care: Preventing Mortality

The first 30 days are the most dangerous period of human life.

### 4.1. The Golden Hour and Biome Transfer
*   Immediately after birth, before cleaning, place the infant skin-to-skin on the mother's bare chest and cover them both. 
*   This regulates the infant's heart rate, stabilizes their body temperature, and introduces them to the mother's skin biome (essential for the infant's immune system) before environmental pathogens can take hold.

### 4.2. Colostrum and Lactation
*   The first milk produced (Colostrum) is thick, yellow, and packed with antibodies (Secretory IgA). It is literally the infant's first oral vaccine.
*   If the mother struggles to lactate, herbal galactagogues like Fenugreek or Fennel seed tea must be administered immediately.

### 4.3. The "Fourth Trimester" (Postnatal Rest)
*   The mother is highly vulnerable to postpartum hemorrhage and infection. She must be mandated to remain in bed or close to the hearth for 30 to 40 days, relieved of all physical labor. The community must provide all meals and water.

---

## 5. 🔬 Scientific Validation & Research Context
*   **Delayed Cord Clamping:** The World Health Organization (WHO) explicitly recommends delayed cord clamping (1-3 minutes minimum) for all births to improve maternal and infant health and nutrition outcomes.
*   **Skin-to-Skin Contact (Kangaroo Care):** Clinical studies confirm that immediate skin-to-skin contact reduces neonatal mortality by 36% in low-resource settings, as it prevents hypothermia and stimulates immediate breastfeeding reflexes.

---
## 6. Practical Implementation Guide for Beginners

### 6.1. Step-by-Step Action Plan
*   **Phase 1: The Delivery Kit:** Assemble a sterile birthing kit containing: heavy cotton thread (for cord tying), a scalpel blade or extremely sharp knife (never used for other tasks), clean cotton cloths (boiled and sun-dried), and a suction bulb (if scavenged) to clear the infant's airway.
*   **Phase 2: Midwife Apprenticeship:** Identify at least two women in the settlement who will act as primary midwives. They must cross-train so that multiple people possess the calm, experiential knowledge required to guide a first-time mother through labor.

### 6.2. Troubleshooting & Failure Modes
*   **Postpartum Hemorrhage:** If the mother bleeds excessively after the placenta is delivered, immediately initiate vigorous, deep uterine massage (rubbing the lower abdomen). This forces the uterus to contract and clamp down on the bleeding vessels. Encourage immediate breastfeeding, as nipple stimulation releases oxytocin, which also triggers uterine contractions.
"""

trauma_md = """# Advanced Trauma Care: Zero-Tech Medical Protocols

**Alignment:** Outcome 2: Absolute Biological Sovereignty

## 1. Why This Is Important (The Rationale)
Outcome 2 requires Absolute Biological Sovereignty. While the "Temperate Antibiotic Kit" addresses baseline infection and illness, a settlement will inevitably face acute physical trauma. Without a functional industrial hospital, the inability to set a broken bone or stop arterial bleeding turns an accident into a generational tragedy. 

---

## 2. Advanced Trauma Protocols: Detailed Execution

### 2.1. Hemorrhage Control (The Windlass Tourniquet)
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

### 2.2. Orthopedic Stabilization (The Traction Splint)
A fractured femur can sever the femoral artery if the bone shifts. The massive thigh muscles will immediately spasm, pulling the jagged bone ends over each other. 

**Step-by-Step Application:**
1. **Manual Traction:** Have the strongest person available grasp the patient's ankle and steadily, firmly pull the leg straight down, aligning it with the healthy leg. This is excruciating but necessary. *Do not release this pull until the splint is fully secured.*
2. **Measure the Splints:** Find two sturdy branches or planks. The outside splint should reach from the armpit to past the foot. The inside splint should reach from the groin to past the foot.
3. **Padding:** Pad the rigid splints with clothing, moss, or leaves, especially around bony prominences (knees, ankles).
4. **Binding:** Using cloth strips, tie the splints to the leg at four points: (1) Ankle, (2) Below the knee, (3) Above the knee, (4) Thigh/Groin. *Never tie a knot directly over the break itself.*

---

## 3. 🔬 Scientific Validation & Research Context
*   **The Windlass Tourniquet:** Research from the Committee on Tactical Combat Casualty Care (CoTCCC) validates that improvised tourniquets without a mechanical windlass fail to achieve complete arterial occlusion in over 90% of cases, leading to a false sense of security and death by slow hemorrhage.

---
## 4. Practical Implementation Guide for Beginners

### 4.1. Step-by-Step Action Plan
*   **Phase 1: The Trauma Kit:** Assemble a dedicated zero-tech trauma bag today. It must contain: 2x commercially made windlass tourniquets (do not improvise these unless forced), 10 yards of compressed cotton gauze, and heavy-duty trauma shears.
*   **Phase 2: The Drill:** Conduct a mock drill. Have a community member simulate a severe leg wound. Time how long it takes for a responder to apply the tourniquet and achieve mechanical tightness. If it takes longer than 60 seconds, the drill is a failure.

### 4.2. Troubleshooting & Failure Modes
*   **Infection Post-Trauma:** If a wound is packed to stop bleeding, the gauze *must* be removed and the wound irrigated with sterilized (boiled) water within 24 hours. Leaving bloody gauze in a deep cavity guarantees systemic sepsis.
"""

def update_files():
    # 1. Rename the Trauma directory
    old_trauma_dir = "Outcome_2_Biological_Sovereignty/04_The_Body/04_Trauma_and_Midwifery"
    new_trauma_dir = "Outcome_2_Biological_Sovereignty/04_The_Body/04_Advanced_Trauma_Care"
    
    if os.path.exists(old_trauma_dir):
        os.rename(old_trauma_dir, new_trauma_dir)
        
    old_html_trauma_dir = "html/Outcome_2_Biological_Sovereignty/04_The_Body/04_Trauma_and_Midwifery"
    new_html_trauma_dir = "html/Outcome_2_Biological_Sovereignty/04_The_Body/04_Advanced_Trauma_Care"
    if os.path.exists(old_html_trauma_dir):
        os.rename(old_html_trauma_dir, new_html_trauma_dir)

    # 2. Write the new Trauma File
    with open(f"{new_trauma_dir}/01_Advanced_Trauma_Care.md", "w", encoding="utf-8") as f:
        f.write(trauma_md)
        
    # Delete old trauma file
    if os.path.exists(f"{new_trauma_dir}/01_Advanced_Trauma_and_Midwifery.md"):
        os.remove(f"{new_trauma_dir}/01_Advanced_Trauma_and_Midwifery.md")

    # 3. Create Midwifery directory and write file
    mid_dir = "Outcome_2_Biological_Sovereignty/04_The_Body/07_Maternal_and_Neonatal_Care"
    os.makedirs(mid_dir, exist_ok=True)
    with open(f"{mid_dir}/01_Generational_Midwifery_and_Care.md", "w", encoding="utf-8") as f:
        f.write(midwifery_md)

if __name__ == "__main__":
    update_files()
    print("Maternal and Trauma split successfully.")
