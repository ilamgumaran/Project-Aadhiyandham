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
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for old, new in replacements:
            content = content.replace(old, new)

        content = content.replace("*Missing/Optimal Placeholder:*", "*Solution Framework:*")
        content = content.replace("<em>Missing/Optimal Placeholder:</em>", "<em>Solution Framework:</em>")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def fix_index_links():
    """Fix links in readme.md and html/index.html to match global numbering."""

    # Readme
    if os.path.exists('readme.md'):
        with open('readme.md', 'r', encoding='utf-8') as f:
            readme = f.read()
        # Update candidate_locations reference
        readme = readme.replace("[candidate_locations/](candidate_locations/)",
                                "[Candidate Atlas](Outcome_1_Locating_Refugia/03_Candidate_Atlas/)")
        with open('readme.md', 'w', encoding='utf-8') as f:
            f.write(readme)

    # index.html
    if os.path.exists('html/index.html'):
        with open('html/index.html', 'r', encoding='utf-8') as f:
            index = f.read()

        # Update to global numbering paths
        index = index.replace('href="candidate_locations/', 'href="Outcome_1_Locating_Refugia/03_Candidate_Atlas/')
        index = index.replace('candidate_locations/index.html', 'Outcome_1_Locating_Refugia/03_Candidate_Atlas/index.html')

        with open('html/index.html', 'w', encoding='utf-8') as f:
            f.write(index)

if __name__ == "__main__":
    update_vision()
    fix_index_links()
    print("Cleaned up remaining placeholders and fixed broken root index links.")
