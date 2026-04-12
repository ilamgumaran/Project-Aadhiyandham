"""
Check that technical terms defined in module Vocabulary sections
are also defined in the central Glossary.md.

Scans all .md files in Outcome_* directories for terms in
"Vocabulary of the Foundation" sections and verifies each term
has a corresponding entry in Glossary.md.

Prints a report of missing terms. Does NOT fail the build (advisory only).
"""

import os
import re
import sys

GLOSSARY_PATH = "Glossary.md"

SOURCE_DIRS = [
    "Outcome_1_Locating_Refugia",
    "Outcome_2_Biological_Sovereignty",
    "Outcome_3_Perimeter_Defense",
    "Outcome_4_Psychological_Centeredness",
    "Outcome_5_Decadal_Resilience",
    "Outcome_6_Flourishing_Civilization",
]

# Matches bold terms in vocabulary sections: **Term Name:**
VOCAB_TERM_PATTERN = re.compile(r'\*\*([^*:]+?)(?:\s*\(.*?\))?\s*:\*\*')


def load_glossary_terms(glossary_path):
    """Extract all defined terms from Glossary.md."""
    terms = set()
    with open(glossary_path, "r", encoding="utf-8") as f:
        for line in f:
            match = VOCAB_TERM_PATTERN.search(line)
            if match:
                terms.add(match.group(1).strip().lower())
    return terms


def find_module_vocab_terms(source_dirs):
    """Find all terms defined in Vocabulary sections across all modules."""
    module_terms = {}  # term -> list of files defining it

    for source_dir in source_dirs:
        if not os.path.isdir(source_dir):
            continue
        for root, dirs, files in os.walk(source_dir):
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                filepath = os.path.join(root, fname)
                in_vocab_section = False

                with open(filepath, "r", encoding="utf-8") as f:
                    for line in f:
                        # Detect start of vocabulary section
                        if re.match(r'^#+\s*\d*\.?\s*Vocabulary', line):
                            in_vocab_section = True
                            continue
                        # Detect start of next section (any heading)
                        if in_vocab_section and re.match(r'^#+\s*\d*\.?\s*[A-Z]', line) and 'Vocabulary' not in line:
                            in_vocab_section = False
                            continue

                        if in_vocab_section:
                            match = VOCAB_TERM_PATTERN.search(line)
                            if match:
                                term = match.group(1).strip().lower()
                                if term not in module_terms:
                                    module_terms[term] = []
                                module_terms[term].append(filepath)

    return module_terms


def main():
    glossary_terms = load_glossary_terms(GLOSSARY_PATH)
    module_terms = find_module_vocab_terms(SOURCE_DIRS)

    missing = {}
    for term, files in sorted(module_terms.items()):
        if term not in glossary_terms:
            missing[term] = files

    print(f"Glossary contains {len(glossary_terms)} terms.")
    print(f"Modules define {len(module_terms)} unique vocabulary terms.")

    if missing:
        print(f"\n{len(missing)} term(s) used in modules but MISSING from Glossary.md:")
        for term, files in sorted(missing.items()):
            short_files = [os.path.basename(f) for f in files[:3]]
            suffix = f" (+{len(files)-3} more)" if len(files) > 3 else ""
            print(f"  - {term.title()}  (used in: {', '.join(short_files)}{suffix})")
        print(f"\nConsider adding these terms to {GLOSSARY_PATH}.")
    else:
        print("\nAll module vocabulary terms are covered in the Glossary.")


if __name__ == "__main__":
    main()
