import os

RESEARCH_DATA = {
    "01_The_Journey/02_Orienting_and_Positioning": {
        "md": """
## 🔬 Scientific Validation & Research Context
*   **The Cognitive Map:** The human requirement to anchor onto physical landmarks ("Sentinels") is deeply rooted in our neurobiology. In 2014, John O'Keefe and May-Britt and Edvard Moser won the Nobel Prize in Physiology for discovering the brain's "inner GPS." 
*   **Grid and Place Cells:** Their research showed that specific neurons in the hippocampus ("Place Cells") fire when we are in a known location, while "Grid Cells" in the entorhinal cortex provide a metric coordinate system. When a traveler lacks distinct physical landmarks, this internal grid system fails to calibrate, leading directly to the physiological stress response commonly known as "panic" or "lizard-brain."
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>The human requirement to anchor onto physical landmarks is a neurobiological imperative:</p>
            <ul>
                <li><strong>The Cognitive Map:</strong> In 2014, John O'Keefe and the Mosers won the Nobel Prize for discovering the brain's "inner GPS." They identified specific neurons in the hippocampus ("Place Cells") that map environments, and "Grid Cells" in the entorhinal cortex that calculate distance and spatial metrics.</li>
                <li><strong>Spatial Panic:</strong> When a traveler lacks distinct external landmarks ("Sentinels"), this internal neural grid fails to calibrate. The resulting cognitive dissonance triggers an immediate cortisol spike and physiological stress response, bypassing rational thought.</li>
            </ul>
        </div>
"""
    },
    "05_The_Mind/03_Restorative_Architecture": {
        "md": """
## 🔬 Scientific Validation & Research Context
*   **Biophilic Design & Neuroarchitecture:** Christopher Alexander’s architectural theories from *A Pattern Language* (1977) have been empirically validated by modern neuroscience. Environments built with "living structures" (such as natural light on two sides of a room, or fractal geometries in stonework) actively lower cortisol levels and engage the parasympathetic nervous system.
*   **Fractal Fluency:** The human visual cortex evolved in nature and is highly tuned to process fractal geometries (like the branching of trees or the grain of wood) with minimal cognitive effort. Stark, featureless concrete walls require more visual processing power, generating subconscious, low-grade stress.
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>The restorative properties of architecture are proven by empirical neuroscience:</p>
            <ul>
                <li><strong>Neuroarchitecture:</strong> Christopher Alexander’s theories of "living structure" have been validated by biometric studies (EEG and skin conductance). Rooms with natural light on two sides and transitional spaces actively lower cortisol levels and engage the parasympathetic (rest and digest) nervous system.</li>
                <li><strong>Fractal Fluency:</strong> The human visual cortex is evolved to process fractal geometries (like wood grain, leaves, or uneven stone) with near-zero cognitive effort. Stark, hyper-symmetrical industrial walls require continuous active visual processing, generating subconscious, chronic stress.</li>
            </ul>
        </div>
"""
    },
    "07_The_Mechanics/02_Mechanical_Power": {
        "md": """
## 🔬 Scientific Validation & Research Context
*   **The Laws of Thermodynamics:** The First Law of Thermodynamics states that energy cannot be created or destroyed, only transformed. A water wheel or line-shaft does not "make" power; it captures the kinetic energy of gravity acting on water mass.
*   **Mechanical Advantage & Friction:** The efficiency of any pre-electric system is entirely dictated by the reduction of friction. The use of hardwood bearings soaked in animal fat reduces the coefficient of sliding friction by up to 80% compared to dry wood-on-wood contact, allowing the captured kinetic energy to successfully translate into cutting or grinding torque instead of being lost as waste heat.
""",
        "html": """
        <div class="research-validation" style="margin: 2em 0; padding: 1.5em; background-color: #f0f7f4; border-left: 5px solid #2ecc71; border-radius: 4px;">
            <h3 style="color: #27ae60; margin-top: 0;">🔬 Scientific Validation & Research Context</h3>
            <p>Mechanical systems are strictly bound by physics:</p>
            <ul>
                <li><strong>Thermodynamics:</strong> Energy cannot be created. Gravity-fed mechanical systems (like water wheels) merely capture the kinetic energy of water mass falling through an elevation gradient. Efficiency is entirely dependent on limiting energy loss.</li>
                <li><strong>Coefficient of Friction:</strong> The greatest threat to mechanical power is parasitic drag (friction). Lubricating wooden or rudimentary steel bearings with rendered animal fats or pressed seed oils reduces the coefficient of friction by up to 80%, preventing the system from burning its own energy as waste heat.</li>
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
