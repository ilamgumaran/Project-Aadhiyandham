"""
add_glossaries.py
Ensures every module markdown file contains a glossary back-reference
linking to the master Glossary.md for any defined terms it mentions.
Adds a '## Glossary Reference' section at the bottom if missing.
"""
import os
import re
import glob


def load_glossary_terms(glossary_path='Glossary.md'):
    """Extract all bold terms from the master Glossary."""
    terms = []
    if not os.path.exists(glossary_path):
        print(f"Warning: {glossary_path} not found.")
        return terms
    with open(glossary_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match lines like: *   **Term:** Definition
            m = re.match(r'^\*\s+\*\*(.+?)\*\*', line.strip())
            if m:
                terms.append(m.group(1).rstrip(':'))
    return terms


GLOSSARY_HEADER = re.compile(
    r'^##\s*\d*\.?\s*Glossary Reference',
    re.MULTILINE,
)


def file_mentions_terms(text, terms):
    """Return list of glossary terms mentioned in the file body."""
    mentioned = []
    for term in terms:
        # Escape for regex, case-insensitive word-boundary match
        pattern = re.escape(term)
        if re.search(pattern, text, re.IGNORECASE):
            mentioned.append(term)
    return sorted(mentioned)


def process_file(filepath, terms):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Skip if already has a glossary reference section
    if GLOSSARY_HEADER.search(text):
        return False

    mentioned = file_mentions_terms(text, terms)
    if not mentioned:
        return False

    # Calculate relative path to Glossary.md from this file
    depth = filepath.count(os.sep)
    rel_path = '../' * depth + 'Glossary.md'

    section = f"\n\n## Glossary Reference\n\n"
    section += f"*See [{rel_path}]({rel_path}) for full definitions of:*\n\n"
    for term in mentioned:
        section += f"*   **{term}**\n"
    section += "\n"

    # Insert before the Practical Implementation Guide if present,
    # otherwise append to end
    impl_match = re.search(
        r'^##\s*\d*\.?\s*\d*\.?\s*Practical Implementation Guide',
        text,
        re.MULTILINE,
    )
    if impl_match:
        new_text = text[:impl_match.start()] + section + text[impl_match.start():]
    else:
        new_text = text.rstrip() + section

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    return True


def main():
    terms = load_glossary_terms()
    if not terms:
        print("No glossary terms loaded. Skipping.")
        return

    md_files = glob.glob('**/*.md', recursive=True)
    changed = 0
    for fp in md_files:
        if 'html/' in fp or '.git/' in fp or 'node_modules/' in fp:
            continue
        # Skip root-level docs and the glossary itself
        if fp in ('Glossary.md', 'content_plan.md', 'readme.md',
                   'master_report.md', 'settlers_summary.md',
                   'vision_and_outcomes.md'):
            continue
        if process_file(fp, terms):
            changed += 1
            print(f"  Added glossary reference to: {fp}")

    print(f"Glossary injection complete. {changed} file(s) updated.")


if __name__ == '__main__':
    main()
