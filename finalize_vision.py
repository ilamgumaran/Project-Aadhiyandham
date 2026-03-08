import os

def update_vision_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for the markdown and html files
    replacements = [
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Micro-Climate Forecasting`", "Advanced Micro-Climate Forecasting"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Advanced Micro-Climate Forecasting</code>", "Advanced Micro-Climate Forecasting"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Generational Sanitation & Humanure`", "Generational Sanitation & Humanure"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Generational Sanitation & Humanure</code>", "Generational Sanitation & Humanure"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Zero-Tech Dentistry & Oral Hygiene`", "Zero-Tech Dentistry & Oral Hygiene"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Zero-Tech Dentistry & Oral Hygiene</code>", "Zero-Tech Dentistry & Oral Hygiene"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Wildfire Defensible Space`", "Wildfire Defensible Space"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Wildfire Defensible Space</code>", "Wildfire Defensible Space"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Foundational Chemistry`", "Foundational Chemistry"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Foundational Chemistry</code>", "Foundational Chemistry"),
        ("`[READY FOR REVIEW] [TO BE DEVELOPED] Information Storage`", "Information Storage"),
        ("<code style=\"color:#d32f2f;\">[READY FOR REVIEW] [TO BE DEVELOPED] Information Storage</code>", "Information Storage"),
        ("*Missing/Optimal Placeholder:*", "*Solution Framework:*"),
        ("<em>Missing/Optimal Placeholder:</em>", "<em>Solution Framework:</em>")
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_vision_file('vision_and_outcomes.md')
update_vision_file('html/vision_and_outcomes.html')
