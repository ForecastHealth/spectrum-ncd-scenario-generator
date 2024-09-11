import os
import json
import csv
import argparse
from country_metadata import get_tag

COUNTRY_PROJECTIONS_DIR = "./examples"  # Where the country PJZN are

def get_iso3_codes():
    iso3_codes = {}
    with open('data/GBModData_CountryMaster_0.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            iso3_codes[row['Country']] = row['ISO']
    return iso3_codes

def get_base_coverage(income_status):
    coverage_map = {
        'Low income': 0.05,
        'Lower middle income': 0.075,
        'Upper middle income': 0.1,
        'High income': 0.15
    }
    return coverage_map.get(income_status, 0.05)  # Default to 0.05 if not found

def process_country(country, iso3_code, filename, template_config, scenario):
    income_status = get_tag(iso3_code, "wb_income")
    base_coverage = get_base_coverage(income_status)
    
    create_config(filename, iso3_code, country, template_config, base_coverage, scenario)

def create_config(filename, iso3_code, country, config, baseline_coverage, scenario):
    for association_type in [
        'treatment associations',
        'prevention associations',
        'risk factors',
    ]:
        for association in config[association_type]:
            association['baseline_coverage'] = baseline_coverage
    
    # Add metadata
    config['metadata'] = {
        "pjnz_filename": f"{COUNTRY_PROJECTIONS_DIR}/{filename}",
        "iso3": iso3_code,
        "country": country,
        "scenario": scenario,
        "scaleup_type": "scaleup"  # Keeping this for backward compatibility
    }
    
    # Add default_coverage key
    config['default_coverage'] = baseline_coverage
    
    output_dir = f'./config/{scenario}'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'{iso3_code}_{scenario}.json')
    
    with open(output_path, 'w') as f:
        json.dump(config, f, indent=2)

def extract_scenario_from_filename(filename):
    # Assuming the filename format is something like "template_configXXX.json"
    # where XXX is the scenario
    base_name = os.path.basename(filename)
    scenario = base_name.split('_')[-1].split('.')[0]
    return scenario

def main(template_config_path):
    with open(template_config_path, 'r') as f:
        template_config = json.load(f)
    scenario = extract_scenario_from_filename(template_config_path)
    
    iso3_codes = get_iso3_codes()
    
    for filename in os.listdir(COUNTRY_PROJECTIONS_DIR):
        if filename.endswith('.PJNZ'):
            country = filename[:-5]  # Remove .PJNZ extension
            if country in iso3_codes:
                process_country(country, iso3_codes[country], filename, template_config, scenario)
            else:
                print(f"Warning: ISO3 code not found for {country}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process country data with a given template configuration.")
    parser.add_argument("template_config", help="Path to the template configuration JSON file")
    args = parser.parse_args()
    
    main(args.template_config)
