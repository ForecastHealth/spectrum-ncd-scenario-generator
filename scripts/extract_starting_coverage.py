# scripts/extract_starting_coverage.py
import csv
import os
import zipfile

def load_constants(constants_path):
    """
    Load constants.csv and create reverse lookup dictionaries.
    """
    constants_reverse_lookup = {
        'diseaseID': {},
        'treatmentID': {},
        'riskID': {}
    }
    with open(constants_path, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header

        for row in reader:
            category, label, value = row
            if category in constants_reverse_lookup:
                constants_reverse_lookup[category][value] = label
    return constants_reverse_lookup

def load_country_iso_mapping(mapping_path):
    """
    Load GBModData_CountryMaster_0.csv to create a country to ISO mapping.
    """
    country_iso_mapping = {}
    with open(mapping_path, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country_name = row['Country'].strip()
            iso_code = row['ISO'].strip()
            country_iso_mapping[country_name] = iso_code
    return country_iso_mapping

def extract_starting_coverages(nc_data, constants_reverse_lookup):
    """
    Extract starting coverage values from the NC data for treatments and preventions.
    """
    coverages = []  # List of dictionaries: [{'intervention': '...', 'value': ..., 'type': 'Treatment/Prevention'}]

    i = 0
    while i < len(nc_data):
        row = nc_data[i]
        if not row:
            i += 1
            continue
        if row[0] == "<Treatment Association>" or row[0] == "<Prevention Association>":
            block_start = i
            block_type = row[0]
            # Now find the end of the block
            i += 1
            while i < len(nc_data) and nc_data[i][0] != "<End>":
                i += 1
            block_end = i
            # Process the block from block_start to block_end
            # Extract DiseaseID and TreatmentID/PreventionID
            disease_id = None
            intervention_id = None
            num_impacts = 1
            for j in range(block_start, block_end):
                if len(nc_data[j]) < 3:
                    continue
                if nc_data[j][1] == "DiseaseID":
                    disease_id = nc_data[j][2]
                elif nc_data[j][1] in ["treatID", "PreventionID"]:
                    intervention_id = nc_data[j][2]
                elif nc_data[j][1] == "NumImpacts":
                    num_impacts = int(nc_data[j][2])
            # Map IDs to names
            if disease_id and intervention_id:
                disease_name = constants_reverse_lookup['diseaseID'].get(disease_id, disease_id)
                if block_type == '<Treatment Association>':
                    intervention_name = constants_reverse_lookup['treatmentID'].get(intervention_id, intervention_id)
                else:
                    intervention_name = constants_reverse_lookup['treatmentID'].get(intervention_id, intervention_id)
                # Now find the <Coverages> section
                coverages_start = -1
                for j in range(block_start, block_end):
                    if nc_data[j][0] == "<Coverages>":
                        coverages_start = j + 1
                        break
                if coverages_start == -1:
                    print(f"No <Coverages> section found for {intervention_name}")
                    continue
                # Now extract coverages
                for k in range(num_impacts):
                    coverage_row_index = coverages_start + k
                    if coverage_row_index >= len(nc_data):
                        break
                    coverage_row = nc_data[coverage_row_index]
                    # coverage values are in coverage_row[5:]
                    coverage_values = coverage_row[5:]
                    # Get the first non-empty value
                    starting_coverage = next((v for v in coverage_values if v not in [None, '', ' ']), None)
                    try:
                        starting_coverage = float(starting_coverage)
                    except (ValueError, TypeError):
                        starting_coverage = None
                    coverages.append({
                        'intervention': intervention_name,
                        'value': starting_coverage,
                        'type': block_type.strip('<>')
                    })
            i = block_end  # Move to the end of the block
        else:
            i += 1
    return coverages

def extract_rf_starting_coverages(nc_data, constants_reverse_lookup):
    """
    Extract starting coverage values for risk factors from the NC data.
    """
    coverages = []  # List of dictionaries: [{'risk_factor': '...', 'level': ..., 'value': ...}]
    i = 0
    while i < len(nc_data):
        row = nc_data[i]
        if not row:
            i += 1
            continue
        if row[0] == " <RF Coverage V2 now with more levels>":
            # Found the start of the risk factors block
            rf_block_start = i
            # Skip header rows
            data_start = rf_block_start + 3
            # There are 58 risk factors, each with 12 rows
            num_risk_factors = 58
            rf_unit_size = 12
            for unit_index in range(num_risk_factors):
                base_index = data_start + unit_index * rf_unit_size
                # Get the risk factor ID from the first row of the unit
                rf_row = nc_data[base_index]
                if len(rf_row) < 2:
                    continue
                risk_id = rf_row[1]
                risk_name = constants_reverse_lookup['riskID'].get(risk_id, risk_id)
                for level_index in range(4):  # Levels 1 to 4
                    level_base_index = base_index + level_index * 3
                    level = level_index + 1
                    # Extract coverage from 'both sexes' row
                    coverage_row = nc_data[level_base_index]
                    # Ensure the row has enough columns
                    if len(coverage_row) < 4:
                        continue
                    coverage_values = coverage_row[3:]
                    # Get the first non-empty value
                    starting_coverage = next(
                        (v for v in coverage_values if v not in [None, '', ' ']), None)
                    try:
                        starting_coverage = float(starting_coverage)
                    except (ValueError, TypeError):
                        starting_coverage = None
                    coverages.append({
                        'risk_factor': risk_name,
                        'level': level,
                        'value': starting_coverage,
                        'type': 'Risk Factor'
                    })
            break  # Exit after processing risk factors
        else:
            i += 1
    return coverages

def main():
    constants_path = 'data/constants.csv'
    examples_dir = './examples/'
    country_iso_mapping_path = 'data/GBModData_CountryMaster_0.csv'
    output_csv = 'starting_coverages.csv'

    constants_reverse_lookup = load_constants(constants_path)
    country_iso_mapping = load_country_iso_mapping(country_iso_mapping_path)

    pjnz_files = [f for f in os.listdir(examples_dir) if f.endswith('.PJNZ')]

    all_coverages = []

    for pjnz_file in pjnz_files:
        pjnz_path = os.path.join(examples_dir, pjnz_file)
        # Extract the country name from the PJNZ filename (assuming it's the filename without extension)
        country_name = os.path.splitext(pjnz_file)[0]
        print(f"Processing {pjnz_file}, Country name: {country_name}")

        iso_code = country_iso_mapping.get(country_name)
        if not iso_code:
            print(f"ISO code not found for country '{country_name}'. Skipping.")
            continue

        with zipfile.ZipFile(pjnz_path, 'r') as pjnz_zip:
            # Find the NC file inside
            nc_filenames = [name for name in pjnz_zip.namelist() if name.endswith('.NC')]
            if not nc_filenames:
                print(f"No NC file found in {pjnz_file}")
                continue
            nc_filename = nc_filenames[0]
            with pjnz_zip.open(nc_filename) as nc_file:
                nc_lines = nc_file.read().decode('utf-8').splitlines()
                nc_data = list(csv.reader(nc_lines))

        # Extract starting coverages for treatments and preventions
        coverages = extract_starting_coverages(nc_data, constants_reverse_lookup)

        # Extract starting coverages for risk factors
        risk_factor_coverages = extract_rf_starting_coverages(nc_data, constants_reverse_lookup)

        # Add ISO code to each coverage entry
        for cov in coverages:
            all_coverages.append({
                'ISO': iso_code,
                'intervention': cov['intervention'],
                'value': cov['value'],
                'type': cov['type']
            })
        for rf_cov in risk_factor_coverages:
            all_coverages.append({
                'ISO': iso_code,
                'intervention': rf_cov['risk_factor'],
                'level': rf_cov['level'],
                'value': rf_cov['value'],
                'type': rf_cov['type']
            })

    # Write to CSV
    header = ['ISO', 'intervention', 'level', 'value', 'type']
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in all_coverages:
            writer.writerow(row)

if __name__ == '__main__':
    main()