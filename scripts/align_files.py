import os
import glob
import re

def map_to_outcome(filepath):
    if "01_The_Journey" in filepath or "02_The_Site" in filepath or "candidate_locations" in filepath:
        return "Outcome 1: Locating and Connecting Optimal Refugia"
    elif "03_The_Arrival" in filepath or "04_The_Body" in filepath or "06_The_Ecosystem" in filepath:
        # Perimeter Defense got moved to Outcome 3
        if "03_The_Arrival/07_Perimeter_Defense" in filepath:
            return "Outcome 3: Perimeter Sovereignty and Passive Defense"
        return "Outcome 2: Absolute Biological Sovereignty"
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

def update_md(filepath, outcome):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "**Alignment:**" in content or "Foundational" in outcome or outcome == "Ignore":
        return False

    # Find the first H1 header and insert the alignment below it
    pattern = r'^(# .*?\n)'
    replacement = r'\1\n**Alignment:** ' + outcome + r'\n'
    
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def update_html(filepath, outcome):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "class=\"alignment\"" in content or "Foundational" in outcome or outcome == "Ignore":
        return False

    # Find the H1 inside the header and insert the alignment
    pattern = r'(<h1>.*?</h1>)'
    alignment_html = f'<p class="alignment" style="color: #2c3e50; font-weight: bold; background-color: #e8f4f8; padding: 5px 10px; border-radius: 4px; display: inline-block;">Alignment: {outcome}</p>'
    replacement = r'\1\n        ' + alignment_html
    
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    md_files = glob.glob('**/*.md', recursive=True)
    md_count = 0
    html_count = 0

    for filepath in md_files:
        if 'html/' in filepath or '.git/' in filepath:
            continue
        
        outcome = map_to_outcome(filepath)
        if update_md(filepath, outcome):
            md_count += 1
            
        # Try to find corresponding HTML file
        html_path = "html/" + filepath.replace(".md", ".html")
        if os.path.exists(html_path):
            if update_html(html_path, outcome):
                html_count += 1
                
    print(f"Updated {md_count} Markdown files and {html_count} HTML files with Alignment blocks.")

if __name__ == "__main__":
    main()
