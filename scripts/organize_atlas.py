import os
import glob
import shutil

def organize_atlas():
    base_dir = "Outcome_1_Locating_Refugia/03_Candidate_Atlas"
    continents = {
        "africa": "Africa",
        "asia": "Asia",
        "europe": "Europe",
        "oceania": "Oceania",
        "sa": "South_America",
        "usa": "North_America"
    }
    
    # Create continent directories
    for folder in continents.values():
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
        os.makedirs(os.path.join("html", base_dir, folder), exist_ok=True)
        
    md_files = glob.glob(os.path.join(base_dir, "*.md"))
    
    for filepath in md_files:
        filename = os.path.basename(filepath)
        if filename == "template_location.md":
            continue
            
        # Determine continent from prefix
        prefix = filename.split('_')[0]
        if prefix in continents:
            target_folder = continents[prefix]
            target_path = os.path.join(base_dir, target_folder, filename)
            
            # Move the markdown file
            shutil.move(filepath, target_path)
            
            # Also move the corresponding HTML file if it exists
            html_filepath = os.path.join("html", base_dir, filename.replace(".md", ".html"))
            if os.path.exists(html_filepath):
                html_target_path = os.path.join("html", base_dir, target_folder, filename.replace(".md", ".html"))
                shutil.move(html_filepath, html_target_path)
                
    print("Candidate locations successfully organized by continent.")

if __name__ == "__main__":
    organize_atlas()
