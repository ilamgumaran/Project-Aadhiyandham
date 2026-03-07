import os
import glob

def convert_md_to_html(md_path, html_path, prev_link, next_link, atlas_index="index.html", main_index="../index.html"):
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

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title if title else "Candidate Location"} - Project Aadhiyandham</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <p><a href="{main_index}">Main Index</a> | <a href="{atlas_index}">Atlas Index</a></p>
    </header>

    <section>
        {content_html}
    </section>

    <div class="nav">
        <span>{f'Previous: <a href="{prev_link}">Previous Location</a>' if prev_link else ""}</span>
        <span><a href="{atlas_index}">Back to Atlas Index</a></span>
        <span>{f'Next: <a href="{next_link}">Next Location</a>' if next_link else ""}</span>
    </div>

    <footer>
        <p>Licensed under GNU GPLv3 | Project Aadhiyandham</p>
    </footer>
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

def main():
    source_dir = "candidate_locations"
    dest_dir = "html/candidate_locations"
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    md_files = sorted([f for f in os.listdir(source_dir) if f.endswith(".md")])
    
    for i, filename in enumerate(md_files):
        md_path = os.path.join(source_dir, filename)
        html_filename = filename.replace(".md", ".html")
        html_path = os.path.join(dest_dir, html_filename)
        
        prev_link = md_files[i-1].replace(".md", ".html") if i > 0 else None
        next_link = md_files[i+1].replace(".md", ".html") if i < len(md_files) - 1 else None
        
        print(f"Converting {filename}...")
        convert_md_to_html(md_path, html_path, prev_link, next_link)

if __name__ == "__main__":
    main()
