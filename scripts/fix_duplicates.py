import os
import re

def remove_duplicates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML block starts with <div class="practical-guide"
    # and ends with </div> just before a </section> or </body>.
    # A robust way is to split the document by the start marker,
    # keep the first part and the second part (first occurrence),
    # and for any subsequent occurrences, strip out the block.

    marker = '<div class="practical-guide"'
    if content.count(marker) > 1:
        parts = content.split(marker)
        
        # Reconstruct the string
        new_content = parts[0] + marker + parts[1]
        
        for part in parts[2:]:
            # The part starts with the rest of the div. We need to find the end of this div.
            # Assuming the block ends at the first </div> that matches our structure, 
            # or we can use regex to remove the entire block.
            
            # Since our injected block is very specific, let's just use regex to remove all instances,
            # then inject it exactly once at the end of the first </section>
            pass
            
        # Better approach: remove ALL practical guide blocks, then re-insert it once.
        pass

    # Regex approach: Remove all occurrences of the practical guide block
    block_pattern_html = r'\s*<div class="practical-guide".*?</div>\s*'
    block_pattern_md = r'\n---\n## 🚀 Practical Implementation Guide for Beginners.*?(?=\n## |\Z)'
    
    # We'll use a precise non-greedy regex for HTML
    html_removed = re.sub(r'<div class="practical-guide".*?</div>', '', content, flags=re.DOTALL)
    
    if len(html_removed) != len(content) and filepath.endswith('.html'):
        # Re-insert the guide just before the final </section> before the <div class="nav">
        # Or before <section class="vocabulary"> if it exists
        # Let's read the block we just removed to save it
        match = re.search(r'<div class="practical-guide".*?</div>', content, flags=re.DOTALL)
        if match:
            guide_block = match.group(0)
            
            # Find the best insertion point
            if '<section class="vocabulary">' in html_removed:
                new_content = html_removed.replace('<section class="vocabulary">', guide_block + '\n\n    <section class="vocabulary">')
            elif '</section>' in html_removed:
                # insert at the last </section> before footer/nav
                parts = html_removed.rsplit('</section>', 1)
                new_content = parts[0] + '\n' + guide_block + '\n    </section>' + parts[1]
            else:
                new_content = html_removed.replace('</body>', guide_block + '\n</body>')
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Fixed duplicates in {filepath}")

def process_all():
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                remove_duplicates(filepath)

if __name__ == "__main__":
    process_all()
