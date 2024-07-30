import os
import json
import csv
from country_metadata import get_tag

TARGET_RATE = 95

def get_iso3_codes():
    iso3_codes = {}
    with open('data/GBModData_CountryMaster_0.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            iso3_codes[row['Country']] = row['ISO']
    return iso3_codes

def get_base_coverage(income_status):
    coverage_map = {
        'Low income': 5,
        'Lower middle income': 7.5,
        'Upper middle income': 10,
        'High income': 15
    }
    return coverage_map.get(income_status, 5)  # Default to 5 if not found

def process_country(country, iso3_code, filename):
    income_status = get_tag(iso3_code, "wb_income")
    base_coverage = get_base_coverage(income_status)
    if base_coverage is None:
        base_coverage = get_base_coverage("Low income")
    
    with open('config/template.json', 'r') as f:
        baseline_config = json.load(f)
    
    create_config(filename, iso3_code, country, baseline_config, base_coverage, base_coverage, "baseline")
    create_config(filename, iso3_code, country, baseline_config, base_coverage, TARGET_RATE, "scaleup")

def create_config(filename, iso3_code, country, config, baseline_coverage, target_coverage, config_type):
    for association_type in ['treatment associations', 'prevention associations']:
        for association in config[association_type]:
            association['baseline_coverage'] = baseline_coverage
            association['target_coverage'] = target_coverage
    
    # Add metadata
    config['metadata'] = {
        "pjnz_filename": filename,
        "iso3": iso3_code,
        "country": country,
        "scenario": config_type
    }
    
    output_path = f'./config/{config_type}/{country}_{config_type}.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(config, f, indent=2)

def main():
    iso3_codes = get_iso3_codes()
    
    for filename in os.listdir('examples'):
        if filename.endswith('.PJNZ'):
            country = filename[:-5]  # Remove .PJNZ extension
            if country in iso3_codes:
                process_country(country, iso3_codes[country], filename)
            else:
                print(f"Warning: ISO3 code not found for {country}")

if __name__ == "__main__":
    main()
