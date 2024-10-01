# scripts/map_coverages_to_interventions.py

import os
import csv
import json
from collections import defaultdict

def load_starting_coverages(starting_coverages_path):
    """
    Load starting_coverages.csv and create a dictionary mapping ISO codes to intervention coverages.
    """
    coverage_data = defaultdict(dict)  # {ISO: {intervention: value}}
    with open(starting_coverages_path, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            iso = row['ISO']
            intervention = row['intervention']
            try:
                value = float(row['value'])
            except ValueError:
                value = None
            coverage_data[iso][intervention] = value
    return coverage_data

def extract_interventions_from_template(template_path):
    """
    Extract the list of interventions from a template JSON file.
    """
    with open(template_path, 'r', encoding='utf-8-sig') as f:
        template = json.load(f)
    
    interventions = set()

    # Extract from treatment associations
    for assoc in template.get('treatment associations', []):
        intervention = assoc.get('treatment')
        if intervention:
            interventions.add(intervention)

    # Extract from prevention associations
    for assoc in template.get('prevention associations', []):
        intervention = assoc.get('prevention')
        if intervention:
            interventions.add(intervention)

    # Extract from risk factors
    for risk_factor in template.get('risk factors', []):
        # Assuming the intervention name is stored under the 'name' or 'intervention' key
        intervention = risk_factor.get('intervention')
        if not intervention:
            intervention = risk_factor.get('name')
        if intervention:
            interventions.add(intervention)

    return interventions

def main():
    starting_coverages_path = 'data/starting_coverages.csv'
    templates_dir = './templates/'
    output_csv = 'coverage_means.csv'

    coverage_data = load_starting_coverages(starting_coverages_path)

    template_files = [f for f in os.listdir(templates_dir) if f.endswith('.json')]

    # Get list of ISO codes from starting_coverages.csv
    iso_codes = coverage_data.keys()

    all_results = []

    for iso in iso_codes:
        iso_coverage = coverage_data[iso]
        for template_file in template_files:
            template_path = os.path.join(templates_dir, template_file)
            interventions = extract_interventions_from_template(template_path)

            # Collect starting coverage values for the interventions
            values = []
            for intervention in interventions:
                value = iso_coverage.get(intervention)
                if value is not None:
                    values.append(value)
                else:
                    print(f"Warning: No starting coverage for intervention '{intervention}' in ISO '{iso}'")

            if values:
                mean_value = sum(values) / len(values)
            else:
                mean_value = None  # No data available for this ISO and template

            all_results.append({
                'ISO': iso,
                'FILENAME': os.path.splitext(template_file)[0],
                'MEAN_VALUE': mean_value
            })

    # Write to CSV
    header = ['ISO', 'FILENAME', 'MEAN_VALUE']
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)

if __name__ == '__main__':
    main()
