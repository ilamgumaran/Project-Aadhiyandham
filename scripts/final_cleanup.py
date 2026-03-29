import os
import re

def update_vision():
    files = ['vision_and_outcomes.md', 'html/vision_and_outcomes.html']
    
    replacements = [
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Thermal Mass Cooking & Rocket Ovens`", "Thermal Mass Cooking & Rocket Ovens"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Thermal Mass Cooking & Rocket Ovens</code>", "Thermal Mass Cooking & Rocket Ovens"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Ceramic Synthesis & Pottery`", "Ceramic Synthesis & Pottery"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Ceramic Synthesis & Pottery</code>", "Ceramic Synthesis & Pottery"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Cordage and Rope Making`", "Advanced Cordage and Rope Making"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Cordage and Rope Making</code>", "Advanced Cordage and Rope Making"),
    ]
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for old, new in replacements:
            content = content.replace(old, new)
            
        # Fix the "Missing/Optimal Placeholder:" prefix for these items
        # Because we just removed the tag, the line now looks like:
        # *Missing/Optimal Placeholder:* Thermal Mass Cooking & Rocket Ovens
        # We need to change that prefix to Solution Framework.
        # It's easier to just do a regex replace for any Missing/Optimal Placeholder that doesn't have [TO BE DEVELOPED]
        
        # But wait, there are no more TO BE DEVELOPED tags! All of them are done.
        content = content.replace("*Missing/Optimal Placeholder:*", "*Solution Framework:*")
        content = content.replace("<em>Missing/Optimal Placeholder:</em>", "<em>Solution Framework:</em>")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def fix_index_links():
    # Fix the links in readme.md and html/index.html that point to the old root folders instead of Outcome_X_...
    
    # Readme
    with open('readme.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        
    readme = readme.replace("[01_The_Journey/](01_The_Journey/)", "[01_The_Journey/](Outcome_1_Locating_Refugia/01_The_Journey/)")
    readme = readme.replace("[02_The_Site/](02_The_Site/)", "[02_The_Site/](Outcome_1_Locating_Refugia/02_The_Site/)")
    readme = readme.replace("[03_The_Arrival/](03_The_Arrival/)", "[03_The_Arrival/](Outcome_2_Biological_Sovereignty/03_The_Arrival/)")
    readme = readme.replace("[04_The_Body/](04_The_Body/)", "[04_The_Body/](Outcome_2_Biological_Sovereignty/04_The_Body/)")
    readme = readme.replace("[06_The_Ecosystem/](06_The_Ecosystem/)", "[06_The_Ecosystem/](Outcome_2_Biological_Sovereignty/06_The_Ecosystem/)")
    readme = readme.replace("[05_The_Mind/](05_The_Mind/)", "[05_The_Mind/](Outcome_4_Psychological_Centeredness/05_The_Mind/)")
    readme = readme.replace("[07_The_Mechanics/](07_The_Mechanics/)", "[07_The_Mechanics/](Outcome_5_Decadal_Resilience/07_The_Mechanics/)")
    readme = readme.replace("[08_The_Society/](08_The_Society/)", "[08_The_Society/](Outcome_5_Decadal_Resilience/08_The_Society/)")
    readme = readme.replace("[09_The_Next_Generation/](09_The_Next_Generation/)", "[09_The_Next_Generation/](Outcome_5_Decadal_Resilience/09_The_Next_Generation/)")
    readme = readme.replace("[10_The_Archive/](10_The_Archive/)", "[10_The_Archive/](Outcome_5_Decadal_Resilience/10_The_Archive/)")
    readme = readme.replace("[11_The_Horizon/](11_The_Horizon/)", "[11_The_Horizon/](Outcome_5_Decadal_Resilience/11_The_Horizon/)")
    
    with open('readme.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    # index.html
    with open('html/index.html', 'r', encoding='utf-8') as f:
        index = f.read()

    # The manual links in the <nav> element in index.html text body
    index = index.replace('href="01_The_Journey/', 'href="Outcome_1_Locating_Refugia/01_The_Journey/')
    index = index.replace('href="02_The_Site/', 'href="Outcome_1_Locating_Refugia/02_The_Site/')
    index = index.replace('href="03_The_Arrival/', 'href="Outcome_2_Biological_Sovereignty/03_The_Arrival/')
    index = index.replace('href="04_The_Body/', 'href="Outcome_2_Biological_Sovereignty/04_The_Body/')
    index = index.replace('href="06_The_Ecosystem/', 'href="Outcome_2_Biological_Sovereignty/06_The_Ecosystem/')
    index = index.replace('href="05_The_Mind/', 'href="Outcome_4_Psychological_Centeredness/05_The_Mind/')
    index = index.replace('href="07_The_Mechanics/', 'href="Outcome_5_Decadal_Resilience/07_The_Mechanics/')
    index = index.replace('href="08_The_Society/', 'href="Outcome_5_Decadal_Resilience/08_The_Society/')
    index = index.replace('href="09_The_Next_Generation/', 'href="Outcome_5_Decadal_Resilience/09_The_Next_Generation/')
    index = index.replace('href="10_The_Archive/', 'href="Outcome_5_Decadal_Resilience/10_The_Archive/')
    index = index.replace('href="11_The_Horizon/', 'href="Outcome_5_Decadal_Resilience/11_The_Horizon/')

    # Fix the specific moved ones
    index = index.replace('Outcome_2_Biological_Sovereignty/03_The_Arrival/07_Perimeter_Defense/01_Passive_Perimeter_Defense.html', 'Outcome_3_Perimeter_Defense/01_Passive_Defense/01_Passive_Perimeter_Defense.html')
    index = index.replace('Outcome_5_Decadal_Resilience/09_The_Next_Generation/08_Cultural_Technology/01_Cultural_Technology_and_Rituals.html', 'Outcome_6_Flourishing_Civilization/01_Cultural_Technology/01_Cultural_Technology_and_Rituals.html')

    with open('html/index.html', 'w', encoding='utf-8') as f:
        f.write(index)

if __name__ == "__main__":
    update_vision()
    fix_index_links()
    print("Cleaned up remaining placeholders and fixed broken root index links.")
