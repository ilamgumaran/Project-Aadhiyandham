import os
import re

master_sequence = [
    "01_The_Journey/01_Rationale_and_Importance",
    "01_The_Journey/02_Orienting_and_Positioning",
    "01_The_Journey/03_Direction_and_Orientation_Basics",
    "01_The_Journey/04_Terrestrial_Navigation/01_Rationale_and_Importance",
    "01_The_Journey/04_Terrestrial_Navigation/02_Map_and_Compass_Guide",
    "01_The_Journey/04_Terrestrial_Navigation/03_Celestial_Navigation_Sun",
    "01_The_Journey/04_Terrestrial_Navigation/04_Non_Motorized_Transit_Routes",
    "01_The_Journey/05_Essential_Packing_List",
    "02_The_Site/01_Rationale_and_Importance",
    "02_The_Site/02_Topographical_Resilience",
    "02_The_Site/03_Solar_and_Thermal_Balance",
    "02_The_Site/04_Water_Sovereignty_and_Hydrams",
    "02_The_Site/05_Initial_Site_Layout",
    "03_The_Arrival/01_Rationale_and_Importance",
    "03_The_Arrival/02_Bio_Security_and_Water",
    "03_The_Arrival/03_Shelter_and_Thermal_Grounding",
    "03_The_Arrival/04_Emergency_Nutrition",
    "03_The_Arrival/05_Psychological_Grounding",
    "03_The_Arrival/06_Emergency_Sanitation",
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

def format_label(text):
    return text.replace('_', ' ').title()

def get_breadcrumbs(current_path, index):
    parts = current_path.split('/')
    depth = len(parts) - 1
    root_rel = '../' * depth
    
    # Path trail
    trail = [f'<a href="{root_rel}index.html">Index</a>']
    current_acc = ""
    for i, part in enumerate(parts[:-1]):
        current_acc += part + "/"
        label = format_label(part)
        # Assuming rationale is the index of each subdir
        link = f"{root_rel}{current_acc}01_Rationale_and_Importance.html"
        trail.append(f'<a href="{link}">{label}</a>')
    
    # Current page number
    page_num = f"Page {index + 1} of {len(master_sequence)}"
    trail.append(f'<span>{format_label(parts[-1])}</span>')
    
    return f'<div class="breadcrumbs">{" &gt; ".join(trail)} | <strong>{page_num}</strong></div>'

def update_file(idx):
    path = master_sequence[idx]
    html_path = f"html/{path}.html"
    if not os.path.exists(html_path): return

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    bc = get_breadcrumbs(path, idx)
    
    # Insert after <header>
    if '<div class="breadcrumbs">' in content:
        content = re.sub(r'<div class="breadcrumbs">.*?</div>', bc, content, flags=re.DOTALL)
    else:
        content = content.replace('</header>', f'</header>\n    {bc}')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added breadcrumbs to {html_path}")

for i in range(len(master_sequence)):
    update_file(i)
