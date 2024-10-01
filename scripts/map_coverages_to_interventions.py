# scripts/map_coverages_to_interventions.py

import os
import csv
import json
from collections import defaultdict

def load_starting_coverages(starting_coverages_path):
    """
    Load starting_coverages.csv and create a dictionary mapping ISO codes to intervention coverages,
    considering the 'level' for risk factors.
    """
    # Updated coverage_data to handle levels: {ISO: {intervention: {level: value}}}
    coverage_data = defaultdict(lambda: defaultdict(dict))
    with open(starting_coverages_path, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            iso = row['ISO']
            intervention = row['intervention']
            level = row.get('level') or ''
            level = str(level)  # Ensure level is a string for consistent keys
            try:
                value = float(row['value'])
            except ValueError:
                value = None
            coverage_data[iso][intervention][level] = value
    return coverage_data

def extract_interventions_from_template(template_path):
    """
    Extract the list of interventions from a template JSON file, including levels for risk factors.
    """
    with open(template_path, 'r', encoding='utf-8-sig') as f:
        template = json.load(f)
    
    # Use a set of tuples to store (intervention, level)
    interventions = set()

    # Extract from treatment associations
    for assoc in template.get('treatment associations', []):
        intervention = assoc.get('treatment')
        if intervention:
            # Treatments usually don't have levels
            interventions.add((intervention, ''))

    # Extract from prevention associations
    for assoc in template.get('prevention associations', []):
        intervention = assoc.get('prevention')
        if intervention:
            # Preventions usually don't have levels
            interventions.add((intervention, ''))

    # Extract from risk factors
    for risk_factor in template.get('risk factors', []):
        # Assume the intervention name is stored under 'intervention' or 'name'
        intervention = risk_factor.get('risk factor') or risk_factor.get('name')
        level = risk_factor.get('level') or ''
        level = str(level)  # Ensure level is a string
        if intervention:
            interventions.add((intervention, level))

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
            for intervention, level in interventions:
                value = iso_coverage.get(intervention, {}).get(level)
                if value is not None:
                    values.append(value)
                else:
                    print(f"Warning: No starting coverage for intervention '{intervention}' (level '{level}') in ISO '{iso}'")

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
