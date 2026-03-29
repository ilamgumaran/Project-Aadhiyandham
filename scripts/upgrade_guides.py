import os
import re

MODULE_CONTENT = {
    "02_The_Site": {
        "svg": """
        <div class="diagram" style="margin: 20px 0; padding: 15px; background: #fff; border: 1px solid #ddd; border-radius: 8px;">
            <h3>Reference Diagram: The Solar Window & Thermal Mass</h3>
            <svg width="100%" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
                <!-- Sky -->
                <rect width="500" height="250" fill="#e0f7fa"/>
                <!-- Sun Path -->
                <path d="M 50 200 Q 250 20 450 200" fill="none" stroke="#ffa000" stroke-width="2" stroke-dasharray="5,5"/>
                <circle cx="150" cy="80" r="15" fill="#ffeb3b"/>
                <text x="120" y="55" font-size="12" font-weight="bold">Winter Sun (Low)</text>
                <circle cx="250" cy="30" r="15" fill="#ffeb3b"/>
                <text x="210" y="15" font-size="12" font-weight="bold">Summer Sun (High)</text>
                <!-- House -->
                <polygon points="250,150 200,200 300,200" fill="#8d6e63"/>
                <rect x="210" y="200" width="80" height="50" fill="#d7ccc8"/>
                <rect x="260" y="210" width="20" height="30" fill="#a1887f"/> <!-- Door -->
                <!-- Thermal Mass -->
                <rect x="210" y="240" width="80" height="10" fill="#5d4037"/>
                <text x="220" y="248" font-size="8" fill="#fff">THERMAL MASS</text>
                <!-- Trees/Windbreak -->
                <path d="M 100 250 L 100 150 L 80 180 L 100 130 L 120 180 Z" fill="#2e7d32"/>
                <path d="M 70 250 L 70 170 L 50 200 L 70 150 L 90 200 Z" fill="#388e3c"/>
                <text x="40" y="140" font-size="10" font-weight="bold">Windbreak (North)</text>
            </svg>
            <p><em>Always position your primary structure facing the equator (South in the Northern Hemisphere, North in the Southern) to maximize winter solar heat gain, while using natural tree lines to block cold prevailing winds.</em></p>
        </div>
        """,
        "guide": """
    <h3>Detailed Action Plan</h3>
    <ul>
        <li><strong>Phase 1: Observation (Days 1-7):</strong> Do not dig immediately. Observe the land at dawn, noon, and dusk. Track where the frost melts first—this is your micro-climate thermal belt.</li>
        <li><strong>Phase 2: Hydrology Check:</strong> Dig a 1-meter test pit. If it fills with water, the water table is too high for a subterranean shelter. Move up the slope.</li>
        <li><strong>Phase 3: The Windbreak:</strong> Before building your main shelter, construct a temporary woven-branch wall (wattle) on the windward side to reduce wind chill by up to 15 degrees.</li>
    </ul>
    <h3>Advanced Troubleshooting</h3>
    <ul>
        <li><strong>Poor Drainage:</strong> If water pools around your shelter after rain, immediately dig a "French drain" (a trench filled with gravel) leading water downhill away from the foundation.</li>
    </ul>
"""
    },
    "03_The_Arrival": {
        "svg": """
        <div class="diagram" style="margin: 20px 0; padding: 15px; background: #fff; border: 1px solid #ddd; border-radius: 8px;">
            <h3>Reference Diagram: Emergency Bio-Sand Water Filter</h3>
            <svg width="100%" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
                <!-- Container -->
                <path d="M 150 50 L 250 50 L 230 250 L 170 250 Z" fill="none" stroke="#333" stroke-width="3"/>
                <!-- Layers -->
                <polygon points="155,70 245,70 240,110 160,110" fill="#a1887f"/>
                <text x="260" y="95" font-size="12">1. Coarse Gravel (Removes large debris)</text>
                
                <polygon points="160,110 240,110 235,160 165,160" fill="#d7ccc8"/>
                <text x="260" y="140" font-size="12">2. Fine Sand (Filters pathogens)</text>
                
                <polygon points="165,160 235,160 232,200 168,200" fill="#424242"/>
                <text x="260" y="185" font-size="12">3. Crushed Charcoal (Removes toxins/tastes)</text>
                
                <polygon points="168,200 232,200 230,240 170,240" fill="#e0e0e0"/>
                <text x="260" y="225" font-size="12">4. Cotton/Cloth Layer</text>
                
                <!-- Water Drops -->
                <circle cx="200" cy="270" r="5" fill="#2196F3"/>
                <circle cx="200" cy="285" r="5" fill="#2196F3"/>
                <text x="220" y="280" font-size="12" font-weight="bold" fill="#2196F3">Clean Water (Must still be boiled!)</text>
            </svg>
            <p><em>This field-expedient filter will remove 90% of particulate matter and many heavy metals, but it does NOT kill viruses. Always bring filtered water to a rolling boil for 1 minute before drinking.</em></p>
        </div>
        """,
        "guide": """
    <h3>Detailed Action Plan</h3>
    <ul>
        <li><strong>Hour 1-4 (Security):</strong> Establish a perimeter. Identify the nearest water source and designate a latrine area at least 60 meters downhill from it.</li>
        <li><strong>Hour 4-12 (Shelter & Fire):</strong> Build a "debris hut" or string up a tarp. Gather 3x the amount of firewood you think you need before dark.</li>
        <li><strong>Day 2-5 (Water Sovereignty):</strong> Construct the Bio-Sand filter (see diagram) using a hollow log, plastic bucket, or clothing. Boil all water.</li>
    </ul>
    <h3>Advanced Troubleshooting</h3>
    <ul>
        <li><strong>Fire Failure:</strong> If wood is too wet to burn, look for standing deadwood or peel the outer bark off branches to reach the dry heartwood. Use a knife to make "feather sticks" for tinder.</li>
    </ul>
"""
    },
    "06_The_Ecosystem": {
        "svg": """
        <div class="diagram" style="margin: 20px 0; padding: 15px; background: #fff; border: 1px solid #ddd; border-radius: 8px;">
            <h3>Reference Diagram: The Terra Preta (Biochar) Trench</h3>
            <svg width="100%" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
                <!-- Ground -->
                <rect x="0" y="100" width="500" height="150" fill="#795548"/>
                <path d="M 0 100 Q 250 110 500 100" fill="none" stroke="#4e342e" stroke-width="2"/>
                
                <!-- Trench -->
                <path d="M 150 100 L 200 200 L 300 200 L 350 100 Z" fill="#3e2723"/>
                
                <!-- Fire/Biochar -->
                <polygon points="210,190 290,190 270,120 250,150 230,120" fill="#ff5722"/>
                <polygon points="200,200 300,200 320,180 180,180" fill="#212121"/>
                
                <!-- Dirt cover -->
                <path d="M 120 90 Q 250 60 380 90" fill="none" stroke="#795548" stroke-width="10" stroke-dasharray="20,10"/>
                
                <text x="180" y="230" font-size="14" fill="#fff" font-weight="bold">Restricted Oxygen Burn</text>
                
                <!-- Labels -->
                <line x1="320" y1="190" x2="400" y2="150" stroke="#fff" stroke-width="2"/>
                <text x="410" y="150" font-size="12" fill="#fff">1. Pyrolysis Zone (Charcoal)</text>
                
                <line x1="280" y1="130" x2="380" y2="80" stroke="#fff" stroke-width="2"/>
                <text x="390" y="80" font-size="12">2. Soil/Sod Cover to choke smoke</text>
            </svg>
            <p><em>Biochar (Terra Preta) acts as a microscopic sponge for water and nutrients. By burning wood in a low-oxygen trench, you create carbon structures that will maintain soil fertility for thousands of years.</em></p>
        </div>
        """,
        "guide": """
    <h3>Detailed Action Plan</h3>
    <ul>
        <li><strong>Phase 1: The Char Pit:</strong> Dig a cone-shaped pit. Start a fire at the bottom. As the wood turns white-hot, bury it in dirt to cut off the oxygen, creating biochar instead of ash.</li>
        <li><strong>Phase 2: Inoculation:</strong> Crush the charcoal into pea-sized pieces. DO NOT put it straight into the garden. Soak it in liquid compost tea or urine for 2 weeks so it absorbs nutrients.</li>
        <li><strong>Phase 3: The Three Sisters:</strong> Plant using indigenous knowledge—Corn provides a stalk, Beans climb the stalk and fix nitrogen, and Squash leaves cover the ground to prevent weeds and retain moisture.</li>
    </ul>
    <h3>Advanced Troubleshooting</h3>
    <ul>
        <li><strong>Nitrogen Lockup:</strong> If your plant leaves turn yellow after adding biochar, you didn't inoculate it properly. Add a layer of fresh manure or nitrogen-rich grass clippings immediately.</li>
    </ul>
"""
    },
    "07_The_Mechanics": {
        "svg": """
        <div class="diagram" style="margin: 20px 0; padding: 15px; background: #fff; border: 1px solid #ddd; border-radius: 8px;">
            <h3>Reference Diagram: The Basic Line-Shaft Power System</h3>
            <svg width="100%" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
                <!-- Water Wheel -->
                <circle cx="100" cy="150" r="60" fill="none" stroke="#795548" stroke-width="10"/>
                <line x1="100" y1="90" x2="100" y2="210" stroke="#795548" stroke-width="4"/>
                <line x1="40" y1="150" x2="160" y2="150" stroke="#795548" stroke-width="4"/>
                <line x1="55" y1="105" x2="145" y2="195" stroke="#795548" stroke-width="4"/>
                <line x1="55" y1="195" x2="145" y2="105" stroke="#795548" stroke-width="4"/>
                <!-- Water -->
                <path d="M 0 200 Q 100 220 200 200" fill="none" stroke="#2196F3" stroke-width="15"/>
                <!-- Shaft -->
                <rect x="100" y="145" width="300" height="10" fill="#424242"/>
                <!-- Pulleys -->
                <ellipse cx="250" cy="150" rx="10" ry="30" fill="#616161"/>
                <ellipse cx="350" cy="150" rx="15" ry="40" fill="#616161"/>
                <!-- Belts -->
                <path d="M 250 120 L 250 50" stroke="#333" stroke-width="2" stroke-dasharray="4,2"/>
                <path d="M 250 180 L 250 220" stroke="#333" stroke-width="2" stroke-dasharray="4,2"/>
                <text x="210" y="40" font-size="12">To Sawmill / Lathe</text>
                <text x="210" y="240" font-size="12">To Grindstone</text>
                <text x="360" y="110" font-size="12" font-weight="bold">Step-Up Gearing (Increases RPM)</text>
            </svg>
            <p><em>A centralized power source (water or animal) turning a single overhead steel or hardwood shaft. Leather or canvas belts transfer this rotational energy to individual tools, forming the backbone of pre-electric industrialization.</em></p>
        </div>
        """,
        "guide": """
    <h3>Detailed Action Plan</h3>
    <ul>
        <li><strong>Phase 1: Sourcing the Shaft:</strong> Locate the straightest, hardest wood available (Oak or Hickory) or scavenge a steel pipe from an abandoned vehicle/building.</li>
        <li><strong>Phase 2: Friction Reduction:</strong> You cannot run a system on raw friction. Carve bearing blocks from dense wood and lubricate them constantly with rendered animal fat or pressed seed oil.</li>
        <li><strong>Phase 3: The Belts:</strong> Cut continuous strips of thick leather. Sew the ends together tightly. Ensure there is a mechanism to "slip" the belt off the pulley to act as a clutch to stop a machine in an emergency.</li>
    </ul>
    <h3>Advanced Troubleshooting</h3>
    <ul>
        <li><strong>Belt Slippage:</strong> If the leather belt slips when cutting hard material, it is either too loose or too dry. Apply a mixture of pine pitch (rosin) and a tiny amount of oil to the belt to increase grip.</li>
    </ul>
"""
    }
}

DEFAULT_GUIDE = """
    <h3>Detailed Action Plan</h3>
    <ul>
        <li><strong>Phase 1: The Blueprint:</strong> Read the theoretical archives fully. Translate the concept into a physical drawing using charcoal or pencil before touching any raw materials.</li>
        <li><strong>Phase 2: The Prototype:</strong> Build a 1/10th scale model of the structure or system. Identify where the stress points are. If the model fails, the real thing will kill you.</li>
        <li><strong>Phase 3: Redundancy:</strong> Never rely on a single system for heat, water, or food. If you build a mechanical system, keep manual hand-tools preserved and oiled as a fallback.</li>
    </ul>
    <h3>Advanced Troubleshooting</h3>
    <ul>
        <li><strong>The "5 Whys" Method:</strong> When a system fails, ask "Why?" five times to reach the root cause. (e.g., The wall collapsed. Why? The wood rotted. Why? Water pooled. Why? No drainage trench. Fix the trench, not just the wall.)</li>
    </ul>
"""

def update_guides():
    for root, dirs, files in os.walk("html"):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                # Determine module
                folder_name = os.path.basename(root)
                module_data = MODULE_CONTENT.get(folder_name, None)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find the existing practical guide block
                pattern = r'(<div class="practical-guide"[^>]*>.*?<h2>.*?</h2>)(.*?)(</div>)'
                
                # Check if it has already been detailed (contains 'Detailed Action Plan')
                if 'Detailed Action Plan' in content:
                    continue

                if re.search(pattern, content, flags=re.DOTALL):
                    # We have a guide block to upgrade
                    svg_html = module_data['svg'] if module_data else ""
                    guide_html = module_data['guide'] if module_data else DEFAULT_GUIDE
                    
                    replacement = r'\1\n' + svg_html + '\n' + guide_html + '\n\\3'
                    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Upgraded guide in {filepath}")

if __name__ == "__main__":
    update_guides()
