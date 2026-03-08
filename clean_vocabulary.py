import os
import re

def fix_duplicates():
    html_root = "html"
    count = 0
    for root, dirs, files in os.walk(html_root):
        for file in files:
            if file.endswith(".html") and file != "index.html":
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if there are multiple vocabulary sections
                if content.count('<section class="vocabulary"') > 1:
                    # Strip ALL existing vocabulary sections completely
                    content = re.sub(r'<section class="vocabulary".*?</section>', '', content, flags=re.DOTALL)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
    print(f"Cleaned up duplicates in {count} HTML pages.")

if __name__ == "__main__":
    fix_duplicates()
