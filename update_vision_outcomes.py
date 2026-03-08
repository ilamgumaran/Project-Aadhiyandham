import os
import re

def update_vision_file():
    filepath = "vision_and_outcomes.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace("### Outcome 3: Psychological Centeredness", 
"""### Outcome 3: Perimeter Sovereignty and Passive Defense [READY FOR REVIEW]
*   **Physical Security:** A community cannot achieve biological or psychological sovereignty if it is constantly vulnerable to external threats (human or animal). The settlement must be designed with intrinsic, passive defense mechanisms that deter conflict without requiring a permanent militarized state.
    *   *Solution Framework:* Topographical selection (high elevation, limited access points).
    *   *Missing/Optimal Placeholder:* `[READY FOR REVIEW] [TO BE DEVELOPED] Passive Perimeter Defense & Early Warning Systems` (Cultivating thorny biomimetic barriers, non-lethal deterrents, and acoustic tripwires).

### Outcome 4: Psychological Centeredness""")
    
    new_content = new_content.replace("### Outcome 4: Decadal and Generational Resilience", "### Outcome 5: Decadal and Generational Resilience")
    new_content = new_content.replace("### Outcome 5: A Flourishing Civilization", "### Outcome 6: A Flourishing Civilization")

    # Let's also add missing elements to Outcome 2 and 5 (now 6)
    # Actually they are already there from the previous steps, but let's make sure the missing areas I identified earlier (like Textiles and Trauma care) are properly tagged as READY FOR REVIEW if the user wants them.
    new_content = new_content.replace("[TO BE DEVELOPED] Advanced Trauma Care", "[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Trauma Care")
    new_content = new_content.replace("[TO BE DEVELOPED] Long-Term Food Preservation", "[READY FOR REVIEW] [TO BE DEVELOPED] Long-Term Food Preservation")
    new_content = new_content.replace("[TO BE DEVELOPED] Textile and Clothing Synthesis", "[READY FOR REVIEW] [TO BE DEVELOPED] Textile and Clothing Synthesis")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

update_vision_file()
