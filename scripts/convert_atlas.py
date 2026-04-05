import os
import glob
import re

def convert_md_to_html(md_path, html_path, title_cache, main_index="../../index.html", atlas_index="../index.html"):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    title = ""
    content_html = ""
    for line in lines:
        line = line.strip()
        if not line:
            content_html += "<br>\n"
            continue
        if line.startswith("# "):
            title = line[2:]
            content_html += f"<h1>{title}</h1>\n"
        elif line.startswith("## "):
            content_html += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("### "):
            content_html += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("* "):
            content_html += f"<li>{line[2:]}</li>\n"
        elif line.startswith("[x]") or line.startswith("[ ]"):
            content_html += f"<p>{line}</p>\n"
        else:
            content_html += f"<p>{line}</p>\n"

    # Default if no title found
    if not title:
        title = os.path.basename(md_path).replace('.md', '').replace('_', ' ').title()

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title} - Project Aadhiyandham</title>
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
    <header>
        <p><a href="{main_index}">Main Index</a> | <a href="{atlas_index}">Atlas Index</a></p>
    </header>

    <section>
        {content_html}
    </section>

    <div class="nav">
        <span><a href="{atlas_index}">Back to Atlas Index</a></span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
        
    return title

def build_atlas_index(grouped_locations):
    index_path = "html/Outcome_1_Locating_Refugia/03_Candidate_Atlas/index.html"
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Global Atlas of Resilient Locations - Project Aadhiyandham</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <p><a href="../index.html">Main Index</a></p>
        <h1>Global Atlas of Resilient Locations</h1>
        <p>A categorized evaluation of 70 geographical sites selected for long-term climatic, geological, and hydrological stability.</p>
    </header>

    <section>
"""

    for continent in sorted(grouped_locations.keys()):
        html_content += f"        <h2>{continent.replace('_', ' ')}</h2>\n        <ul>\n"
        for loc in sorted(grouped_locations[continent], key=lambda x: x['title']):
            html_content += f"            <li><a href='{continent}/{loc['filename']}'>{loc['title']}</a></li>\n"
        html_content += "        </ul>\n\n"

    html_content += """    </section>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    source_dir = "Outcome_1_Locating_Refugia/03_Candidate_Atlas"
    dest_dir = "html/Outcome_1_Locating_Refugia/03_Candidate_Atlas"
    
    continents = ["Africa", "Asia", "Europe", "North_America", "Oceania", "South_America"]
    
    grouped_locations = {c: [] for c in continents}
    
    for continent in continents:
        cont_source = os.path.join(source_dir, continent)
        cont_dest = os.path.join(dest_dir, continent)
        
        if not os.path.exists(cont_dest):
            os.makedirs(cont_dest)
            
        md_files = glob.glob(os.path.join(cont_source, "*.md"))
        
        for md_path in md_files:
            filename = os.path.basename(md_path)
            html_filename = filename.replace(".md", ".html")
            html_path = os.path.join(cont_dest, html_filename)
            
            title = convert_md_to_html(md_path, html_path, {})
            grouped_locations[continent].append({
                "filename": html_filename,
                "title": title
            })
            print(f"Converted {continent}/{filename}")

    # Build the master index
    build_atlas_index(grouped_locations)
    print("Generated 03_Candidate_Atlas/index.html")

if __name__ == "__main__":
    main()
