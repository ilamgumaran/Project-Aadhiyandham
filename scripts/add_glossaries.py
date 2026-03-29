import os
import re
import string

# Core glossary + extensive extra terms to ensure every page gets definitions
glossary_dict = {
    # Original Glossary
    "Aadhiyandham": "A Tamil portmanteau of Aadhi (Primordial Beginning) and Andham (Final End).",
    "Acoustic Sovereignty": "The intentional management of a settlement's soundscape.",
    "Allicin": "The potent antibacterial and antifungal compound created when raw garlic is crushed.",
    "Annealing": "The process of slowly cooling synthesized materials in a controlled environment.",
    "Biochar": "A highly porous form of charcoal produced through pyrolysis.",
    "Biomimicry": "The practice of learning from and emulating nature’s strategies.",
    "Blissful Curiosity": "The primary motivation of the Aadhiyandham citizen.",
    "Bloomery": "A type of furnace used for smelting iron from its oxides.",
    "Centered Null": "The psychological baseline of Aadhiyandham.",
    "Circadian Rhythm": "The internal 24-hour biological clock.",
    "Crucible Steel": "A high-carbon steel produced by co-fusing wrought iron and organic carbon.",
    "Wootz": "A high-carbon steel produced by co-fusing wrought iron and organic carbon.",
    "E-Prime": "A version of the English language that excludes all forms of the verb 'to be'.",
    "Entropy": "The universal tendency toward disorder and the loss of useful energy.",
    "Glymphatic System": "The brain's waste clearance system.",
    "Gravity-Fed": "Any system that utilizes the earth's gravitational pull instead of electrical power.",
    "Heirloom Seeds": "Open-pollinated plant varieties passed down through generations.",
    "Hydraulic Ram Pump": "A cyclic water pump that uses the 'water hammer' effect.",
    "Hydram": "A cyclic water pump that uses the 'water hammer' effect.",
    "Liebig’s Law": "The principle that growth is controlled by the scarcest resource.",
    "Line-Shaft": "A power transmission system using a central rotating shaft.",
    "Pyrolysis": "The thermochemical decomposition of organic material at elevated temperatures.",
    "Recycling Cliff": "The projected point in time when salvaged old-world materials will corrode.",
    "Refugia": "Geographical areas that remain life-supporting during periods of disruption.",
    "Schmutzdecke": "The essential biological slime layer that forms on top of a Slow Sand Filter.",
    "Serotonin": "A neurotransmitter triggered by morning sunlight.",
    "Silvopasture": "The intentional integration of trees, forage plants, and livestock.",
    "Terra Preta": "A human-made, highly fertile soil type characterized by high concentrations of biochar.",
    "Thermal Belt": "A horizontal zone on a mountain slope where nighttime temperatures remain warmer.",
    
    # Extra technical/geographical terms
    "Topography": "The arrangement of the natural and artificial physical features of an area.",
    "Pathogen": "An organism (like a bacterium or virus) that causes disease.",
    "Wrought Iron": "A tough, malleable form of iron suitable for forging and rolling.",
    "Solar Window": "The specific area of the sky through which the sun passes during the day.",
    "Orography": "The branch of physical geography dealing with mountains.",
    "Declination": "The angle between magnetic north and true north.",
    "Bearing": "The direction or path along which something moves or lies, measured in degrees.",
    "Triangulation": "A way of determining something's location using the locations of other things.",
    "Contour Line": "A line on a map joining points of equal height above or below sea level.",
    "Line of Sight": "An imaginary straight line connecting the observer's eye to a specific landmark.",
    "Latrine": "A toilet or outhouse, especially a communal one in a camp.",
    "Micro-climate": "The climate of a very small or restricted area, especially when this differs from the climate of the surrounding area.",
    "Nitrogen-fixing": "The chemical processes by which atmospheric nitrogen is assimilated into organic compounds.",
    "Swale": "A shady, usually moist depression in the landscape used to capture water.",
    "Compost": "Decayed organic material used as a plant fertilizer.",
    "Leeward": "The side sheltered or away from the wind.",
    "Windward": "The side or direction from which the wind is blowing.",
    "Thermal Mass": "A material's resistance to fluctuations in temperature, acting as a heat battery.",
    "Inoculation": "The introduction of microorganisms into an environment (like soil or biochar) where they will grow and reproduce.",
    "Baseplate Compass": "A liquid-filled compass mounted on a clear plastic base, used with maps.",
    "Tinder": "Dry, flammable material, such as wood or paper, used for lighting a fire.",
    "Macronutrient": "A type of food (e.g. fat, protein, carbohydrate) required in large amounts in the diet.",
    "Decadal": "Relating to or covering a period of a decade (ten years).",
    "Sentinel": "A recognizable natural or artificial feature used for navigation.",
    "Sanitation": "Conditions relating to public health, especially the provision of clean drinking water and adequate sewage disposal.",
    "Resilience": "The capacity to withstand or to recover quickly from difficulties; toughness.",
    "Forage": "Bulky food such as grass or hay for horses and cattle; or the act of searching for wild food resources."
}

def get_definitions_for_page(text):
    found = {}
    # To avoid matching inside HTML tags, strip HTML tags for the search text
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    
    # We want whole word match only
    for term, definition in glossary_dict.items():
        pattern = r'\b' + re.escape(term) + r'\b'
        if re.search(pattern, clean_text, re.IGNORECASE):
            found[term] = definition
            
    return found

def update_html_files():
    html_root = "html"
    count = 0
    for root, dirs, files in os.walk(html_root):
        for file in files:
            if file.endswith(".html") and file != "index.html":
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Strip existing vocabulary section
                content = re.sub(r'<section class="vocabulary">.*?</section>', '', content, flags=re.DOTALL)
                
                defs = get_definitions_for_page(content)
                
                # If no definitions were found, add a fallback generic definition to ensure EVERY page has one
                if not defs:
                    defs["Aadhiyandham"] = glossary_dict["Aadhiyandham"]
                
                # Build HTML section
                glossary_html = '<section class="vocabulary" style="margin-top: 2em; padding: 1em; background-color: #f9f9f9; border-top: 2px solid #ccc;">\n'
                glossary_html += '    <h2>Vocabulary and Definitions</h2>\n'
                glossary_html += '    <dl>\n'
                for term in sorted(defs.keys()):
                    glossary_html += f'        <dt style="font-weight: bold; color: #2c3e50; margin-top: 10px;">{term}</dt>\n'
                    glossary_html += f'        <dd style="margin-left: 20px; font-size: 0.95em; color: #555;">{defs[term]}</dd>\n'
                glossary_html += '    </dl>\n'
                glossary_html += '</section>\n'
                
                # Insert just before the <div class="nav"> at the bottom, or before </body>
                if '<div class="nav">' in content:
                    new_content = content.replace('<div class="nav">', glossary_html + '    <div class="nav">')
                else:
                    new_content = content.replace('</body>', glossary_html + '</body>')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
    print(f"Added/Updated vocabulary on {count} pages.")

if __name__ == "__main__":
    update_html_files()
