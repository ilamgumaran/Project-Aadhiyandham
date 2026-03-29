import os
import re

def update_atlas_nav():
    source_dir = "html/candidate_locations"
    html_files = sorted([f for f in os.listdir(source_dir) if f.endswith(".html") and f != "index.html"])
    
    for i, filename in enumerate(html_files):
        file_path = os.path.join(source_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        prev_link = html_files[i-1] if i > 0 else "index.html"
        next_link = html_files[i+1] if i < len(html_files) - 1 else "index.html"
        
        # New navigation block
        new_nav = f"""    <div class="nav">
        <span>Previous: <a href="{prev_link}">Previous Location</a></span>
        <span><a href="index.html">Back to Atlas Index</a></span>
        <span>Next: <a href="{next_link}">Next Location</a></span>
    </div>"""
        
        # Replace the nav div
        updated_content = re.sub(r'<div class="nav">.*?</div>', new_nav, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated {file_path}")

if __name__ == "__main__":
    update_atlas_nav()
