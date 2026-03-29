import os
import glob
import subprocess
import re

DIR_MAPPING = {
    "03_The_Arrival/07_Perimeter_Defense": "Outcome_3_Perimeter_Defense/01_Passive_Defense",
    "09_The_Next_Generation/08_Cultural_Technology": "Outcome_6_Flourishing_Civilization/01_Cultural_Technology",
    "01_The_Journey": "Outcome_1_Locating_Refugia/01_The_Journey",
    "02_The_Site": "Outcome_1_Locating_Refugia/02_The_Site",
    "03_The_Arrival": "Outcome_2_Biological_Sovereignty/03_The_Arrival",
    "04_The_Body": "Outcome_2_Biological_Sovereignty/04_The_Body",
    "06_The_Ecosystem": "Outcome_2_Biological_Sovereignty/06_The_Ecosystem",
    "05_The_Mind": "Outcome_4_Psychological_Centeredness/05_The_Mind",
    "07_The_Mechanics": "Outcome_5_Decadal_Resilience/07_The_Mechanics",
    "08_The_Society": "Outcome_5_Decadal_Resilience/08_The_Society",
    "09_The_Next_Generation": "Outcome_5_Decadal_Resilience/09_The_Next_Generation",
    "10_The_Archive": "Outcome_5_Decadal_Resilience/10_The_Archive",
    "11_The_Horizon": "Outcome_5_Decadal_Resilience/11_The_Horizon"
}

def get_new_path(old_path):
    for old_prefix, new_prefix in sorted(DIR_MAPPING.items(), key=lambda x: -len(x[0])):
        if old_path == old_prefix or old_path.startswith(old_prefix + "/"):
            return old_path.replace(old_prefix, new_prefix, 1)
    return old_path

def main():
    # 1. Gather all files
    md_files = glob.glob("**/*.md", recursive=True)
    html_files = glob.glob("html/**/*.html", recursive=True)
    
    all_files = md_files + html_files
    
    # Pre-calculate old to new mappings
    file_map = {}
    for f in all_files:
        if ".git" in f or "node_modules" in f:
            continue
        
        if f.startswith("html/"):
            rel = f[5:]
            new_rel = get_new_path(rel)
            if rel != new_rel:
                file_map[f] = "html/" + new_rel
        else:
            new_f = get_new_path(f)
            if f != new_f:
                file_map[f] = new_f

    # 2. Process links inside files BEFORE moving them
    for f in all_files:
        if ".git" in f or "node_modules" in f: continue
        if not os.path.isfile(f): continue
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        new_f = file_map.get(f, f)
        new_dir = os.path.dirname(new_f)
        
        def link_replacer(match):
            href = match.group(2)
            if href.startswith("http") or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:"):
                return match.group(0)
            
            # Resolve old absolute path
            old_abs = os.path.normpath(os.path.join(os.path.dirname(f), href))
            
            # Find what the new absolute path will be
            target_new_abs = file_map.get(old_abs, old_abs)
            
            # Calculate new relative path from the new directory
            try:
                new_href = os.path.relpath(target_new_abs, new_dir)
            except ValueError:
                new_href = href
                
            return match.group(1) + new_href + match.group(3)

        # Replace markdown links: [text](link)
        content = re.sub(r'(\[.*?\]\()([^)]+)(\))', link_replacer, content)
        # Replace html links: href="link"
        content = re.sub(r'(href=["\'])([^"^\']+)(["\'])', link_replacer, content)
        # Replace src="link"
        content = re.sub(r'(src=["\'])([^"^\']+)(["\'])', link_replacer, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

    # 3. Physically move the files using git mv
    for old_f in sorted(file_map.keys(), key=len, reverse=True):
        new_f = file_map[old_f]
        if os.path.exists(old_f):
            os.makedirs(os.path.dirname(new_f), exist_ok=True)
            subprocess.run(["git", "mv", old_f, new_f])
            
    # Clean up empty directories
    subprocess.run(["find", ".", "-type", "d", "-empty", "-delete"])
            
    print("Architecture refactored.")

if __name__ == "__main__":
    main()
