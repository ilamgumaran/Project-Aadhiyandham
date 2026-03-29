import os
import glob

# Tailored instructions based on the module folder
GUIDES = {
    "01_The_Journey": {
        "md": """
---
## 🚀 Practical Implementation Guide for Beginners: The Journey

### 1. Step-by-Step Action Plan
*   **Preparation (Months 1-3):** Begin physical conditioning. Walk 5 miles a day with a 20lb backpack. Acquire baseplate compasses and physical topographical maps.
*   **Execution (Transit):** Never travel at night unless necessary. Establish a buddy system.
*   **Arrival:** When you reach the candidate location, establish a temporary perimeter before resting.

### 2. Troubleshooting & Failure Modes
*   **Lost Navigation:** If you lose your bearings, STOP. Do not wander. Use the shadow-stick method (Module 01.03) to find North and re-orient using a known landmark (river or mountain).
*   **Injury:** Have a designated medic. Prioritize stopping bleeding and stabilizing fractures before continuing.

### 3. Community & Decadal Flourishing
*   Ensure every adult and capable child knows how to read the map and use the compass. Redundancy is survival.
""",
        "html": """
<div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
    <h2>🚀 Practical Implementation Guide for Beginners: The Journey</h2>
    <h3>1. Step-by-Step Action Plan</h3>
    <ul>
        <li><strong>Preparation (Months 1-3):</strong> Begin physical conditioning. Walk 5 miles a day with a 20lb backpack. Acquire baseplate compasses and physical topographical maps.</li>
        <li><strong>Execution (Transit):</strong> Never travel at night unless necessary. Establish a buddy system.</li>
        <li><strong>Arrival:</strong> When you reach the candidate location, establish a temporary perimeter before resting.</li>
    </ul>
    <h3>2. Troubleshooting & Failure Modes</h3>
    <ul>
        <li><strong>Lost Navigation:</strong> If you lose your bearings, STOP. Do not wander. Use the shadow-stick method to find North and re-orient using a known landmark.</li>
        <li><strong>Injury:</strong> Have a designated medic. Prioritize stopping bleeding and stabilizing fractures before continuing.</li>
    </ul>
    <h3>3. Community & Decadal Flourishing</h3>
    <ul>
        <li>Ensure every adult and capable child knows how to read the map and use the compass. Redundancy is survival.</li>
    </ul>
</div>
"""
    },
    "02_The_Site": {
        "md": """
---
## 🚀 Practical Implementation Guide for Beginners: Site Selection & Setup

### 1. Step-by-Step Action Plan
*   **Day 1-3:** Survey the immediate 1km radius. Identify the primary fresh water source and the highest defensible/dry ground.
*   **Day 4-7:** Establish the "Initial Site Layout" (Module 02.05) using stakes and twine. Separate sanitation (latrines) from water sources by at least 100 meters downhill.
*   **Year 1:** Begin modifying the topography slightly with swales to catch rainwater and prevent soil erosion.

### 2. Troubleshooting & Failure Modes
*   **Water Contamination:** If water causes illness, immediately boil all drinking water and check upstream for animal carcasses or mineral runoff.
*   **Flooding:** If unexpected rain floods the camp, relocate to the pre-identified secondary high-ground.

### 3. Community & Decadal Flourishing
*   Plant long-lived tree species (Oak, Chestnut, Fruit trees) on the perimeter in Year 1. They will take decades to mature but will secure the micro-climate for future generations.
""",
        "html": """
<div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
    <h2>🚀 Practical Implementation Guide for Beginners: Site Selection & Setup</h2>
    <h3>1. Step-by-Step Action Plan</h3>
    <ul>
        <li><strong>Day 1-3:</strong> Survey the immediate 1km radius. Identify the primary fresh water source and the highest defensible/dry ground.</li>
        <li><strong>Day 4-7:</strong> Establish the Initial Site Layout using stakes and twine. Separate sanitation (latrines) from water sources by at least 100 meters downhill.</li>
        <li><strong>Year 1:</strong> Begin modifying the topography slightly with swales to catch rainwater and prevent soil erosion.</li>
    </ul>
    <h3>2. Troubleshooting & Failure Modes</h3>
    <ul>
        <li><strong>Water Contamination:</strong> If water causes illness, immediately boil all drinking water and check upstream for animal carcasses or mineral runoff.</li>
        <li><strong>Flooding:</strong> If unexpected rain floods the camp, relocate to the pre-identified secondary high-ground.</li>
    </ul>
    <h3>3. Community & Decadal Flourishing</h3>
    <ul>
        <li>Plant long-lived tree species (Oak, Chestnut, Fruit trees) on the perimeter in Year 1. They will take decades to mature but will secure the micro-climate for future generations.</li>
    </ul>
</div>
"""
    },
    "06_The_Ecosystem": {
        "md": """
---
## 🚀 Practical Implementation Guide for Beginners: The Ecosystem

### 1. Step-by-Step Action Plan
*   **Month 1:** Start a compost pile immediately. Collect all organic waste (excluding meat/dairy initially) and layer with dry carbon (leaves, straw).
*   **Month 3:** Begin creating Terra Preta (biochar). Dig a trench, burn wood with restricted oxygen, crush the char, and mix it with compost before adding to garden beds.
*   **Year 1:** Plant the 'Top 10 Staples' (Potatoes, Beans, Corn, Squash) from the seed bank. Save 20% of the yield strictly for next year's seeds.

### 2. Troubleshooting & Failure Modes
*   **Crop Failure (Pests):** Do not use chemical pesticides. Introduce companion planting (e.g., Marigolds with Tomatoes) and encourage natural predators like ladybugs and birds.
*   **Soil Depletion:** If yields drop, you are taking more than you give. Rest the bed, plant nitrogen-fixing cover crops (clover, beans), and double the compost application.

### 3. Community & Decadal Flourishing
*   Assign a "Keeper of the Seeds." Seed genetics adapt to your specific microclimate over decades. This is the true wealth of the settlement.
""",
        "html": """
<div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
    <h2>🚀 Practical Implementation Guide for Beginners: The Ecosystem</h2>
    <h3>1. Step-by-Step Action Plan</h3>
    <ul>
        <li><strong>Month 1:</strong> Start a compost pile immediately. Collect all organic waste and layer with dry carbon (leaves, straw).</li>
        <li><strong>Month 3:</strong> Begin creating Terra Preta (biochar). Mix crushed char with compost before adding to garden beds.</li>
        <li><strong>Year 1:</strong> Plant the 'Top 10 Staples' from the seed bank. Save 20% of the yield strictly for next year's seeds.</li>
    </ul>
    <h3>2. Troubleshooting & Failure Modes</h3>
    <ul>
        <li><strong>Crop Failure (Pests):</strong> Use companion planting and encourage natural predators. Avoid synthetic chemicals.</li>
        <li><strong>Soil Depletion:</strong> If yields drop, rest the bed, plant nitrogen-fixing cover crops, and double the compost application.</li>
    </ul>
    <h3>3. Community & Decadal Flourishing</h3>
    <ul>
        <li>Assign a "Keeper of the Seeds." Seed genetics adapt to your specific microclimate over decades. This is the true wealth of the settlement.</li>
    </ul>
</div>
"""
    },
    "default": {
        "md": """
---
## 🚀 Practical Implementation Guide for Beginners

### 1. Step-by-Step Action Plan
*   **Preparation:** Read this module fully before attempting to build or implement. Gather raw materials locally.
*   **Execution:** Build a small-scale prototype first. For example, if building a mechanical system or shelter, make a miniature version to test physics and material strength.
*   **Review:** Test the implementation under stress (wind, water, heavy use) and refine.

### 2. Troubleshooting & Failure Modes
*   **System Failure:** When a system breaks, apply the "5 Whys" technique to find the root cause (e.g., The gear broke. Why? It was made of soft wood. Why? We lacked hardwood. Why?). Fix the root cause, not just the symptom.
*   **Burnout:** Decadal survival is a marathon, not a sprint. If the community is exhausted, lower productivity expectations and focus on rest and social cohesion.

### 3. Community & Decadal Flourishing
*   **Apprenticeship:** No critical skill should be held by only one person. Every master must have an apprentice. Document local modifications to these original instructions in a physical journal.
""",
        "html": """
<div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">
    <h2>🚀 Practical Implementation Guide for Beginners</h2>
    <h3>1. Step-by-Step Action Plan</h3>
    <ul>
        <li><strong>Preparation:</strong> Read this module fully before attempting to build or implement. Gather raw materials locally.</li>
        <li><strong>Execution:</strong> Build a small-scale prototype first to test physics and material strength.</li>
        <li><strong>Review:</strong> Test the implementation under stress (wind, water, heavy use) and refine.</li>
    </ul>
    <h3>2. Troubleshooting & Failure Modes</h3>
    <ul>
        <li><strong>System Failure:</strong> When a system breaks, apply the "5 Whys" technique to find the root cause. Fix the root cause, not just the symptom.</li>
        <li><strong>Burnout:</strong> Decadal survival is a marathon. If exhausted, focus on rest and social cohesion.</li>
    </ul>
    <h3>3. Community & Decadal Flourishing</h3>
    <ul>
        <li><strong>Apprenticeship:</strong> No critical skill should be held by only one person. Document local modifications in a physical journal.</li>
    </ul>
</div>
"""
    }
}

def process_md_file(filepath):
    # Determine the context
    folder = filepath.split('/')[-2] if len(filepath.split('/')) > 1 else ""
    guide = GUIDES.get(folder, GUIDES["default"])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Practical Implementation Guide" in content:
        return # Already processed
        
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(guide["md"])

def process_html_file(filepath):
    folder = filepath.split('/')[-2] if len(filepath.split('/')) > 1 else ""
    guide = GUIDES.get(folder, GUIDES["default"])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Practical Implementation Guide" in content:
        return # Already processed
        
    # Inject before </section> if it exists, else before </body>
    if "</section>" in content:
        content = content.replace("</section>", guide["html"] + "\n    </section>")
    elif "</body>" in content:
        content = content.replace("</body>", guide["html"] + "\n</body>")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    print("Processing Markdown files...")
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                process_md_file(filepath)
                
    print("Processing HTML files...")
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                process_html_file(filepath)
    
    print("Done updating all files.")
