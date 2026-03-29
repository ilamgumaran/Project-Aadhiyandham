import os
import re

SPECIFIC_FILES = {
    "02_The_Site": "02_Topographical_Resilience.md", # Wait, 02_The_Site specific guide was originally Topographical? Let me check what it was. Actually, the original guide was Site Selection & Setup. Let's just fix Ecosystem for now, or all of them.
}

# In `add_practical_guide.py`, the specific guides were for:
# - 01_The_Journey (all)
# - 02_The_Site (all)
# - 06_The_Ecosystem (all)

# Actually, the user specifically mentioned "The Terra Preta this seem to be on many pages, keep it only on the relevant pages"

# Let's write a script that reverts the specific MD guides back to DEFAULT_MD_GUIDE if they are NOT the target files.
# Let's map out the targets for the MD files.

TARGET_MD_FILES = {
    "01_The_Journey": "01_The_Journey/02_Orienting_and_Positioning.md",  # Actually, The Journey guide is broadly applicable to transit. But let's keep it broad or just leave it.
    "02_The_Site": "02_The_Site/05_Initial_Site_Layout.md", 
    "06_The_Ecosystem": "06_The_Ecosystem/02_Soil_Sovereignty.md"
}

DEFAULT_MD_GUIDE = """
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
"""

def fix_md_guides():
    for root, dirs, files in os.walk("."):
        if ".git" in root or "html" in root:
            continue
            
        for file in files:
            if not file.endswith(".md"):
                continue
                
            folder_name = os.path.basename(root)
            
            # We only care about the folders that had specific guides injected: 02_The_Site and 06_The_Ecosystem
            if folder_name in ["02_The_Site", "06_The_Ecosystem"]:
                filepath = os.path.join(root, file)
                
                # Check if this is the target file
                is_target = False
                if filepath.endswith(TARGET_MD_FILES[folder_name]):
                    is_target = True
                    
                if not is_target:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Find the practical guide block in MD
                    pattern = r'\n---\n## 🚀 Practical Implementation Guide for Beginners.*'
                    
                    if re.search(pattern, content, flags=re.DOTALL):
                        new_content = re.sub(pattern, DEFAULT_MD_GUIDE, content, flags=re.DOTALL)
                        
                        # Strip trailing newlines to match style
                        new_content = new_content.strip() + "\n"
                        
                        if content != new_content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Reverted to default MD guide: {filepath}")

if __name__ == "__main__":
    fix_md_guides()
