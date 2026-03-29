import os
import glob
import re

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>01 {short_title} - Project Aadhiyandham</title>
    <link rel="stylesheet" href="../../../style.css">
</head>
<body>
    <header>
        <p><a href="../../../index.html">Main Index</a></p>
        <h1>{title}</h1>
        <p class="alignment" style="color: #2c3e50; font-weight: bold; background-color: #e8f4f8; padding: 5px 10px; border-radius: 4px; display: inline-block;">Alignment: {alignment}</p>
    </header>

    <div class="breadcrumbs"><a href="../../../index.html">Index</a> &gt; <a href="../01_Rationale_and_Importance.html">04 The Body</a> &gt; <span>{short_title}</span></div>

    <section>
{content_html}
    </section>

    <div class="nav">
        <span>Previous: <a href="../01_Rationale_and_Importance.html">Rationale and Importance</a></span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>
"""

def md_to_html_simple(md_text):
    lines = md_text.split('\n')
    html_lines = []
    in_list = False
    for line in lines[1:]:
        line = line.strip()
        if not line or line.startswith('**Alignment:**'):
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
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. ') or line.startswith('4. ') or line.startswith('5. ') or line.startswith('6. ') or line.startswith('7. ') or line.startswith('8. '):
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
    if '<div class="practical-guide"' in "".join(html_lines):
        html_lines.append('</div>')
    return "\n".join(html_lines)


def process_file(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    title_match = re.search(r'^# (.*)', md_content)
    title = title_match.group(1) if title_match else "Document"
    short_title = title.split(':')[0]

    align_match = re.search(r'\*\*Alignment:\*\* (.*)', md_content)
    alignment = align_match.group(1) if align_match else "Outcome 2: Absolute Biological Sovereignty"

    content_html = md_to_html_simple(md_content)
    
    # Fix research validation closing div
    content_html = content_html.replace("<hr>\n<div class=\"practical-guide\"", "</div>\n<div class=\"practical-guide\"")

    final_html = HTML_TEMPLATE.format(
        title=title,
        short_title=short_title,
        alignment=alignment,
        content_html=content_html
    )

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

process_file("Outcome_2_Biological_Sovereignty/04_The_Body/04_Advanced_Trauma_Care/01_Advanced_Trauma_Care.md", "html/Outcome_2_Biological_Sovereignty/04_The_Body/04_Advanced_Trauma_Care/01_Advanced_Trauma_Care.html")
process_file("Outcome_2_Biological_Sovereignty/04_The_Body/07_Maternal_and_Neonatal_Care/01_Generational_Midwifery_and_Care.md", "html/Outcome_2_Biological_Sovereignty/04_The_Body/07_Maternal_and_Neonatal_Care/01_Generational_Midwifery_and_Care.html")
