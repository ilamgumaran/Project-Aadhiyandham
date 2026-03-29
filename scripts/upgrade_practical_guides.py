import os
import glob
import re

def process_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the 🚀 icon from any header
    new_content = re.sub(r'(#+.*?)\s*🚀\s*', r'\1', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Remove the 🚀 icon
    if '🚀' in content:
        content = re.sub(r'🚀\s*', '', content)
        changed = True

    # Find the practical-guide div and remove it, keeping the inner content
    # and adding an <hr> before the <h2>. Also try to wrap h3 sections in <div class="how-to">.
    pattern = r'<div class="practical-guide"[^>]*>\s*(<h2.*?>.*?</h2>)(.*?)</div>'
    
    def replacer(match):
        h2 = match.group(1)
        inner = match.group(2)
        # split by <h3>
        parts = re.split(r'(<h3.*?>)', inner)
        new_inner = parts[0]
        for i in range(1, len(parts), 2):
            h3 = parts[i]
            body = parts[i+1]
            new_inner += f'\n        <div class="how-to">\n            {h3}{body}        </div>\n'
        return f'<hr>\n\n        {h2}\n{new_inner}'

    new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)
    if count > 0:
        content = new_content
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    md_files = glob.glob('**/*.md', recursive=True)
    md_count = 0
    for filepath in md_files:
        if 'html/' in filepath or '.git/' in filepath:
            continue
        if process_md(filepath):
            md_count += 1
            
    html_files = glob.glob('html/**/*.html', recursive=True)
    html_count = 0
    for filepath in html_files:
        if process_html(filepath):
            html_count += 1
            
    print(f"Updated {md_count} MD files and {html_count} HTML files to promote practical guides.")

if __name__ == '__main__':
    main()
