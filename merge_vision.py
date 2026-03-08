import os

# Read the vision content
with open('vision_and_outcomes.md', 'r', encoding='utf-8') as f:
    vision_md = f.read()

# Read the HTML vision content to extract the section
with open('html/vision_and_outcomes.html', 'r', encoding='utf-8') as f:
    vision_html_full = f.read()
    
    # Extract just the <section> block
    import re
    match = re.search(r'<section>(.*?)</section>', vision_html_full, re.DOTALL)
    if match:
        vision_html_section = match.group(1).strip()
    else:
        vision_html_section = ""

# --- UPDATE README.MD ---
clean_vision_md = vision_md.replace('# Project Vision and Expected Outcomes\n\n', '')
readme_content = f"""# Project Aadhiyandham (ஆதியந்தம்): A User Manual for Civilization

{clean_vision_md}

---

## 4. Resources and Quick Links
*   **[content_plan.md](content_plan.md):** The master tracker classifying all atomic and action-oriented files.
*   **[master_report.md](master_report.md):** The final synthesis and global candidate ranking.
*   **[settlers_summary.md](settlers_summary.md):** The condensed, action-oriented handbook.
*   **[Glossary.md](Glossary.md):** Detailed definitions of project terms.
*   **[candidate_locations/](candidate_locations/):** Detailed evaluations of 70 resilient global sites.
*   **[html/](html/):** A beautiful, web-ready version of the archive.
"""

with open('readme.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)


# --- UPDATE HTML/INDEX.HTML ---
# We want to replace the current overview and mandate with the detailed vision_html_section,
# and then put the navigation and quick links at the bottom.

index_html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project Aadhiyandham (ஆதியந்தம்) - Archive</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <h1>Project Aadhiyandham (ஆதியந்தம்)</h1>
        <p><em>The Architecture of the Null: A User Manual for Civilization</em></p>
    </header>

    <section>
        {vision_html_section}
    </section>

    <nav>
        <h2>The Master Structure: Aligned by Expected Outcomes</h2>
        <p>To ensure every action serves the core vision, the manual's modules are organized by the 6 Expected Outcomes.</p>
        
        <ul>
            <li><strong>Outcome 1: Locating & Connecting Optimal Refugia</strong>
                <ul>
                    <li><a href="01_The_Journey/01_Rationale_and_Importance.html">01 The Journey</a> (Transit & Navigation)</li>
                    <li><a href="02_The_Site/01_Rationale_and_Importance.html">02 The Site</a> (Geography & Climate)</li>
                    <li><a href="candidate_locations/index.html">The Candidate Atlas</a> (70 Resilient Locations)</li>
                </ul>
            </li>
            <li><strong>Outcome 2: Absolute Biological Sovereignty</strong>
                <ul>
                    <li><a href="03_The_Arrival/01_Rationale_and_Importance.html">03 The Arrival</a> (Water & Early Shelter)</li>
                    <li><a href="04_The_Body/01_Rationale_and_Importance.html">04 The Body</a> (Endocrine Health & Antibiotics)</li>
                    <li><a href="06_The_Ecosystem/01_Rationale_and_Importance.html">06 The Ecosystem</a> (Soil, Seed, & Livestock)</li>
                </ul>
            </li>
            <li><strong>Outcome 3: Perimeter Sovereignty and Passive Defense</strong>
                <ul>
                    <li><a href="03_The_Arrival/07_Perimeter_Defense/01_Passive_Perimeter_Defense.html">Perimeter Defense</a> (Acoustic Tripwires & Fire Breaks)</li>
                </ul>
            </li>
            <li><strong>Outcome 4: Psychological Centeredness</strong>
                <ul>
                    <li><a href="05_The_Mind/01_Rationale_and_Importance.html">05 The Mind</a> (Linguistic Precision & Architecture)</li>
                </ul>
            </li>
            <li><strong>Outcome 5: Decadal and Generational Resilience</strong>
                <ul>
                    <li><a href="07_The_Mechanics/01_Rationale_and_Importance.html">07 The Mechanics</a> (Power & Smelting)</li>
                    <li><a href="08_The_Society/01_Rationale_and_Importance.html">08 The Society</a> (Consensus Governance)</li>
                    <li><a href="09_The_Next_Generation/01_Rationale_and_Importance.html">09 The Next Generation</a> (Education)</li>
                    <li><a href="10_The_Archive/01_Rationale_and_Importance.html">10 The Archive</a> (Natural Phenomena)</li>
                    <li><a href="11_The_Horizon/01_Rationale_and_Importance.html">11 The Horizon</a> (Advanced Synthesis)</li>
                </ul>
            </li>
            <li><strong>Outcome 6: A Flourishing Civilization</strong>
                <ul>
                    <li><a href="09_The_Next_Generation/08_Cultural_Technology/01_Cultural_Technology_and_Rituals.html">Cultural Technology</a> (Rituals, Calendars, & Meaning)</li>
                </ul>
            </li>
        </ul>
    </nav>

    <section>
        <hr>
        <div class="how-to">
            <h2>Quick Reference Links</h2>
            <p>View the <strong><a href="content_plan.html">Content & Atomic File Plan</a></strong> to see the exact alignment of all files, the <strong><a href="master_report.html">Master Research Report</a></strong> for the executive summary, the <strong><a href="settlers_summary.html">Settler's Summary</a></strong> for immediate survival actions, or the <strong><a href="glossary.html">Glossary</a></strong> for term definitions.</p>
        </div>
    </section>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

with open('html/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html_template)
