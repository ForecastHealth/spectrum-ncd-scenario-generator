import json
import csv
import logging
from typing import Dict, List
import os
import zipfile

def setup_logging(log_file_path: str):
    """Set up logging to both console and file."""
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_file_path, mode='w'),
                            logging.StreamHandler()
                        ])
    logging.info(f"Logging initialized. Log file: {log_file_path}")

def load_config(config_path: str) -> Dict:
    """Load and return the JSON configuration file."""
    logging.info(f"Loading configuration file: {config_path}")
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        logging.info(f"Configuration file loaded successfully")
        return config
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in configuration file: {config_path}")
        raise
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        raise

def load_csv(file_path: str) -> List[List[str]]:
    """Load and return a CSV file as a list of lists."""
    logging.info(f"Loading CSV file: {file_path}")
    try:
        with open(file_path, 'r', newline='') as f:
            data = list(csv.reader(f))
        logging.info(f"CSV file loaded successfully: {len(data)} rows")
        return data
    except FileNotFoundError:
        logging.error(f"CSV file not found: {file_path}")
        raise

def save_csv(file_path: str, data: List[List[str]]):
    """Save a list of lists as a CSV file."""
    logging.info(f"Saving CSV file: {file_path}")
    try:
        with open(file_path, 'w', newline='') as f:
            csv.writer(f).writerows(data)
        logging.info(f"CSV file saved successfully: {len(data)} rows")
    except IOError:
        logging.error(f"Error writing to file: {file_path}")
        raise

def create_constants_lookup(constants: List[List[str]]) -> Dict[str, Dict[str, str]]:
    """Create a lookup dictionary from constants.csv."""
    logging.info("Creating constants lookup")
    lookup = {}
    for category, label, value in constants:
        if category not in lookup:
            lookup[category] = {}
        lookup[category][label] = value
    logging.info(f"Constants lookup created: {len(lookup)} categories")
    return lookup

def update_coverage_rates(coverages: List[str], baseline: float, target: float, start_index: int, stop_index: int) -> List[str]:
    """Update coverage rates based on the given parameters."""
    logging.info(f"Updating coverage rates: Baseline {baseline:.1f}, Target {target:.1f}, Start Index {start_index}, Stop Index {stop_index}")
    
    # Find the first non-empty value and the last value
    first_non_empty = next((i for i, v in enumerate(coverages) if v), 0)
    last_non_empty = len(coverages) - 1 - next((i for i, v in enumerate(reversed(coverages)) if v), 0)
    
    updated_coverages = coverages[:first_non_empty]
    
    for i in range(first_non_empty, len(coverages)):
        if i <= start_index:
            rate = baseline
        elif i >= stop_index:
            rate = target
        else:
            progress = (i - start_index) / (stop_index - start_index)
            rate = baseline + (target - baseline) * progress
        
        if i <= last_non_empty:
            updated_coverages.append(f"{rate:.1f}")
        else:
            updated_coverages.append("")

    logging.info(f"Coverage rates updated: {len(updated_coverages)} values")
    return updated_coverages

def get_risk_factor_indices(mapped_risk_ids: List[List[str]], risk_factor: str, levels: List[int]) -> List[int]:
    """Get the indices for a risk factor from mapped_risk_ids.csv."""
    logging.info(f"Getting risk factor indices for: {risk_factor}, Levels: {levels}")
    indices = []
    for row in mapped_risk_ids:
        if row[1] == risk_factor and int(row[2]) in levels:
            indices.append(int(row[0]))
    logging.info(f"Found {len(indices)} matching indices for risk factor: {risk_factor}")
    return indices

def process_risk_factors(nc_data: List[List[str]], risk_factors: List[Dict], mapped_risk_ids: List[List[str]]) -> List[List[str]]:
    """Process risk factors and update the NC data."""
    logging.info(f"Processing risk factors: {len(risk_factors)} risk factors")
    rf_start_index = -1
    rf_end_index = -1

    for i, row in enumerate(nc_data):
        if row and row[0] == " <RF Coverage V2 now with more levels>":
            rf_start_index = i
            logging.info(f"Found start of risk factor block at row {i}")
        elif rf_start_index != -1 and row and row[0] == "<Risk Factor Stata>":
            rf_end_index = i
            logging.info(f"Found end of risk factor block at row {i}")
            break

    if rf_start_index == -1 or rf_end_index == -1:
        logging.warning("Risk factor block not found in NC file")
        return nc_data

    for rf in risk_factors:
        risk_factor = rf["risk factor"]
        indices = get_risk_factor_indices(mapped_risk_ids, risk_factor, rf["levels"])
        
        if not indices:
            logging.warning(f"Risk Factor: No matching indices found for {risk_factor}")
            continue

        logging.info(f"Risk Factor: Processing {risk_factor}")
        logging.info(f"  Levels: {rf['levels']}")
        logging.info(f"  Matching indices: {indices}")

        for index in indices:
            coverages = nc_data[rf_start_index + 3][3:]
            updated_coverages = update_coverage_rates(
                coverages,
                rf["baseline_coverage"] * 100,
                rf["target_coverage"] * 100,
                rf["scaling_start_index"],
                rf["scaling_stop_index"]
            )
            nc_data[rf_start_index + 3 + index] = nc_data[rf_start_index + 3 + index][:3] + updated_coverages
            
            logging.info(f"  Updated coverages for index {index}")
            logging.info(f"    Baseline: {rf['baseline_coverage']:.2f}, Target: {rf['target_coverage']:.2f}")
            logging.info(f"    Start Index: {rf['scaling_start_index']}, Stop Index: {rf['scaling_stop_index']}")
            logging.info(f"    Original coverages: {coverages}")
            logging.info(f"    Updated coverages: {updated_coverages}")

    return nc_data

def process_nc_file(nc_data: List[List[str]], config: Dict, constants_lookup: Dict[str, Dict[str, str]], mapped_risk_ids: List[List[str]]) -> List[List[str]]:
    """Process the NC file, updating Treatment and Prevention Associations as encountered."""
    logging.info("Starting to process NC file")
    
    current_block_type = None
    block_start_index = -1
    
    for i, row in enumerate(nc_data):
        if not row:  # Skip empty rows
            continue

        if row[0] == "<Treatment Association>" or row[0] == "<Prevention Association>":
            current_block_type = row[0][1:-1]  # Remove < and >
            block_start_index = i
            logging.info(f"Found start of {current_block_type} block at row {i}")
        elif row[0] == "<End>" and current_block_type in ["Treatment Association", "Prevention Association"]:
            process_association_block(nc_data, block_start_index, i, current_block_type, config, constants_lookup)
            current_block_type = None
            block_start_index = -1
        elif row[0] == " <RF Coverage V2 now with more levels>":
            logging.info("Found start of Risk Factor block")
            nc_data = process_risk_factors(nc_data, config["risk factors"], mapped_risk_ids)
            break  # Assuming risk factors are at the end of the file

    logging.info("Finished processing NC file")
    return nc_data

def process_association_block(nc_data: List[List[str]], start_index: int, end_index: int, block_type: str, config: Dict, constants_lookup: Dict[str, Dict[str, str]]):
    """Process a single Treatment or Prevention Association block."""
    disease_id = None
    treatment_id = None
    num_impacts = 1

    for i in range(start_index, end_index):
        if nc_data[i][1] == "DiseaseID":
            disease_id = nc_data[i][2]
        elif nc_data[i][1] in ["treatID", "PreventionID"]:
            treatment_id = nc_data[i][2]
        elif nc_data[i][1] == "NumImpacts":
            num_impacts = int(nc_data[i][2])
            logging.info(f"Number of impacts for this block: {num_impacts}")

    if not disease_id or not treatment_id:
        logging.warning(f"Invalid {block_type} block: missing DiseaseID or treatID/PreventionID")
        return

    # Look up the association in the config
    association_type = "treatment associations" if block_type == "Treatment Association" else "prevention associations"
    matching_assoc = next((assoc for assoc in config[association_type] 
                           if constants_lookup["diseaseID"].get(assoc["disease"]) == disease_id
                           and constants_lookup["treatmentID"].get(assoc.get("treatment") or assoc.get("prevention")) == treatment_id), 
                          None)

    if not matching_assoc:
        logging.info(f"No matching configuration found for {block_type}: DiseaseID {disease_id}, TreatmentID {treatment_id}")
        return

    # Update coverages
    coverages_start = -1
    for i in range(start_index, end_index):
        if nc_data[i][0] == "<Coverages>":
            coverages_start = i + 1
            break

    if coverages_start == -1:
        logging.warning(f"No <Coverages> section found in {block_type} block: DiseaseID {disease_id}, TreatmentID {treatment_id}")
        return

    for j in range(num_impacts):
        current_row = coverages_start + j
        if current_row >= end_index:
            logging.warning(f"Unexpected end of block while processing coverages: DiseaseID {disease_id}, TreatmentID {treatment_id}")
            break

        coverages = nc_data[current_row][5:]
        updated_coverages = update_coverage_rates(
            coverages,
            matching_assoc["baseline_coverage"] * 100,
            matching_assoc["target_coverage"] * 100,
            matching_assoc["scaling_start_index"],
            matching_assoc["scaling_stop_index"]
        )
        nc_data[current_row] = nc_data[current_row][:5] + updated_coverages
        logging.info(f"Updated coverages for {block_type}: DiseaseID {disease_id}, TreatmentID {treatment_id}, Impact {j + 1} of {num_impacts}")
        logging.info(f"  Baseline: {matching_assoc['baseline_coverage']:.2f}, Target: {matching_assoc['target_coverage']:.2f}")
        logging.info(f"  Start Index: {matching_assoc['scaling_start_index']}, Stop Index: {matching_assoc['scaling_stop_index']}")
        logging.info(f"  Original coverages: {coverages}")
        logging.info(f"  Updated coverages: {updated_coverages}")

    logging.info(f"Finished processing {block_type} block: DiseaseID {disease_id}, TreatmentID {treatment_id}")

def process_nc_content(nc_content: List[List[str]], config_path: str) -> List[List[str]]:
    """Process NC content based on the given configuration."""
    config = load_config(config_path)
    constants = load_csv("./data/constants.csv")
    constants_lookup = create_constants_lookup(constants)
    mapped_risk_ids = load_csv("./data/mapped_risk_ids.csv")

    return process_nc_file(nc_content, config, constants_lookup, mapped_risk_ids)

def process_pjnz_file(pjnz_path: str, config_path: str, output_dir: str):
    """Process a PJNZ file, update its NC content, and create a new PJNZ file."""
    setup_logging(os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pjnz_path))[0]}.log"))
    
    with zipfile.ZipFile(pjnz_path, 'r') as pjnz_file:
        nc_filename = next(name for name in pjnz_file.namelist() if name.endswith('.NC'))
        nc_content = list(csv.reader(pjnz_file.open(nc_filename).read().decode('utf-8').splitlines()))

    updated_nc_content = process_nc_content(nc_content, config_path)

    output_pjnz_path = os.path.join(output_dir, os.path.basename(pjnz_path))
    with zipfile.ZipFile(output_pjnz_path, 'w') as new_pjnz_file:
        for item in zipfile.ZipFile(pjnz_path, 'r').infolist():
            if item.filename == nc_filename:
                new_pjnz_file.writestr(item.filename, '\n'.join([','.join(row) for row in updated_nc_content]))
            else:
                new_pjnz_file.writestr(item, zipfile.ZipFile(pjnz_path, 'r').read(item.filename))

    logging.info(f"Updated PJNZ file saved to {output_pjnz_path}")

def process_nc_file_direct(nc_path: str, config_path: str, output_dir: str):
    """Process an NC file directly and output the updated NC file."""
    output_filename = os.path.splitext(os.path.basename(config_path))[0]
    output_nc_path = os.path.join(output_dir, f"{output_filename}.NC")
    setup_logging(os.path.join(output_dir, f"{output_filename}.log"))

    nc_content = load_csv(nc_path)
    updated_nc_content = process_nc_content(nc_content, config_path)
    save_csv(output_nc_path, updated_nc_content)

    logging.info(f"Updated NC file saved to {output_nc_path}")