import os
import re
from html.parser import HTMLParser

# 1. Parse Glossary.md to build a dictionary
glossary_dict = {}
with open('Glossary.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        match = re.match(r'\*\s+\*\*([^*]+)\*\*:\s+(.*)', line)
        if match:
            term = match.group(1).strip()
            # Handle terms with Tamil parentheticals
            clean_term = re.sub(r'\(.*\)', '', term).strip()
            definition = match.group(2).strip()
            glossary_dict[clean_term] = definition

# 2. Add extra common technical terms that might be missed
extra_terms = {
    "Pathogen": "An organism (like a bacterium or virus) that causes disease.",
    "Wrought Iron": "A tough, malleable form of iron suitable for forging and rolling, rather than casting.",
    "Solar Window": "The specific area of the sky through which the sun passes during the day, critical for site heating.",
    "Topography": "The arrangement of the natural and artificial physical features of an area.",
    "Orography": "The branch of physical geography dealing with mountains.",
    "Declination": "The angle between magnetic north and true north.",
    "Bearing": "The direction or path along which something moves or lies, measured in degrees.",
    "Triangulation": "A way of determining something's location using the locations of other things.",
    "SI System": "The International System of Units (Metric), used for logical and universal measurement.",
    "E-Prime": "A version of English that excludes the verb 'to be' to focus on objective actions."
}
glossary_dict.update(extra_terms)

def get_definitions_for_page(text):
    found = {}
    
    # Simple check for each term in the text (case-insensitive)
    for term, definition in glossary_dict.items():
        if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
            found[term] = definition
            
    # Recursive check: check if any words in the definitions also have definitions
    iterations = 0
    while iterations < 2: # Limit recursion
        new_terms = {}
        combined_defs = " ".join(found.values())
        for term, definition in glossary_dict.items():
            if term not in found and re.search(r'\b' + re.escape(term) + r'\b', combined_defs, re.IGNORECASE):
                new_terms[term] = definition
        if not new_terms:
            break
        found.update(new_terms)
        iterations += 1
        
    return found

def update_html_files():
    html_root = "html"
    for root, dirs, files in os.walk(html_root):
        for file in files:
            if file.endswith(".html") and file != "index.html":
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Strip existing glossary if re-running
                content = re.sub(r'<section class="vocabulary">.*?</section>', '', content, flags=re.DOTALL)
                
                # Get definitions
                defs = get_definitions_for_page(content)
                if not defs:
                    continue
                
                # Build HTML section
                glossary_html = '<section class="vocabulary">\n        <hr>\n        <h2>Vocabulary of the Foundation</h2>\n        <dl>\n'
                for term in sorted(defs.keys()):
                    glossary_html += f'            <dt><strong>{term}</strong></dt>\n            <dd>{defs[term]}</dd>\n'
                glossary_html += '        </dl>\n    </section>\n'
                
                # Insert before navigation or footer
                if '<div class="nav">' in content:
                    new_content = content.replace('<div class="nav">', glossary_html + '    <div class="nav">')
                else:
                    new_content = content.replace('</footer>', glossary_html + '</footer>')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added vocabulary to {file_path}")

# 3. Add CSS for vocabulary list
def update_css():
    css_path = "html/style.css"
    with open(css_path, 'r') as f:
        if '.vocabulary' in f.read(): return
    
    with open(css_path, 'a') as f:
        f.write("\n.vocabulary dl { margin-top: 20px; }\n.vocabulary dt { font-weight: bold; color: var(--accent); margin-top: 10px; }\n.vocabulary dd { margin-left: 20px; font-size: 0.95em; color: #555; }\n")

if __name__ == "__main__":
    update_html_files()
    update_css()
