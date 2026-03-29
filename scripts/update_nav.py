import os
import re

# Master sequence of files (module_dir/filename without extension)
master_sequence = [
    "01_The_Journey/01_Rationale_and_Importance",
    "01_The_Journey/02_Transit_Guide_from_Georgia_USA",
    "01_The_Journey/03_Emergency_Family_Transit_Protocol",
    "02_The_Site/01_Rationale_and_Importance",
    "02_The_Site/02_Topographical_Resilience",
    "02_The_Site/03_Solar_and_Thermal_Balance",
    "02_The_Site/04_Water_Sovereignty_and_Hydrams",
    "03_The_Arrival/01_Rationale_and_Importance",
    "03_The_Arrival/02_Bio_Security_and_Water",
    "03_The_Arrival/03_Shelter_and_Thermal_Grounding",
    "03_The_Arrival/04_Emergency_Nutrition",
    "03_The_Arrival/05_Psychological_Grounding",
    "04_The_Body/01_Rationale_and_Importance",
    "04_The_Body/02_Biochemical_Signals",
    "04_The_Body/03_Temperate_Antibiotics",
    "05_The_Mind/01_Rationale_and_Importance",
    "05_The_Mind/02_Linguistic_Precision",
    "05_The_Mind/03_Restorative_Architecture",
    "06_The_Ecosystem/01_Rationale_and_Importance",
    "06_The_Ecosystem/02_Soil_Sovereignty",
    "06_The_Ecosystem/03_The_Seed_Bank",
    "06_The_Ecosystem/04_Livestock_and_Mechanical_Animals",
    "07_The_Mechanics/01_Rationale_and_Importance",
    "07_The_Mechanics/02_Mechanical_Power",
    "07_The_Mechanics/03_Low_Tech_Mobility",
    "07_The_Mechanics/04_Material_Synthesis_and_Recycling",
    "08_The_Society/01_Rationale_and_Importance",
    "08_The_Society/02_Recycling_Cliff",
    "08_The_Society/03_Consensus_Models",
    "09_The_Next_Generation/01_Rationale_and_Importance",
    "09_The_Next_Generation/02_English_Language_Lessons",
    "09_The_Next_Generation/03_Tamil_Language_Lessons",
    "09_The_Next_Generation/04_Metrics_and_Measurement",
    "09_The_Next_Generation/05_Mathematics_and_Geometry",
    "09_The_Next_Generation/06_Foundational_Science",
    "09_The_Next_Generation/07_Philosophy_and_Thought_Experiments",
    "10_The_Archive/01_Rationale_and_Importance",
    "10_The_Archive/02_Laws_of_Energy",
    "10_The_Archive/03_Limiting_Factors",
    "11_The_Horizon/01_Rationale_and_Importance",
    "11_The_Horizon/02_Glassmaking",
    "11_The_Horizon/03_Crucible_Steel"
]

def get_relative_path(current_path, target_path):
    curr_dir = current_path.split('/')[0]
    targ_dir, targ_file = target_path.split('/')
    if curr_dir == targ_dir:
        return f"{targ_file}.html"
    else:
        return f"../{targ_dir}/{targ_file}.html"

def update_html_nav(file_idx):
    current_full_path = master_sequence[file_idx]
    html_path = f"html/{current_full_path}.html"
    
    if not os.path.exists(html_path):
        print(f"File not found: {html_path}")
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine Previous link
    if file_idx == 0:
        prev_link = "../index.html"
        prev_label = "Index"
    else:
        prev_link = get_relative_path(current_full_path, master_sequence[file_idx-1])
        prev_label = master_sequence[file_idx-1].split('/')[1].replace('_', ' ')

    # Determine Next link
    if file_idx == len(master_sequence) - 1:
        next_link = "../index.html"
        next_label = "Index"
    else:
        next_link = get_relative_path(current_full_path, master_sequence[file_idx+1])
        next_label = master_sequence[file_idx+1].split('/')[1].replace('_', ' ')

    # Regex to replace the entire nav div
    new_nav = f"""    <div class="nav">
        <span>Previous: <a href="{prev_link}">{prev_label}</a></span>
        <span>Next: <a href="{next_link}">{next_label}</a></span>
    </div>"""
    
    # Simple replacement if div exists
    updated_content = re.sub(r'<div class="nav">.*?</div>', new_nav, content, flags=re.DOTALL)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated {html_path}")

for i in range(len(master_sequence)):
    update_html_nav(i)
