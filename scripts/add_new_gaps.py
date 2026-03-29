import os

def update_vision_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Thermal Mass Cooking to Outcome 2 Food
    food_target = "*   *Solution Framework:* Long-Term Food Preservation"
    food_replacement = "*   *Missing/Optimal Placeholder:* `[READY FOR REVIEW] [TO BE DEVELOPED] Thermal Mass Cooking & Rocket Ovens` (Minimizing deforestation by cooking and boiling water with 80% less wood).\n    " + food_target
    content = content.replace(food_target, food_replacement)
    
    # Add Ceramic Synthesis to Outcome 5 Mechanics
    mech_target = "*   *Solution Framework:* Foundational Chemistry"
    mech_replacement = "*   *Missing/Optimal Placeholder:* `[READY FOR REVIEW] [TO BE DEVELOPED] Ceramic Synthesis & Pottery` (Pit-firing clay to create water-tight storage, fermentation crocks, and boiling vessels without scavenged metal).\n    " + mech_target
    content = content.replace(mech_target, mech_replacement)

    # Add Cordage to Outcome 5 Engineering
    eng_target = "*   *Solution Framework:* Textile and Clothing Synthesis"
    eng_replacement = "*   *Missing/Optimal Placeholder:* `[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Cordage and Rope Making` (Synthesizing high-tensile rope from plant fibers, essential for timber framing and traction splints).\n    " + eng_target
    content = content.replace(eng_target, eng_replacement)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_vision_file('vision_and_outcomes.md')

def update_html_vision(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    food_target = "<li><em>Solution Framework:</em> Long-Term Food Preservation"
    food_replacement = "<li><em>Missing/Optimal Placeholder:</em> <code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Thermal Mass Cooking & Rocket Ovens</code> (Minimizing deforestation by cooking and boiling water with 80% less wood).</li>\n                    " + food_target
    content = content.replace(food_target, food_replacement)
    
    mech_target = "<li><em>Solution Framework:</em> Foundational Chemistry"
    mech_replacement = "<li><em>Missing/Optimal Placeholder:</em> <code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Ceramic Synthesis & Pottery</code> (Pit-firing clay to create water-tight storage, fermentation crocks, and boiling vessels without scavenged metal).</li>\n                    " + mech_target
    content = content.replace(mech_target, mech_replacement)

    eng_target = "<li><em>Solution Framework:</em> Textile and Clothing Synthesis"
    eng_replacement = "<li><em>Missing/Optimal Placeholder:</em> <code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Cordage and Rope Making</code> (Synthesizing high-tensile rope from plant fibers, essential for timber framing and traction splints).</li>\n                    " + eng_target
    content = content.replace(eng_target, eng_replacement)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_html_vision('html/vision_and_outcomes.html')
