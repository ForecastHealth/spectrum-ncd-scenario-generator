import json
import os
from collections import defaultdict

def combine_json_configs(template_dir='./templates'):
    combined_config = defaultdict(list)

    # Iterate through all JSON files in the template directory
    for filename in os.listdir(template_dir):
        if filename == "all.json":
            continue
        if filename.endswith('.json'):
            file_path = os.path.join(template_dir, filename)
            
            with open(file_path, 'r') as f:
                config = json.load(f)
            
            # Combine the configurations
            for key, value in config.items():
                if isinstance(value, list):
                    combined_config[key].extend(value)
                elif isinstance(value, dict):
                    if key not in combined_config:
                        combined_config[key] = {}
                    combined_config[key].update(value)
                else:
                    combined_config[key] = value

    # Write the combined configuration to all.json
    with open('./templates/all.json', 'w') as f:
        json.dump(combined_config, f, indent=2)

    print(f"Combined configuration written to all.json")

if __name__ == "__main__":
    combine_json_configs()
