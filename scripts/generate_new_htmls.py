import os
import re

from build_new_modules import MODULES, HTML_TEMPLATE, build_html_with_svgs

def md_to_html_simple(md_text):
    lines = md_text.split('\\n')
    html_lines = []
    in_list = False
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        if line.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if 'Practical Implementation Guide' in line:
                html_lines.append('<div class="practical-guide" style="margin-top: 2em; padding: 1em; background-color: #f4f8fb; border-left: 4px solid #2196F3;">')
                html_lines.append('<h2>' + line[3:] + '</h2>')
            elif 'Scientific Validation' in line:
                html_lines.append('<div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">')
                html_lines.append('<h3 style="color: #27ae60; margin-top: 0;">' + line[3:] + '</h3>')
            else:
                html_lines.append('<h2>' + line[3:] + '</h2>')
        elif line.startswith('### '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<h3>' + line[4:] + '</h3>')
        elif line.startswith('* ') or line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            li_content = line[2:]
            li_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', li_content)
            li_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', li_content)
            html_lines.append('<li>' + li_content + '</li>')
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
            # Hack for numbered lists
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            li_content = line[3:]
            li_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', li_content)
            li_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', li_content)
            html_lines.append('<li>' + li_content + '</li>')
        elif line == '---':
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<hr>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            p_content = line
            p_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_content)
            p_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_content)
            html_lines.append('<p>' + p_content + '</p>')
    if in_list:
        html_lines.append('</ul>')
    html_lines.append('</div>')
    return "\n".join(html_lines)


def generate_htmls():
    for rel_path, data in MODULES.items():
        md_path = f"{rel_path}.md"
        html_path = f"html/{rel_path}.html"
        
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        
        short_title = data["title"].split(':')[0]
        content_html = md_to_html_simple(data["md"])
        
        # Extract alignment
        align_match = re.search(r'\*\*Alignment:\*\* (.*)', data["md"])
        alignment = align_match.group(1) if align_match else ""
        
        final_html = HTML_TEMPLATE.format(
            title=data["title"],
            parent_name=data["parent_name"],
            short_title=short_title,
            content_html=content_html,
            alignment=alignment
        )
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(final_html)
            
        print(f"Generated base HTML {html_path}")
        
    # Now inject the SVGs
    build_html_with_svgs()

if __name__ == "__main__":
    generate_htmls()
