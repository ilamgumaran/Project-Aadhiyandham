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
    if "Outcome_1_" in filepath or "Candidate_Atlas" in filepath or "candidate_locations" in filepath:
        return "Outcome 1: Locating and Connecting Optimal Refugia"
    elif "Outcome_2_" in filepath:
        return "Outcome 2: Absolute Biological Sovereignty"
    elif "Outcome_3_" in filepath: 
        return "Outcome 3: Perimeter Sovereignty and Passive Defense"
    elif "Outcome_4_" in filepath:
        return "Outcome 4: Psychological Centeredness"
    elif "Outcome_5_" in filepath:
        return "Outcome 5: Decadal and Generational Resilience"
    elif "Outcome_6_" in filepath:
        return "Outcome 6: A Flourishing Civilization"
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

    for filepath in md_files:
        if 'html/' in filepath or '.git/' in filepath:
            continue
        
        outcome_key = map_to_outcome(filepath)
        if outcome_key == "Ignore":
            continue

        title, summary = extract_metadata(filepath)
        
        classification = "Atomic Topic"
        if "Rationale_and_Importance" in filepath:
            classification = "Module Theory & Structure"
        elif "Guide" in title or "How-To" in title or "Protocol" in title or "Practical" in title:
            classification = "Action Oriented"
        elif "Candidate_Atlas" in filepath or "candidate_locations" in filepath:
            classification = "Location Data"
            
        outcomes[outcome_key].append({
            'file': filepath,
            'title': title,
            'summary': summary,
            'class': classification
        })

    # Generate Markdown
    md_output = "# Content & Atomic File Plan (Aligned by Expected Outcomes)\n\n"
    md_output += "This document organizes all files in the repository by the **6 Expected Outcomes** of Project Aadhiyandham.\n\n"
    
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
    </style>
</head>
<body>
    <header>
        <p><a href="index.html">Main Index</a></p>
        <h1>Content & Atomic File Plan (Outcome Aligned)</h1>
        <p>A master tracker of all repository files categorized by the specific Vision Outcome they serve.</p>
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
        
        for item in sorted(outcomes[outcome], key=lambda x: x['file']):
            file_display = f"`{os.path.basename(item['file'])}`"
            html_file_display = f"<a href='../{item['file']}'>{os.path.basename(item['file'])}</a>"

            md_output += f"| {file_display} | {item['title']} | **{item['class']}** | {item['summary']} |\n"
            
            tag_class = ""
            if item['class'] == "Module Theory & Structure": tag_class = "tag-theory"
            elif item['class'] == "Action Oriented": tag_class = "tag-action"
            elif item['class'] == "Location Data": tag_class = "tag-location"
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
