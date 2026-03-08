import os
import re

# Data structure mapping relative file paths (without extension) to the scientific validation block.
RESEARCH_DATA = {
    "04_The_Body/02_Biochemical_Signals": {
        "md": """
## 🔬 Scientific Validation & Research Context
The protocols outlined above are heavily validated by modern neurobiology and chronobiology:
*   **Glymphatic Clearance:** In 2013, Dr. Maiken Nedergaard and her team published *"Sleep Drives Metabolite Clearance from the Adult Brain"* in the journal **Science**. Their research empirically proved that during deep sleep, the brain's interstitial space expands by 60%, allowing cerebrospinal fluid to "flush" out toxic metabolic byproducts like amyloid-beta (associated with Alzheimer's) twice as fast as during wakefulness. 
*   **Circadian Entrainment:** Decades of chronobiology research confirm that the Suprachiasmatic Nucleus (SCN) requires high-lux, short-wavelength (blue) light in the morning to halt melatonin production and synchronize the body's peripheral clocks, preventing systemic entropy.
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>The protocols outlined above are heavily validated by modern neurobiology and chronobiology:</p>
            <ul>
                <li><strong>Glymphatic Clearance:</strong> In 2013, Dr. Maiken Nedergaard's lab published <em>"Sleep Drives Metabolite Clearance from the Adult Brain"</em> in <strong>Science</strong>. The study empirically proved that during deep sleep, the brain's interstitial space expands by 60%, allowing cerebrospinal fluid to "flush" out toxic metabolic byproducts (like amyloid-beta) twice as fast as when awake.</li>
                <li><strong>Circadian Entrainment:</strong> The Suprachiasmatic Nucleus (SCN) requires high-lux, short-wavelength light in the morning to halt melatonin and synchronize the body's clocks. Blocking blue light at night is critical to allow the melatonin ramp required to initiate the glymphatic wash.</li>
            </ul>
        </div>
"""
    },
    "06_The_Ecosystem/02_Soil_Sovereignty": {
        "md": """
## 🔬 Scientific Validation & Research Context
*   **Biochar and Nutrient Retention:** Dr. Johannes Lehmann's seminal research (published in **Nature**, 2007, *"A Handful of Carbon"*) validated that the ancient Amazonian *Terra Preta* soils remained fertile for thousands of years due to human-created "black carbon" (biochar). Biochar vastly increases the Cation Exchange Capacity (CEC) of soil, acting as a microscopic sponge that prevents vital nutrients (like nitrogen and phosphorus) from leaching away during heavy rains.
*   **Carbon Sequestration:** Burning biomass in a restricted-oxygen environment (pyrolysis) locks carbon into a stable lattice structure that microbes cannot easily break down, effectively sequestering carbon for millennia.
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>The methods above are validated by modern soil science and archaeological soil analysis:</p>
            <ul>
                <li><strong>Biochar (Terra Preta):</strong> Dr. Johannes Lehmann's seminal research (e.g., <em>"A Handful of Carbon"</em>, <strong>Nature</strong> 2007) validated that ancient Amazonian *Terra Preta* soils remained fertile for over 2,000 years due to human-made "black carbon". Biochar massively increases the Cation Exchange Capacity (CEC) of soil, preventing nutrient leaching in heavy rains.</li>
                <li><strong>Carbon Sequestration:</strong> Pyrolysis locks carbon into a stable lattice structure. Unlike raw compost, which decomposes and releases CO2 back into the atmosphere, biochar sequesters carbon for millennia while serving as a permanent reef for soil microbiology.</li>
            </ul>
        </div>
"""
    },
    "03_The_Arrival/02_Bio_Security_and_Water": {
        "md": """
## 🔬 Scientific Validation & Research Context
*   **Bio-Sand Filtration (SSF):** The Center for Affordable Water and Sanitation Technology (CAWST) and the World Health Organization (WHO) validate that Slow Sand Filters (SSF) can remove up to 99.9% of protozoa and 90-99% of bacteria. 
*   **The Schmutzdecke:** The effectiveness of the sand filter is not primarily mechanical, but biological. A biolayer (Schmutzdecke) forms on the top 2 centimeters of the sand. This layer consists of beneficial bacteria and algae that physically consume and trap harmful human pathogens before they pass deeper into the filter.
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>Field-expedient water systems rely on proven biological mechanisms:</p>
            <ul>
                <li><strong>Bio-Sand Efficacy:</strong> The Center for Affordable Water and Sanitation Technology (CAWST) and the WHO validate that Bio-Sand Filters remove up to 99.9% of protozoa and 90-99% of bacteria from raw water sources.</li>
                <li><strong>The Biological Layer:</strong> The filter works via the <em>Schmutzdecke</em> (German for "dirt layer"). A community of beneficial microorganisms forms in the top 2cm of the sand. These microbes prey on and consume human pathogens, making the filter a biological reactor, not just a mechanical sieve.</li>
            </ul>
        </div>
"""
    }
}

def update_md(filepath, md_block):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Scientific Validation" in content:
        return # Already injected
        
    # Inject before the Practical Implementation Guide if it exists
    if "## 🚀 Practical Implementation Guide" in content:
        content = content.replace("## 🚀 Practical Implementation Guide", md_block + "\n\n## 🚀 Practical Implementation Guide")
    else:
        content += "\n" + md_block
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated MD: {filepath}")

def update_html(filepath, html_block):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Scientific Validation" in content:
        return
        
    # Inject before the practical guide div
    if '<div class="practical-guide"' in content:
        content = content.replace('<div class="practical-guide"', html_block + '\n    <div class="practical-guide"')
    elif '</section>' in content:
        # Fallback to before the first section end
        content = content.replace('</section>', html_block + '\n    </section>', 1)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated HTML: {filepath}")

if __name__ == "__main__":
    for module_path, blocks in RESEARCH_DATA.items():
        md_file = module_path + ".md"
        html_file = "html/" + module_path + ".html"
        
        if os.path.exists(md_file):
            update_md(md_file, blocks['md'])
        if os.path.exists(html_file):
            update_html(html_file, blocks['html'])
