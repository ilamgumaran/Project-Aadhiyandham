"""
generate_new_htmls.py — Convert ALL markdown modules to academic-styled HTML.

Scans Outcome_* directories for .md files and generates corresponding HTML
in the html/ directory with:
  - Semantic color-coded sections (Theory, Outcome, Materials, Assembly, etc.)
  - Proper table rendering
  - Code block rendering (for ASCII diagrams)
  - Auto-generated table of contents
  - Safety tier badges
  - Metadata extraction from frontmatter
  - Difficulty badges
"""

import os
import re
import html as html_module

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SOURCE_DIRS = [
    "Outcome_1_Locating_Refugia",
    "Outcome_2_Biological_Sovereignty",
    "Outcome_3_Perimeter_Defense",
    "Outcome_4_Psychological_Centeredness",
    "Outcome_5_Decadal_Resilience",
    "Outcome_6_Flourishing_Civilization",
]

ROOT_FILES = [
    "readme.md",
    "content_plan.md",
    "vision_and_outcomes.md",
    "DEPENDENCIES.md",
    "Glossary.md",
    "master_report.md",
    "settlers_summary.md",
]

# Map outcome directory names to outcome numbers
OUTCOME_MAP = {
    "Outcome_1": "1", "Outcome_2": "2", "Outcome_3": "3",
    "Outcome_4": "4", "Outcome_5": "5", "Outcome_6": "6",
}

# Section classification rules: (pattern_in_heading, css_class)
SECTION_CLASSIFIERS = [
    (r'Why This Is Important|Rationale|Why This Section Exists|Why This Matters', 'section-theory'),
    (r'Expected Outcome', 'section-outcome'),
    (r'Materials Needed|Materials \& Sourcing|Sourcing', 'section-materials'),
    (r'Assembly Instructions|Step.by.Step|Construction|Building|Implementation Steps', 'section-assembly'),
    (r'Visual Illustration|Conceptual|Diagram', 'section-diagram'),
    (r'Vocabulary|Glossary Reference', 'section-vocab'),
    (r'Scientific Validation|Research Context', 'section-research'),
    (r'Practical Implementation|Practical Guide|Implementation Guide|Beginner', 'section-practical'),
    (r'Troubleshooting|Failure Modes', 'section-practical'),
    (r'Community.*Flourishing|Apprenticeship|Decadal', 'section-practical'),
]

# Safety keywords that trigger inline warnings
SAFETY_DANGER_KEYWORDS = [
    r'lethal force', r'fatal if', r'fatally', r'extreme danger',
    r'can kill', r'life.threatening', r'poisonous', r'toxic if ingested',
    r'high.temperature.*burn', r'molten', r'1000.*°',
]
SAFETY_CAUTION_KEYWORDS = [
    r'wear protection', r'protective gear', r'ventilation required',
    r'risk of fire', r'risk of collapse', r'structural failure',
    r'sharp blade', r'heavy lifting', r'high temperature',
    r'do not attempt.*alone', r'cornered.*predator.*lethal',
]

# ---------------------------------------------------------------------------
# Frontmatter Parser
# ---------------------------------------------------------------------------
def parse_frontmatter(md_text):
    """Extract YAML-like frontmatter from HTML comment block."""
    meta = {}
    fm_match = re.search(r'<!--\s*\n(.*?)\n\s*-->', md_text, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('-') and not line.startswith('#'):
                key, _, val = line.partition(':')
                key = key.strip()
                val = val.strip()
                if val and key in ('section', 'outcome', 'difficulty', 'time_to_build', 'season', 'team_size', 'status'):
                    meta[key] = val
    return meta


# ---------------------------------------------------------------------------
# Classify an H2 heading into a semantic section type
# ---------------------------------------------------------------------------
def classify_section(heading_text):
    """Return CSS class for a given H2 heading text."""
    for pattern, css_class in SECTION_CLASSIFIERS:
        if re.search(pattern, heading_text, re.IGNORECASE):
            return css_class
    return None  # No special styling


# ---------------------------------------------------------------------------
# Markdown to HTML Converter
# ---------------------------------------------------------------------------
def md_to_html(md_text):
    """Convert markdown text to semantically structured HTML."""
    # Strip frontmatter comment block
    md_text = re.sub(r'<!--.*?-->', '', md_text, flags=re.DOTALL)

    lines = md_text.split('\n')
    html_lines = []
    toc_entries = []
    in_list = False
    in_ol = False
    in_code_block = False
    in_table = False
    current_section_class = None
    section_open = False
    figure_counter = [0]

    def close_list():
        nonlocal in_list, in_ol
        if in_list:
            html_lines.append('</ul>')
            in_list = False
        if in_ol:
            html_lines.append('</ol>')
            in_ol = False

    def close_section():
        nonlocal section_open
        if section_open:
            html_lines.append('</div>')
            section_open = False

    def close_table():
        nonlocal in_table
        if in_table:
            html_lines.append('</tbody></table>')
            in_table = False

    def format_inline(text):
        """Apply inline formatting: bold, italic, links, code."""
        # Code spans first (so they don't get caught by bold/italic)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links: [text](url) — convert .md references to .html
        def fix_link(m):
            label = m.group(1)
            url = m.group(2)
            # Convert internal .md links to .html
            if url.endswith('.md') and not url.startswith('http'):
                url = url[:-3] + '.html'
            elif '.md#' in url and not url.startswith('http'):
                url = url.replace('.md#', '.html#')
            return f'<a href="{url}">{label}</a>'
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', fix_link, text)
        # Bold
        text = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', text)
        return text

    skip_title = True  # Skip the first H1 (it becomes the page <h1>)

    for i, raw_line in enumerate(lines):
        line = raw_line.rstrip()

        # --- Code blocks ---
        if line.strip().startswith('```'):
            if in_code_block:
                html_lines.append('</code></pre>')
                in_code_block = False
            else:
                close_list()
                close_table()
                lang = line.strip()[3:].strip()
                html_lines.append(f'<pre><code class="language-{lang}">' if lang else '<pre><code>')
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(html_module.escape(line))
            continue

        # --- Table detection ---
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]

            # Check if this is a separator row (|---|---|)
            if all(re.match(r'^[-:]+$', c) for c in cells):
                continue  # Skip separator

            if not in_table:
                close_list()
                # This is the header row
                html_lines.append('<table><thead><tr>')
                for cell in cells:
                    html_lines.append(f'<th>{format_inline(cell)}</th>')
                html_lines.append('</tr></thead><tbody>')
                in_table = True
            else:
                html_lines.append('<tr>')
                for cell in cells:
                    html_lines.append(f'<td>{format_inline(cell)}</td>')
                html_lines.append('</tr>')
            continue
        else:
            close_table()

        stripped = line.strip()
        if not stripped:
            continue

        # --- H1 (page title — skip, handled by template) ---
        if stripped.startswith('# ') and not stripped.startswith('## '):
            if skip_title:
                skip_title = False
                continue
            close_list()
            close_section()
            html_lines.append(f'<h1>{format_inline(stripped[2:])}</h1>')
            continue

        # --- H2 (major sections) ---
        if stripped.startswith('## '):
            close_list()
            close_section()

            heading_text = stripped[3:]
            heading_id = re.sub(r'[^a-z0-9]+', '-', heading_text.lower()).strip('-')
            section_class = classify_section(heading_text)

            # TOC entry
            toc_entries.append((heading_text, heading_id, section_class))

            if section_class:
                html_lines.append(f'<div class="{section_class}" id="{heading_id}">')
                section_open = True
                html_lines.append(f'<h2>{format_inline(heading_text)}</h2>')
            else:
                html_lines.append(f'<h2 id="{heading_id}">{format_inline(heading_text)}</h2>')
            continue

        # --- H3, H4 ---
        if stripped.startswith('### '):
            close_list()
            heading_text = stripped[4:]
            heading_id = re.sub(r'[^a-z0-9]+', '-', heading_text.lower()).strip('-')
            html_lines.append(f'<h3 id="{heading_id}">{format_inline(heading_text)}</h3>')
            continue

        if stripped.startswith('#### '):
            close_list()
            heading_text = stripped[5:]
            html_lines.append(f'<h4>{format_inline(heading_text)}</h4>')
            continue

        # --- Horizontal rule ---
        if stripped == '---':
            close_list()
            html_lines.append('<hr>')
            continue

        # --- Ordered list (1. 2. 3. etc) ---
        ol_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if ol_match:
            if not in_ol:
                close_list()
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f'<li>{format_inline(ol_match.group(2))}</li>')
            continue

        # --- Unordered list ---
        if stripped.startswith('* ') or stripped.startswith('- '):
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = stripped[2:]
            html_lines.append(f'<li>{format_inline(content)}</li>')
            continue

        # --- Paragraph ---
        close_list()
        html_lines.append(f'<p>{format_inline(stripped)}</p>')

    # Close any open elements
    close_list()
    close_table()
    close_section()

    return '\n'.join(html_lines), toc_entries


# ---------------------------------------------------------------------------
# Generate Table of Contents HTML
# ---------------------------------------------------------------------------
def generate_toc(toc_entries):
    """Generate a table-of-contents HTML block from heading entries."""
    if len(toc_entries) < 3:
        return ''

    # Map section class to dot class
    dot_map = {
        'section-theory': 'dot-theory',
        'section-outcome': 'dot-outcome',
        'section-materials': 'dot-materials',
        'section-assembly': 'dot-assembly',
        'section-diagram': 'dot-diagram',
        'section-vocab': 'dot-vocab',
        'section-research': 'dot-research',
        'section-practical': 'dot-practical',
    }

    items = []
    for text, anchor, section_class in toc_entries:
        dot_class = dot_map.get(section_class, '')
        dot = f'<span class="{dot_class}">&#9679;</span> ' if dot_class else ''
        items.append(f'<li>{dot}<a href="#{anchor}">{html_module.escape(text)}</a></li>')

    return f'<div class="toc"><ol>{"".join(items)}</ol></div>'


# ---------------------------------------------------------------------------
# Generate Color Legend HTML
# ---------------------------------------------------------------------------
def generate_color_legend(toc_entries):
    """Generate a color legend showing which section types appear in this module."""
    seen = set()
    legend_items = []
    legend_map = {
        'section-theory': ('legend-theory', 'Theory'),
        'section-outcome': ('legend-outcome', 'Outcome'),
        'section-materials': ('legend-materials', 'Materials'),
        'section-assembly': ('legend-assembly', 'Instructions'),
        'section-research': ('legend-research', 'Research'),
        'section-practical': ('legend-practical', 'Practical Guide'),
    }
    for _, _, section_class in toc_entries:
        if section_class and section_class in legend_map and section_class not in seen:
            seen.add(section_class)
            css, label = legend_map[section_class]
            legend_items.append(f'<span class="{css}">{label}</span>')

    if not legend_items:
        return ''
    return f'<div class="color-legend">{"".join(legend_items)}</div>'


# ---------------------------------------------------------------------------
# Generate Metadata HTML
# ---------------------------------------------------------------------------
def generate_meta_html(meta):
    """Generate metadata display block from frontmatter."""
    if not meta:
        return ''

    labels = {
        'difficulty': 'Difficulty',
        'time_to_build': 'Time to Build',
        'season': 'Best Season',
        'team_size': 'Team Size',
        'status': 'Status',
    }

    items = []
    for key, label in labels.items():
        if key in meta:
            val = meta[key]
            if key == 'difficulty':
                badge_class = f'difficulty-{val}'
                items.append(f'<dt>{label}</dt><dd><span class="difficulty-badge {badge_class}">{val}</span></dd>')
            else:
                items.append(f'<dt>{label}</dt><dd>{html_module.escape(val)}</dd>')

    if not items:
        return ''
    return f'<dl class="module-meta">{"".join(items)}</dl>'


# ---------------------------------------------------------------------------
# Detect Safety Tier
# ---------------------------------------------------------------------------
def detect_safety_tier(md_text):
    """Scan content and return appropriate safety banner HTML."""
    text_lower = md_text.lower()

    for kw in SAFETY_DANGER_KEYWORDS:
        if re.search(kw, text_lower):
            return ('<div class="safety-banner danger">'
                    '<span class="safety-icon">&#9888;</span>'
                    '<div><strong>High Caution Module.</strong> This module involves processes that can cause serious injury if instructions are not followed precisely. '
                    'Build a small-scale prototype first. Never skip safety steps.</div></div>')

    for kw in SAFETY_CAUTION_KEYWORDS:
        if re.search(kw, text_lower):
            return ('<div class="safety-banner caution">'
                    '<span class="safety-icon">&#9888;</span>'
                    '<div><strong>Moderate Caution.</strong> Some steps require care. '
                    'Read the full module before starting. Follow the troubleshooting section if something goes wrong.</div></div>')

    return ('<div class="safety-banner safe">'
            '<span class="safety-icon">&#10003;</span>'
            '<div><strong>Safe to Explore.</strong> This module is safe for beginners. '
            'Experiment freely — mistakes here are low-cost learning opportunities.</div></div>')


# ---------------------------------------------------------------------------
# HTML Template
# ---------------------------------------------------------------------------
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Project Aadhiyandham</title>
    <link rel="stylesheet" href="{css_path}style.css">
</head>
<body class="{body_class}">

    <header>
        <h1>{title}</h1>
        <p class="alignment">{alignment}</p>
        {meta_html}
        {safety_html}
        {legend_html}
        {toc_html}
    </header>

    <section>
{content_html}
    </section>

    <footer>
        <p>Project Aadhiyandham (&#2950;&#2980;&#3007;&#2991;&#2984;&#3021;&#2980;&#2990;&#3021;) &mdash; Licensed under GNU GPLv3</p>
        <p style="font-size: 0.85em; margin-top: 4px;">The Architecture of the Null: A User Manual for Civilization</p>
    </footer>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Determine relative CSS path
# ---------------------------------------------------------------------------
def get_css_path(html_rel_path):
    """Calculate relative path from HTML file to html/ root."""
    depth = html_rel_path.count(os.sep)
    if depth == 0:
        return './'
    return '../' * depth


# ---------------------------------------------------------------------------
# Determine body class from path
# ---------------------------------------------------------------------------
def get_body_class(md_path):
    """Return outcome-N body class based on file path."""
    for prefix, num in OUTCOME_MAP.items():
        if prefix in md_path:
            return f'outcome-{num}'
    return 'global-theme'


# ---------------------------------------------------------------------------
# Extract title and alignment from markdown
# ---------------------------------------------------------------------------
def extract_title(md_text):
    """Extract H1 title from markdown."""
    match = re.match(r'^#\s+(.+)', md_text.strip())
    if match:
        return match.group(1).strip()
    return "Untitled Module"


def extract_alignment(md_text):
    """Extract alignment line from markdown."""
    match = re.search(r'\*\*Alignment:\*\*\s*(.+)', md_text)
    if match:
        return match.group(1).strip()
    return ""


# ---------------------------------------------------------------------------
# Main: Find and convert all markdown files
# ---------------------------------------------------------------------------
def find_all_md_files():
    """Find all markdown files in source directories."""
    files = []
    for source_dir in SOURCE_DIRS:
        if not os.path.isdir(source_dir):
            continue
        for root, dirs, filenames in os.walk(source_dir):
            for fname in sorted(filenames):
                if fname.endswith('.md'):
                    files.append(os.path.join(root, fname))
    return files


def generate_htmls():
    """Convert all markdown source files to HTML."""
    md_files = find_all_md_files()
    # Also process root files
    for rf in ROOT_FILES:
        if os.path.isfile(rf):
            md_files.append(rf)

    generated = 0
    for md_path in md_files:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # Determine output path
        html_rel = md_path.replace('.md', '.html')
        html_path = os.path.join('html', html_rel)
        os.makedirs(os.path.dirname(html_path), exist_ok=True)

        # Extract metadata
        meta = parse_frontmatter(md_text)
        title = extract_title(md_text)
        alignment = extract_alignment(md_text)
        body_class = get_body_class(md_path)
        css_path = get_css_path(html_rel)

        # Convert content
        content_html, toc_entries = md_to_html(md_text)

        # Generate supplementary blocks
        toc_html = generate_toc(toc_entries)
        legend_html = generate_color_legend(toc_entries)
        meta_html = generate_meta_html(meta)
        safety_html = detect_safety_tier(md_text)

        # Assemble final HTML
        final_html = HTML_TEMPLATE.format(
            title=html_module.escape(title),
            alignment=html_module.escape(alignment),
            body_class=body_class,
            css_path=css_path,
            content_html=content_html,
            toc_html=toc_html,
            legend_html=legend_html,
            meta_html=meta_html,
            safety_html=safety_html,
        )

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)

        generated += 1

    print(f"Generated {generated} HTML files from markdown sources.")


if __name__ == "__main__":
    generate_htmls()
