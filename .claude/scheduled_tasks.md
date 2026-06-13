# Scheduled Tasks for Project Aadhiyandham

## Task: Enhance All Topic Modules (every 2 hours)

**Cron**: `17 */2 * * *` (every 2 hours at :17)
**Type**: Recurring, durable
**Auto-expires**: 7 days from creation

To re-create this task in a new Claude Code session, say:
> "Resume the scheduled enhancement task from PROGRESS_TRACKER.md"

### Prompt

```
You are working on Project Aadhiyandham, an open-source blueprint for decentralized civilization. You have a recurring task to systematically enhance every topic module.

## Your workflow each session

### Step 1: Read the progress tracker
Read `PROGRESS_TRACKER.md` in the project root. Find the NEXT module(s) marked `[ ]` (pending). Work on 2-3 modules per session, starting from the top.

### Step 2: Enhance theory and details (Phase 1)
For each pending module, read the current markdown file and enhance it with:

1. **Deeper theory**: Add foundational "why" — the physics, biology, chemistry, or social science behind the topic. Cite principles by name (e.g., Darcy's Law for water flow, Dunbar's Number for group size). Explain first principles so a motivated learner can understand the mechanism, not just the recipe.

2. **Structured sections** (use these H2 headings consistently):
   - `## Theoretical Foundation` — the science/history behind this topic
   - `## Core Principles` — numbered list of key principles the reader must understand
   - `## Practical Implementation` — step-by-step how-to with materials, dimensions, quantities
   - `## Common Failure Modes` — what goes wrong and why, with prevention strategies
   - `## Vocabulary of the Foundation` — key terms with definitions
   - `## Cross-References` — links to related modules in other outcomes
   - `## Further Study` — named books, papers, or historical examples (no URLs)

3. **Safety annotations**: Where relevant, add clear safety warnings using the format:
   - `> **SAFE**: ...` for low-risk activities
   - `> **CAUTION**: ...` for moderate-risk activities
   - `> **DANGER**: ...` for high-risk activities (fire, structural, medical)

4. **Quantitative depth**: Add specific numbers — temperatures, ratios, distances, time durations, load capacities. Replace vague language ("heat it until hot") with precise specifications ("maintain 55-65C for 72 hours").

5. **Historical grounding**: Where applicable, reference historical or indigenous examples that prove the technique works at scale (e.g., Roman concrete, Japanese charcoal kilns, Incan terrace farming).

### Step 3: Update progress tracker
After enhancing each module, update `PROGRESS_TRACKER.md`:
- Change `[ ]` to `[T]` for each theory-enhanced module
- Add a row to the Session Log table with the date, modules enhanced, and brief notes

### Step 4: Check if Phase 1 is complete
If ALL modules show `[T]` or higher, switch to Phase 2:
- Go back through modules marked `[T]` and add ASCII-art diagrams, tables, or SVG illustrations
- Describe diagrams in markdown (ASCII cross-sections, flow diagrams, dimension tables)
- Update status from `[T]` to `[I]` after adding illustrations
- When a module has both theory and illustrations, mark it `[x]`

### Step 5: Regenerate HTML and commit
After enhancing modules:
1. Run `python3 scripts/generate_new_htmls.py` to rebuild HTML
2. Run `python3 scripts/check_markdown_links.py` to verify no broken links
3. Commit changes with message: `feat: enhance [Section Name] — [module names]`
4. Push to main

### Important guidelines
- Maintain the existing markdown formatting conventions (H1 for title, H2 for sections)
- Keep the academic tone — this is a field manual, not a blog post
- Every claim should be backed by a mechanism or principle, not just assertion
- Preserve existing content that is already strong — enhance, don't replace
- Each module should be 2000-5000 words when fully enhanced (theory + practical)
- Do NOT modify the Candidate Atlas files (03_Candidate_Atlas/) — those are location profiles, not topic modules
- Work through outcomes in order: Outcome 1 first, then 2, 3, 4, 5, 6
```
