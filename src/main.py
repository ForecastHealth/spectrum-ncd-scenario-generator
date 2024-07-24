import json
import csv
import logging
from typing import Dict, List, Tuple
import os

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

def find_block_in_nc(nc_data: List[List[str]], block_type: str, disease_id: str, treatment_id: str) -> Tuple[int, int]:
    """Find the start and end indices of a block in the NC file."""
    logging.info(f"Searching for block: {block_type}, DiseaseID: {disease_id}, TreatmentID: {treatment_id}")
    start_index = -1
    end_index = -1
    disease_matched = False
    treatment_matched = False

    for i, row in enumerate(nc_data):
        if row and row[0] == f"<{block_type}>":
            start_index = i
            disease_matched = False
            treatment_matched = False
            logging.info(f"Found start of {block_type} block at row {i}")
            continue

        if start_index != -1:
            if row and row[0] == "<End>":
                if disease_matched and treatment_matched:
                    end_index = i
                    logging.info(f"Found end of matching {block_type} block at row {i}")
                    break
                else:
                    logging.info(f"Found end of non-matching {block_type} block at row {i}")
                    start_index = -1
                    continue

            if len(row) > 2:
                if row[1] == "DiseaseID" and row[2] == disease_id:
                    logging.info(f"Matched DiseaseID {disease_id} at row {i}")
                    disease_matched = True
                elif row[1] == "treatID" and row[2] == treatment_id:
                    logging.info(f"Matched treatID {treatment_id} at row {i}")
                    treatment_matched = True
                elif row[1] == "PreventionID" and row[2] == treatment_id:
                    logging.info(f"Matched PreventionID {treatment_id} at row {i}")
                    treatment_matched = True

    if start_index == -1 or end_index == -1:
        logging.warning(f"Block not found: {block_type}, DiseaseID: {disease_id}, TreatmentID: {treatment_id}")
        return -1, -1

    logging.info(f"Block found: {block_type}, Start: {start_index}, End: {end_index}")
    return start_index, end_index

def update_coverage_rates(coverages: List[str], baseline: float, target: float, start_index: int, stop_index: int) -> List[str]:
    """Update coverage rates based on the given parameters."""
    logging.info(f"Updating coverage rates: Baseline {baseline:.2f}, Target {target:.2f}, Start Index {start_index}, Stop Index {stop_index}")
    updated_coverages = coverages[:start_index]
    total_steps = stop_index - start_index
    
    for i in range(start_index, len(coverages)):
        if i < stop_index:
            rate = baseline + (target - baseline) * (i - start_index + 1) / total_steps
        else:
            rate = target
        updated_coverages.append(f"{rate:.3f}")

    logging.info(f"Coverage rates updated: {len(updated_coverages)} values")
    return updated_coverages

def process_associations(nc_data: List[List[str]], associations: List[Dict], constants_lookup: Dict[str, Dict[str, str]], block_type: str) -> List[List[str]]:
    """Process treatment or prevention associations and update the NC data."""
    logging.info(f"Processing {block_type}s: {len(associations)} associations")
    for assoc in associations:
        disease = assoc["disease"]
        treatment_key = "treatment" if "treatment" in assoc else "prevention"
        treatment = assoc[treatment_key]

        disease_id = constants_lookup["diseaseID"].get(disease)
        treatment_id = constants_lookup["treatmentID"].get(treatment)

        if not disease_id or not treatment_id:
            logging.warning(f"{block_type}: No match found for Disease: {disease} or {treatment_key.capitalize()}: {treatment}")
            continue

        logging.info(f"{block_type}: Processing Disease: {disease} (ID: {disease_id}), {treatment_key.capitalize()}: {treatment} (ID: {treatment_id})")

        start_index, end_index = find_block_in_nc(nc_data, block_type, disease_id, treatment_id)
        if start_index == -1 or end_index == -1:
            logging.warning(f"{block_type}: Block not found for Disease ID: {disease_id}, {treatment_key.capitalize()} ID: {treatment_id}")
            continue

        num_impacts = 1
        for i in range(start_index, end_index):
            if nc_data[i][1] == "NumImpacts":
                num_impacts = int(nc_data[i][2])
                logging.info(f"{block_type}: Number of impacts: {num_impacts}")
                break

        coverages_updated = False
        for i in range(start_index, end_index):
            if nc_data[i][0] == "<Coverages>":
                for j in range(num_impacts):
                    coverages = nc_data[i + 1 + j][5:]
                    updated_coverages = update_coverage_rates(
                        coverages,
                        assoc["baseline_coverage"] * 100,
                        assoc["target_coverage"] * 100,
                        assoc["scaling_start_index"],
                        assoc["scaling_stop_index"]
                    )
                    nc_data[i + 1 + j] = nc_data[i + 1 + j][:5] + updated_coverages
                    logging.info(f"{block_type}: Updated coverages for Disease ID: {disease_id}, {treatment_key.capitalize()} ID: {treatment_id}, Row: {j + 1}")
                    logging.info(f"  Baseline: {assoc['baseline_coverage']:.2f}, Target: {assoc['target_coverage']:.2f}")
                    logging.info(f"  Start Index: {assoc['scaling_start_index']}, Stop Index: {assoc['scaling_stop_index']}")
                    logging.info(f"  Original coverages: {coverages}")
                    logging.info(f"  Updated coverages: {updated_coverages}")
                coverages_updated = True
                break
        
        if not coverages_updated:
            logging.warning(f"{block_type}: Coverages not updated for Disease ID: {disease_id}, {treatment_key.capitalize()} ID: {treatment_id}")

    return nc_data

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

def main(config_path: str):
    """Main function to process the NC file based on the given configuration."""
    # Create output directory if it doesn't exist
    output_dir = "./tmp"
    os.makedirs(output_dir, exist_ok=True)

    output_filename = os.path.splitext(os.path.basename(config_path))[0]
    output_nc_path = os.path.join(output_dir, f"{output_filename}.NC")
    output_log_path = os.path.join(output_dir, f"{output_filename}.log")

    setup_logging(output_log_path)

    logging.info(f"Starting processing for configuration: {config_path}")

    config = load_config(config_path)
    constants = load_csv("./data/constants.csv")
    constants_lookup = create_constants_lookup(constants)
    mapped_risk_ids = load_csv("./data/mapped_risk_ids.csv")
    nc_data = load_csv("./templates/foo.NC")

    nc_data = process_associations(nc_data, config["treatment associations"], constants_lookup, "Treatment Association")
    nc_data = process_associations(nc_data, config["prevention associations"], constants_lookup, "Prevention Association")
    nc_data = process_risk_factors(nc_data, config["risk factors"], mapped_risk_ids)

    save_csv(output_nc_path, nc_data)
    logging.info(f"Updated NC file saved to {output_nc_path}")
    logging.info(f"Log file saved to {output_log_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m src.main config/all_scenarios.json")
    else:
        main(sys.argv[1])
