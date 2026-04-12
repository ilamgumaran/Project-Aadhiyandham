"""
inject_nav.py — Inject global navigation bar into all HTML files.

Updates the nav bar and ensures consistent navigation across the entire
HTML output. Handles varying directory depths with relative path calculation.
"""

import os
import re

NAV_HTML = """
    <!-- Global Navigation Bar -->
    <nav class="global-nav">
        <ul>
            <li><a href="{root_path}index.html">Home</a></li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 1 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_1_Locating_Refugia/01_The_Journey/01_Rationale_and_Importance.html">01. The Journey</a>
                    <a href="{root_path}Outcome_1_Locating_Refugia/02_The_Site/01_Rationale_and_Importance.html">02. The Site</a>
                    <a href="{root_path}Outcome_1_Locating_Refugia/03_Candidate_Atlas/template_location.html">03. The Atlas</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 2 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/01_Rationale_and_Importance.html">03. Water &amp; Sanitation</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/01_Rationale_and_Importance.html">04. Food &amp; Soil</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/01_Rationale_and_Importance.html">05. Health &amp; Body</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/01_Rationale_and_Importance.html">06. Ecological Harmony</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 3 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_3_Perimeter_Defense/07_Passive_Defense/01_Rationale_and_Importance.html">07. Passive Defense</a>
                    <a href="{root_path}Outcome_3_Perimeter_Defense/07a_Active_Threat_Response/01_Rationale_and_Importance.html">07a. Active Threat Response</a>
                    <a href="{root_path}Outcome_3_Perimeter_Defense/07b_Animal_Coexistence_Protocols/01_Rationale_and_Importance.html">07b. Animal Coexistence</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 4 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_4_Psychological_Centeredness/08_The_Mind/01_Rationale_and_Importance.html">08. The Mind</a>
                    <a href="{root_path}Outcome_4_Psychological_Centeredness/08a_Group_Dynamics/01_Rationale_and_Importance.html">08a. Group Dynamics</a>
                    <a href="{root_path}Outcome_4_Psychological_Centeredness/08b_Childhood_Development/01_Rationale_and_Importance.html">08b. Childhood Development</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 5 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_5_Decadal_Resilience/09_The_Mechanics/01_Rationale_and_Importance.html">09. The Mechanics</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/10_The_Society/01_Rationale_and_Importance.html">10. The Society</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/11_The_Next_Generation/01_Rationale_and_Importance.html">11. Education</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/12_The_Archive/01_Rationale_and_Importance.html">12. The Archive</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/13_The_Horizon/01_Rationale_and_Importance.html">13. The Horizon</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 6 &#9662;</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_6_Flourishing_Civilization/14_Cultural_Technology/01_Rationale_and_Importance.html">14. Cultural Technology</a>
                    <a href="{root_path}Outcome_6_Flourishing_Civilization/14a_Inter_Settlement_Diplomacy/01_Rationale_and_Importance.html">14a. Diplomacy</a>
                    <a href="{root_path}Outcome_6_Flourishing_Civilization/14b_Knowledge_Exchange/01_Rationale_and_Importance.html">14b. Knowledge Exchange</a>
                </div>
            </li>
            <li><a href="{root_path}Glossary.html">Glossary</a></li>
        </ul>
    </nav>
"""


def update_html():
    """Inject navigation bar into all HTML files."""
    count = 0
    for root, dirs, files in os.walk('html'):
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)

            # Calculate relative path from this file to the html/ root
            rel_from_html = os.path.relpath(filepath, 'html')
            depth = rel_from_html.count(os.sep)
            root_path = '../' * depth if depth > 0 else './'

            nav_block = NAV_HTML.format(root_path=root_path)

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace existing nav or inject after <body>
            if '<!-- Global Navigation Bar -->' in content:
                content = re.sub(
                    r'<!-- Global Navigation Bar -->.*?</nav>',
                    nav_block.strip(),
                    content,
                    flags=re.DOTALL
                )
            elif '<body' in content:
                content = re.sub(
                    r'(<body[^>]*>)',
                    r'\1\n' + nav_block,
                    content,
                    count=1
                )

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

    print(f"Navigation injected into {count} HTML files.")


if __name__ == '__main__':
    update_html()
