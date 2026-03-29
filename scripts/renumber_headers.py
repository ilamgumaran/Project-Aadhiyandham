import os
import glob
import re

SKIP_FILES = {'index.html', 'content_plan.html', 'glossary.html', 'content_plan.md', 'Glossary.md'}

def clean_title(title):
    # Remove leading numbering like "1. ", "1.1 ", "01. ", "1 ", "1.1.1 "
    # Also handle leading HTML tags before the number
    cleaned = re.sub(r'^(\s*(?:<[^>]+>\s*)*)[\d]+[\d\.]*\s+', r'\1', title)
    return cleaned.strip()

def process_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    h2_counter = 0
    h3_counter = 0
    h4_counter = 0
    
    new_lines = []
    changed = False
    
    in_code_block = False
    
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
            
        if in_code_block:
            new_lines.append(line)
            continue
            
        if line.startswith('## '):
            h2_counter += 1
            h3_counter = 0
            h4_counter = 0
            content = clean_title(line[3:])
            new_line = f"## {h2_counter}. {content}\n"
            if line != new_line: changed = True
            new_lines.append(new_line)
        elif line.startswith('### '):
            h3_counter += 1
            h4_counter = 0
            content = clean_title(line[4:])
            prefix = f"{h2_counter}.{h3_counter}." if h2_counter > 0 else f"{h3_counter}."
            new_line = f"### {prefix} {content}\n"
            if line != new_line: changed = True
            new_lines.append(new_line)
        elif line.startswith('#### '):
            h4_counter += 1
            content = clean_title(line[5:])
            prefix = f"{h2_counter}.{h3_counter}.{h4_counter}." if h2_counter > 0 else f"{h3_counter}.{h4_counter}."
            new_line = f"#### {prefix} {content}\n"
            if line != new_line: changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    return changed

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    h2_counter = 0
    h3_counter = 0
    h4_counter = 0
    
    def header_replacer(match):
        nonlocal h2_counter, h3_counter, h4_counter
        tag = match.group(1).lower()
        attrs = match.group(2)
        inner_html = match.group(3)
        
        # Skip if the h2 is 'Vocabulary and Definitions' to not number global footer elements, or if it has class "alignment"
        if "Vocabulary and Definitions" in inner_html or "class=\"alignment\"" in attrs:
            return match.group(0)
            
        inner_html = clean_title(inner_html)
        
        if tag == 'h2':
            h2_counter += 1
            h3_counter = 0
            h4_counter = 0
            prefix = f"{h2_counter}. "
        elif tag == 'h3':
            h3_counter += 1
            h4_counter = 0
            prefix = f"{h2_counter}.{h3_counter}. " if h2_counter > 0 else f"{h3_counter}. "
        elif tag == 'h4':
            h4_counter += 1
            prefix = f"{h2_counter}.{h3_counter}.{h4_counter}. " if h2_counter > 0 else f"{h3_counter}.{h4_counter}. "
            
        return f"<{tag}{attrs}>{prefix}{inner_html}</{tag}>"

    pattern = re.compile(r'<(h2|h3|h4)([^>]*)>(.*?)</\1>', flags=re.IGNORECASE | re.DOTALL)
    new_content = pattern.sub(header_replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    md_files = glob.glob('**/*.md', recursive=True)
    md_count = 0
    for filepath in md_files:
        if any(skip in filepath for skip in SKIP_FILES) or '.git/' in filepath:
            continue
        if process_md(filepath):
            md_count += 1
        
    html_files = glob.glob('html/**/*.html', recursive=True)
    html_count = 0
    for filepath in html_files:
        if any(skip in filepath for skip in SKIP_FILES):
            continue
        if process_html(filepath):
            html_count += 1
            
    print(f"Renumbered {md_count} MD files and {html_count} HTML files.")

if __name__ == '__main__':
    main()
