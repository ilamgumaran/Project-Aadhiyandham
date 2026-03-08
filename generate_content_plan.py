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
                # Grab the first non-empty text paragraph as a summary
                if len(line) > 20:
                    summary = line
                    break
    
    if not title:
        title = os.path.basename(filepath)
    if len(summary) > 150:
        summary = summary[:147] + "..."
        
    return title, summary

def generate_plan():
    # Gather all markdown files except in html/ and candidate_locations/ for the core structural mapping
    # Actually let's include candidate_locations but group them separately.
    md_files = glob.glob('**/*.md', recursive=True)
    
    modules = {}
    for filepath in md_files:
        if 'html/' in filepath or '.git/' in filepath:
            continue
        
        dir_name = os.path.dirname(filepath)
        if not dir_name:
            dir_name = "Root"
            
        title, summary = extract_metadata(filepath)
        
        # Classification guess: if it's "Rationale_and_Importance", it's a structural/theory file
        # If it's something else, it's an atomic topic or action file
        classification = "Atomic Topic"
        if "Rationale_and_Importance" in filepath:
            classification = "Module Theory & Structure"
        elif "Guide" in title or "How-To" in title or "Protocol" in title:
            classification = "Action Oriented"
        elif "candidate_locations" in filepath:
            classification = "Location Data"
            
        if dir_name not in modules:
            modules[dir_name] = []
            
        modules[dir_name].append({
            'file': filepath,
            'title': title,
            'summary': summary,
            'class': classification
        })

    # Sort directories
    sorted_dirs = sorted(modules.keys())
    
    # Generate Markdown
    md_output = "# Project Aadhiyandham: Content & Atomic File Plan\n\n"
    md_output += "This document serves as a master tracker for all files in the repository, classifying them by type (Atomic Topic, Action-Oriented, Theory) so we can eventually restructure them into a database of specific skills and materials.\n\n"
    
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
        <h1>Content & Atomic File Plan</h1>
        <p>A master tracker of all repository files categorized by their purpose.</p>
    </header>
    <section>
"""

    for directory in sorted_dirs:
        md_output += f"## Directory: `{directory}`\n\n"
        md_output += "| File | Title | Classification | Summary |\n"
        md_output += "|---|---|---|---|\n"
        
        html_output += f"<h2>Directory: {directory}</h2>\n<table>\n"
        html_output += "<tr><th>File</th><th>Title</th><th>Classification</th><th>Summary</th></tr>\n"
        
        for item in sorted(modules[directory], key=lambda x: x['file']):
            md_output += f"| `{os.path.basename(item['file'])}` | {item['title']} | **{item['class']}** | {item['summary']} |\n"
            
            tag_class = ""
            if item['class'] == "Module Theory & Structure": tag_class = "tag-theory"
            elif item['class'] == "Action Oriented": tag_class = "tag-action"
            elif item['class'] == "Location Data": tag_class = "tag-location"
            else: tag_class = "tag-atomic"
            
            html_output += f"<tr><td><a href='../{item['file']}'>{os.path.basename(item['file'])}</a></td><td>{item['title']}</td><td><span class='{tag_class}'>{item['class']}</span></td><td>{item['summary']}</td></tr>\n"
            
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
