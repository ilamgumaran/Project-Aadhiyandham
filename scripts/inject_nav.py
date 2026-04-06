import os
import re

NAV_HTML = """
    <!-- Global Navigation Bar -->
    <nav class="global-nav">
        <ul>
            <li><a href="{root_path}index.html">🏠 Home</a></li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 1 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_1_Locating_Refugia/01_The_Journey/01_Rationale_and_Importance.html">01. The Journey</a>
                    <a href="{root_path}Outcome_1_Locating_Refugia/02_The_Site/01_Rationale_and_Importance.html">02. The Site</a>
                    <a href="{root_path}Outcome_1_Locating_Refugia/03_Candidate_Atlas/index.html">🌍 The Atlas</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 2 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/03_Water_and_Sanitation/01_Rationale_and_Importance.html">03. Water &amp; Sanitation</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/04_Food_and_Soil_Sovereignty/01_Rationale_and_Importance.html">04. Food &amp; Soil</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/05_Health_and_the_Body/01_Rationale_and_Importance.html">05. Health &amp; Body</a>
                    <a href="{root_path}Outcome_2_Biological_Sovereignty/06_Ecological_Harmony/01_Rationale_and_Importance.html">06. Ecological Harmony</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 3 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_3_Perimeter_Defense/07_Passive_Defense/02_Passive_Perimeter_Defense.html">07. Passive Defense</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 4 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_4_Psychological_Centeredness/08_The_Mind/01_Rationale_and_Importance.html">08. The Mind</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 5 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_5_Decadal_Resilience/09_The_Mechanics/01_Rationale_and_Importance.html">09. The Mechanics</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/10_The_Society/01_Rationale_and_Importance.html">10. The Society</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/11_The_Next_Generation/01_Rationale_and_Importance.html">11. Education</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/12_The_Archive/01_Rationale_and_Importance.html">12. The Archive</a>
                    <a href="{root_path}Outcome_5_Decadal_Resilience/13_The_Horizon/01_Rationale_and_Importance.html">13. The Horizon</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="javascript:void(0)" class="dropbtn">Outcome 6 ▾</a>
                <div class="dropdown-content">
                    <a href="{root_path}Outcome_6_Flourishing_Civilization/14_Cultural_Technology/01_Rationale_and_Importance.html">14. Cultural Tech</a>
                </div>
            </li>
            <li><a href="{root_path}glossary.html">📖 Glossary</a></li>
        </ul>
    </nav>
"""

CSS_UPDATE = """
/* Global Sticky Navigation Bar */
.global-nav {
    background-color: #2c3e50;
    position: sticky;
    top: 0;
    z-index: 1000;
    border-radius: 4px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.global-nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    display: flex;
    flex-wrap: wrap;
}
.global-nav li {
    float: left;
}
.global-nav li a, .global-nav .dropbtn {
    display: inline-block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-weight: bold;
}
.global-nav li a:hover, .dropdown:hover .dropbtn {
    background-color: #27ae60;
}
.global-nav li.dropdown {
    display: inline-block;
}
.global-nav .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 4px;
}
.global-nav .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
.global-nav .dropdown-content a:hover {
    background-color: #f1f1f1;
    color: #27ae60;
}
.global-nav .dropdown:hover .dropdown-content {
    display: block;
}
"""

def update_css():
    css_path = 'html/style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.global-nav' not in content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(CSS_UPDATE)
        print("Updated style.css with global nav styles.")

def update_html():
    for root, dirs, files in os.walk('html'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                # Determine depth to calculate root_path
                depth = root.replace('html', '').count(os.sep)
                root_path = '../' * depth if depth > 0 else './'
                if root == 'html':
                    root_path = './'
                
                nav_block = NAV_HTML.format(root_path=root_path)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Overwrite old nav bar if it exists
                if '<!-- Global Navigation Bar -->' in content:
                    content = re.sub(r'<!-- Global Navigation Bar -->.*?</nav>', nav_block.strip(), content, flags=re.DOTALL)
                else:
                    content = content.replace('<body>', '<body>\n' + nav_block)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    update_css()
    update_html()
    print("Global navigation injection complete.")
