import os
import glob
import re

def extract_metadata(filepath):
    title = ""
    summary = ""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not title and line.startswith('# '):
                title = line[2:]
            elif title and line and not line.startswith('#') and not line.startswith('---') and not line.startswith('!['):
                if len(line) > 20:
                    summary = line
                    break
    if not title:
        title = os.path.basename(filepath)
    if len(summary) > 150:
        summary = summary[:147] + "..."
    return title, summary

def map_to_outcome(filepath):
    if "01_The_Journey" in filepath or "02_The_Site" in filepath or "candidate_locations" in filepath:
        return "Outcome 1: Locating and Connecting Optimal Refugia"
    elif "03_The_Arrival" in filepath or "04_The_Body" in filepath or "06_The_Ecosystem" in filepath:
        return "Outcome 2: Absolute Biological Sovereignty"
    elif "03_The_Arrival/07_Perimeter_Defense" in filepath: 
        return "Outcome 3: Perimeter Sovereignty and Passive Defense"
    elif "05_The_Mind" in filepath:
        return "Outcome 4: Psychological Centeredness"
    elif "07_The_Mechanics" in filepath or "08_The_Society" in filepath or "09_The_Next_Generation" in filepath or "10_The_Archive" in filepath or "11_The_Horizon" in filepath:
        if "09_The_Next_Generation/08_Cultural_Technology" in filepath:
            return "Outcome 6: A Flourishing Civilization"
        return "Outcome 5: Decadal and Generational Resilience"
    elif "node_modules" in filepath:
        return "Ignore"
    else:
        return "Foundational Documents"

def generate_plan():
    md_files = glob.glob('**/*.md', recursive=True)
    
    outcomes = {
        "Outcome 1: Locating and Connecting Optimal Refugia": [],
        "Outcome 2: Absolute Biological Sovereignty": [],
        "Outcome 3: Perimeter Sovereignty and Passive Defense": [],
        "Outcome 4: Psychological Centeredness": [],
        "Outcome 5: Decadal and Generational Resilience": [],
        "Outcome 6: A Flourishing Civilization": [],
        "Foundational Documents": []
    }
    
    # Adding NEW missing files to the outcomes mapping manually based on the deep review
    outcomes["Outcome 1: Locating and Connecting Optimal Refugia"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Advanced Micro-Climate Forecasting", "summary": "Predicting localized weather shifts over a 50-year horizon without meteorological satellites.", "class": "Missing Action File"})
    
    outcomes["Outcome 2: Absolute Biological Sovereignty"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Generational Sanitation & Humanure", "summary": "Thermophilic composting of human waste to safely close the phosphorus cycle without contaminating groundwater.", "class": "Missing Action File"})
    outcomes["Outcome 2: Absolute Biological Sovereignty"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Zero-Tech Dentistry & Oral Hygiene", "summary": "Preventing lethal dental abscesses via miswak/neem sticks, salt, and emergency extraction protocols.", "class": "Missing Action File"})
    
    outcomes["Outcome 3: Perimeter Sovereignty and Passive Defense"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Wildfire Defensible Space", "summary": "Forest management, controlled burns, and structural fire-breaks to prevent absolute ecological erasure.", "class": "Missing Action File"})
    
    outcomes["Outcome 5: Decadal and Generational Resilience"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Foundational Chemistry", "summary": "Extracting potash and lye from wood ash to synthesize soap, vital for surgical hygiene and disease prevention.", "class": "Missing Action File"})
    outcomes["Outcome 5: Decadal and Generational Resilience"].append({"file": "MISSING_PLACEHOLDER", "title": "[READY FOR REVIEW] Information Storage", "summary": "Synthesizing paper from plant fibers and creating Iron Gall ink to ensure the physical ledger outlasts scavenged notebooks.", "class": "Missing Action File"})

    for filepath in md_files:
        if 'html/' in filepath or '.git/' in filepath:
            continue
        
        outcome_key = map_to_outcome(filepath)
        if outcome_key == "Ignore":
            continue
            
        # Re-route specific files that were created in previous steps into their exact outcome
        if "03_The_Arrival/07_Perimeter_Defense" in filepath:
            outcome_key = "Outcome 3: Perimeter Sovereignty and Passive Defense"
        elif "09_The_Next_Generation/08_Cultural_Technology" in filepath:
            outcome_key = "Outcome 6: A Flourishing Civilization"

        title, summary = extract_metadata(filepath)
        
        classification = "Atomic Topic"
        if "Rationale_and_Importance" in filepath:
            classification = "Module Theory & Structure"
        elif "Guide" in title or "How-To" in title or "Protocol" in title:
            classification = "Action Oriented"
        elif "candidate_locations" in filepath:
            classification = "Location Data"
            
        outcomes[outcome_key].append({
            'file': filepath,
            'title': title,
            'summary': summary,
            'class': classification
        })

    # Generate Markdown
    md_output = "# Content & Atomic File Plan (Aligned by Expected Outcomes)\n\n"
    md_output += "This document organizes all files in the repository by the **6 Expected Outcomes** of Project Aadhiyandham. Missing gaps critical to these outcomes are tagged as `[READY FOR REVIEW]`.\n\n"
    
    html_output = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Content Plan - Project Aadhiyandham</title>
    <link rel="stylesheet" href="style.css">
    <style>
        table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #2c3e50; color: white; }
        .tag-theory { background: #e8f4f8; color: #2980b9; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }
        .tag-action { background: #fdf2e9; color: #d35400; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; font-weight:bold; }
        .tag-atomic { background: #eef7ed; color: #27ae60; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }
        .tag-location { background: #f4f6f7; color: #7f8c8d; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }
        .tag-missing { background: #fdeded; color: #e74c3c; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; font-weight:bold; border: 1px solid #e74c3c; }
    </style>
</head>
<body>
    <header>
        <p><a href="index.html">Main Index</a></p>
        <h1>Content & Atomic File Plan (Outcome Aligned)</h1>
        <p>A master tracker of all repository files categorized by the specific Vision Outcome they serve, including highlighted critical gaps.</p>
    </header>
    <section>
"""

    outcome_order = [
        "Foundational Documents",
        "Outcome 1: Locating and Connecting Optimal Refugia",
        "Outcome 2: Absolute Biological Sovereignty",
        "Outcome 3: Perimeter Sovereignty and Passive Defense",
        "Outcome 4: Psychological Centeredness",
        "Outcome 5: Decadal and Generational Resilience",
        "Outcome 6: A Flourishing Civilization"
    ]

    for outcome in outcome_order:
        md_output += f"## {outcome}\n\n"
        md_output += "| File | Title | Classification | Summary |\n"
        md_output += "|---|---|---|---|\n"
        
        html_output += f"<h2>{outcome}</h2>\n<table>\n"
        html_output += "<tr><th>File</th><th>Title</th><th>Classification</th><th>Summary</th></tr>\n"
        
        for item in sorted(outcomes[outcome], key=lambda x: (x['class'] != 'Missing Action File', x['file'])):
            file_display = f"`{os.path.basename(item['file'])}`" if item['file'] != "MISSING_PLACEHOLDER" else "---"
            html_file_display = f"<a href='../{item['file']}'>{os.path.basename(item['file'])}</a>" if item['file'] != "MISSING_PLACEHOLDER" else "---"

            md_output += f"| {file_display} | {item['title']} | **{item['class']}** | {item['summary']} |\n"
            
            tag_class = ""
            if item['class'] == "Module Theory & Structure": tag_class = "tag-theory"
            elif item['class'] == "Action Oriented": tag_class = "tag-action"
            elif item['class'] == "Location Data": tag_class = "tag-location"
            elif item['class'] == "Missing Action File": tag_class = "tag-missing"
            else: tag_class = "tag-atomic"
            
            html_output += f"<tr><td>{html_file_display}</td><td>{item['title']}</td><td><span class='{tag_class}'>{item['class']}</span></td><td>{item['summary']}</td></tr>\n"
            
        md_output += "\n"
        html_output += "</table>\n"
        
    html_output += """
    </section>
    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

    with open('content_plan.md', 'w', encoding='utf-8') as f:
        f.write(md_output)
        
    with open('html/content_plan.html', 'w', encoding='utf-8') as f:
        f.write(html_output)

if __name__ == "__main__":
    generate_plan()
