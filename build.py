import os
import yaml
import json
from jinja2 import Environment, FileSystemLoader

# Configuration
DATA_DIR = 'data'
TEMPLATE_DIR = 'templates'
OUTPUT_FILE = 'index.html'

def load_yaml_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def main():
    print("🚀 Starting Cobotics4All Build...")

    # 1. Load Content from YAML
    try:
        data = {
            'challenges': load_yaml_data('challenges.yaml'),
            'missions': load_yaml_data('missions.yaml'),
            'task_plots': load_yaml_data('task_plots.yaml'),
            'skills': load_yaml_data('skills.yaml')
        }
        print(f"✅ Loaded {len(data['challenges'])} challenges, {len(data['missions'])} missions, {len(data['task_plots'])} plots.")
    except FileNotFoundError as e:
        print(f"❌ Error: Could not find data file: {e}")
        return

    # 2. Set up Jinja2 Environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('index.html')

    # 3. Render HTML
    # We pass 'json' so we can dump data into JavaScript for the interactive parts
    output_html = template.render(
        **data, 
        json=json 
    )

    # 4. Save to index.html
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output_html)
    
    print(f"🎉 Build Complete! Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
