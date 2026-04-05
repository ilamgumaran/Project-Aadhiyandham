"""
renumber_headers.py
Enforces strict sequential numbering on markdown headers (## 1. ... ## 2. etc.)
within each module file. Fixes issues like duplicate numbers (e.g., '7. 7.Practical')
and gaps in the sequence.
"""
import os
import re
import glob


# Match ## headers with optional numbering: "## 1. Title" or "## 7. 7.Title" or "## Title"
H2_PATTERN = re.compile(r'^(##\s+)(\d+\.?\s*\d*\.?\s*)(.*)', re.MULTILINE)
H3_PATTERN = re.compile(r'^(###\s+)(\d+\.\d+\.?\s*)(.*)', re.MULTILINE)


def renumber_h2(text):
    """Renumber all ## headers sequentially starting from 1."""
    counter = [0]
    h3_counters = {}

    def replace_h2(m):
        counter[0] += 1
        prefix = m.group(1)  # "## "
        title = m.group(3).strip()
        # Clean any residual double numbering from the title
        title = re.sub(r'^\d+\.?\s*', '', title).strip()
        return f"{prefix}{counter[0]}. {title}"

    text = H2_PATTERN.sub(replace_h2, text)
    return text, counter[0]


def renumber_h3(text, h2_count):
    """Renumber all ### headers as N.M format under their parent ## N."""
    current_h2 = [0]
    h3_counter = [0]

    lines = text.split('\n')
    result = []

    for line in lines:
        h2_match = re.match(r'^##\s+(\d+)\.\s', line)
        if h2_match:
            current_h2[0] = int(h2_match.group(1))
            h3_counter[0] = 0
            result.append(line)
            continue

        h3_match = re.match(r'^(###\s+)(\d+\.\d+\.?\s*)(.*)', line)
        if h3_match and current_h2[0] > 0:
            h3_counter[0] += 1
            prefix = h3_match.group(1)
            title = h3_match.group(3).strip()
            title = re.sub(r'^\d+\.?\s*', '', title).strip()
            result.append(f"{prefix}{current_h2[0]}.{h3_counter[0]}. {title}")
            continue

        result.append(line)

    return '\n'.join(result)


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    # Only process files that have numbered ## headers
    if not H2_PATTERN.search(original):
        return False

    text, h2_count = renumber_h2(original)
    text = renumber_h3(text, h2_count)

    if text == original:
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    return True


def main():
    md_files = glob.glob('**/*.md', recursive=True)
    changed = 0
    for fp in md_files:
        if 'html/' in fp or '.git/' in fp or 'node_modules/' in fp:
            continue
        # Skip root-level summary docs
        if fp in ('content_plan.md', 'readme.md', 'master_report.md',
                   'settlers_summary.md', 'vision_and_outcomes.md',
                   'Glossary.md'):
            continue
        if process_file(fp):
            changed += 1
            print(f"  Renumbered headers in: {fp}")

    print(f"Header renumbering complete. {changed} file(s) updated.")


if __name__ == '__main__':
    main()
