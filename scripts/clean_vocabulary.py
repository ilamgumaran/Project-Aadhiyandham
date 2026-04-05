"""
clean_vocabulary.py
Scans all markdown modules for '## Vocabulary of the Foundation' sections,
deduplicates terms, sorts them alphabetically, and rewrites the section in place.
"""
import os
import re
import glob


VOCAB_HEADER = re.compile(
    r'^##\s*\d*\.?\s*Vocabulary of the Foundation',
    re.MULTILINE,
)


def extract_vocab_block(text):
    """Return (start, end, terms_list) for the vocabulary section, or None."""
    m = VOCAB_HEADER.search(text)
    if not m:
        return None

    start = m.start()
    # Find the next heading (## or ---) or end-of-file
    rest = text[m.end():]
    next_section = re.search(r'^(?=##\s|---)', rest, re.MULTILINE)
    end = m.end() + next_section.start() if next_section else len(text)

    block = text[m.end():end]
    terms = []
    for line in block.strip().splitlines():
        line = line.strip()
        if line.startswith('*') or line.startswith('-'):
            terms.append(line)
    return start, end, terms


def clean_terms(terms):
    """Deduplicate and sort vocabulary bullet points alphabetically."""
    seen = set()
    unique = []
    for t in terms:
        # Normalize for dedup: strip leading bullet and whitespace
        key = re.sub(r'^[\*\-]\s*\**', '', t).strip().lower()
        if key and key not in seen:
            seen.add(key)
            unique.append(t)

    def sort_key(t):
        clean = re.sub(r'^[\*\-]\s*\**', '', t).strip()
        return clean.lower()

    unique.sort(key=sort_key)
    return unique


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    result = extract_vocab_block(text)
    if not result:
        return False

    start, end, terms = result
    if not terms:
        return False

    cleaned = clean_terms(terms)
    if cleaned == terms:
        return False

    header_match = VOCAB_HEADER.search(text)
    header_line = header_match.group(0)
    new_block = header_line + '\n\n' + '\n'.join(cleaned) + '\n\n'
    new_text = text[:start] + new_block + text[end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    return True


def main():
    md_files = glob.glob('**/*.md', recursive=True)
    changed = 0
    for fp in md_files:
        if 'html/' in fp or '.git/' in fp or 'node_modules/' in fp:
            continue
        if process_file(fp):
            changed += 1
            print(f"  Cleaned vocabulary in: {fp}")

    print(f"Vocabulary cleanup complete. {changed} file(s) updated.")


if __name__ == '__main__':
    main()
