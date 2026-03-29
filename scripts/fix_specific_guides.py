import os
import re

SPECIFIC_FILES = {
    "02_The_Site": "03_Solar_and_Thermal_Balance.html",
    "03_The_Arrival": "02_Bio_Security_and_Water.html",
    "06_The_Ecosystem": "02_Soil_Sovereignty.html",
    "07_The_Mechanics": "02_Mechanical_Power.html"
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

def fix_guides():
    for root, dirs, files in os.walk("html"):
        for file in files:
            if not file.endswith(".html"):
                continue
                
            folder_name = os.path.basename(root)
            if folder_name in SPECIFIC_FILES:
                target_file = SPECIFIC_FILES[folder_name]
                
                # If this file is NOT the target file, revert its guide to DEFAULT_GUIDE
                if file != target_file:
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Find the practical guide div and its inner content
                    pattern = r'(<div class="practical-guide"[^>]*>.*?<h2>.*?</h2>)(.*?)(</div>)'
                    
                    if re.search(pattern, content, flags=re.DOTALL):
                        # We replace the middle group \2 with DEFAULT_GUIDE
                        new_content = re.sub(pattern, r'\1\n' + DEFAULT_GUIDE + '\n\\3', content, flags=re.DOTALL)
                        
                        if content != new_content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Reverted to default guide: {filepath}")

if __name__ == "__main__":
    fix_guides()
