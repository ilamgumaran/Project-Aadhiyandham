"""
Validate internal cross-references between Markdown source files.

Scans all .md files in Outcome_* directories for relative markdown links
(e.g., [text](../../path/to/file.md)) and verifies the target file exists.
Exits with code 1 if broken links are found.
"""

import os
import re
import sys

# Directories containing markdown source modules
SOURCE_DIRS = [
    "Outcome_1_Locating_Refugia",
    "Outcome_2_Biological_Sovereignty",
    "Outcome_3_Perimeter_Defense",
    "Outcome_4_Psychological_Centeredness",
    "Outcome_5_Decadal_Resilience",
    "Outcome_6_Flourishing_Civilization",
]

# Also check root-level docs that may link into Outcomes
ROOT_FILES = [
    "readme.md",
    "content_plan.md",
    "vision_and_outcomes.md",
    "DEPENDENCIES.md",
    "Glossary.md",
    "master_report.md",
    "settlers_summary.md",
]

# Regex to match markdown links: [text](path)
# Captures the path portion, excluding anchors (#fragment)
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)#\s]+\.md(?:#[^)]*)?)\)')


def find_md_files(source_dirs):
    """Find all markdown files in source directories."""
    md_files = []
    for source_dir in source_dirs:
        if not os.path.isdir(source_dir):
            continue
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                if f.endswith(".md"):
                    md_files.append(os.path.join(root, f))
    return md_files


def check_markdown_links():
    """Scan all markdown files for broken internal links."""
    broken = []

    # Collect all files to scan
    all_files = []
    all_files.extend(find_md_files(SOURCE_DIRS))
    for rf in ROOT_FILES:
        if os.path.isfile(rf):
            all_files.append(rf)

    for filepath in all_files:
        file_dir = os.path.dirname(filepath)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for match in LINK_PATTERN.finditer(content):
            link_text = match.group(1)
            link_path = match.group(2)

            # Strip fragment anchors
            link_path = link_path.split("#")[0]

            # Skip external or absolute URLs
            if link_path.startswith("http") or link_path.startswith("/"):
                continue

            # Resolve relative to the file's directory
            target = os.path.normpath(os.path.join(file_dir, link_path))

            if not os.path.exists(target):
                broken.append(f"  {filepath}: [{link_text}]({link_path}) -> {target}")

    if broken:
        print(f"Found {len(broken)} broken markdown link(s):")
        for b in broken:
            print(b)
        sys.exit(1)
    else:
        print(f"All markdown links validated across {len(all_files)} files.")


if __name__ == "__main__":
    check_markdown_links()
