import json
import csv
import logging
from typing import Dict, List, Tuple
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path: str) -> Dict:
    """Load and return the JSON configuration file."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in configuration file: {config_path}")
        raise
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        raise

def load_csv(file_path: str) -> List[List[str]]:
    """Load and return a CSV file as a list of lists."""
    try:
        with open(file_path, 'r', newline='') as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        logging.error(f"CSV file not found: {file_path}")
        raise

def save_csv(file_path: str, data: List[List[str]]):
    """Save a list of lists as a CSV file."""
    try:
        with open(file_path, 'w', newline='') as f:
            csv.writer(f).writerows(data)
    except IOError:
        logging.error(f"Error writing to file: {file_path}")
        raise

def get_id_from_constants(constants: List[List[str]], category: str, label: str) -> str:
    """Get the ID for a given category and label from constants.csv."""
    for row in constants:
        if row[0] == category and row[1] == label:
            return row[2]
    logging.warning(f"ID not found for category '{category}' and label '{label}'")
    return ""

def find_block_in_nc(nc_data: List[List[str]], block_type: str, disease_id: str, treatment_id: str) -> Tuple[int, int]:
    """Find the start and end indices of a block in the NC file."""
    start_index = -1
    end_index = -1
    for i, row in enumerate(nc_data):
        if row and row[0] == f"<{block_type}>":
            start_index = i
        elif start_index != -1 and row and row[0] == "<End>":
            end_index = i
            break

        if start_index != -1 and len(row) > 2:
            if row[1] == "DiseaseID" and row[2] == disease_id:
                if block_type == "Treatment Association" and len(row) > 3 and row[3] == treatment_id:
                    break
                elif block_type == "Prevention Association" and len(row) > 3 and row[3] == treatment_id:
                    break
            elif row[1] == "PreventionID" and row[2] == treatment_id:
                break

    if start_index == -1 or end_index == -1:
        logging.warning(f"Block not found: {block_type}, DiseaseID: {disease_id}, TreatmentID: {treatment_id}")
        return -1, -1

    return start_index, end_index

def update_coverage_rates(coverages: List[str], baseline: float, target: float, start_index: int, stop_index: int) -> List[str]:
    """Update coverage rates based on the given parameters."""
    updated_coverages = coverages[:start_index]
    total_steps = stop_index - start_index
    
    for i in range(start_index, len(coverages)):
        if i < stop_index:
            rate = baseline + (target - baseline) * (i - start_index + 1) / total_steps
        else:
            rate = target
        updated_coverages.append(f"{rate:.3f}")

    return updated_coverages

def process_associations(nc_data: List[List[str]], associations: List[Dict], constants: List[List[str]], block_type: str) -> List[List[str]]:
    """Process treatment or prevention associations and update the NC data."""
    for assoc in associations:
        disease_id = get_id_from_constants(constants, "diseaseID", assoc["disease"])
        treatment_id = get_id_from_constants(constants, "treatmentID", assoc["treatment" if "treatment" in assoc else "prevention"])
        
        start_index, end_index = find_block_in_nc(nc_data, block_type, disease_id, treatment_id)
        if start_index == -1 or end_index == -1:
            continue

        for i in range(start_index, end_index):
            if nc_data[i][0] == "<Coverages>":
                coverages = nc_data[i + 1][5:]
                updated_coverages = update_coverage_rates(
                    coverages,
                    assoc["baseline_coverage"] * 100,
                    assoc["target_coverage"] * 100,
                    assoc["scaling_start_index"],
                    assoc["scaling_stop_index"]
                )
                nc_data[i + 1] = nc_data[i + 1][:5] + updated_coverages
                break

    return nc_data

def get_risk_factor_indices(mapped_risk_ids: List[List[str]], risk_factor: str, levels: List[int]) -> List[int]:
    """Get the indices for a risk factor from mapped_risk_ids.csv."""
    indices = []
    for row in mapped_risk_ids:
        if row[1] == risk_factor and int(row[2]) in levels:
            indices.append(int(row[0]))
    return indices

def process_risk_factors(nc_data: List[List[str]], risk_factors: List[Dict], mapped_risk_ids: List[List[str]]) -> List[List[str]]:
    """Process risk factors and update the NC data."""
    rf_start_index = -1
    rf_end_index = -1

    for i, row in enumerate(nc_data):
        if row and row[0] == "<RF Coverage V2 now with more levels>":
            rf_start_index = i
        elif rf_start_index != -1 and row and row[0] == "<End>":
            rf_end_index = i
            break

    if rf_start_index == -1 or rf_end_index == -1:
        logging.warning("Risk factor block not found in NC file")
        return nc_data

    for rf in risk_factors:
        indices = get_risk_factor_indices(mapped_risk_ids, rf["risk factor"], rf["level"])
        
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

    return nc_data

def main(config_path: str):
    """Main function to process the NC file based on the given configuration."""
    config = load_config(config_path)
    constants = load_csv("./data/constants.csv")
    mapped_risk_ids = load_csv("./data/mapped_risk_ids.csv")
    nc_data = load_csv("./templates/foo.NC")

    nc_data = process_associations(nc_data, config["treatment associations"], constants, "Treatment Association")
    nc_data = process_associations(nc_data, config["prevention associations"], constants, "Prevention Association")
    nc_data = process_risk_factors(nc_data, config["risk factors"], mapped_risk_ids)

    output_filename = os.path.splitext(os.path.basename(config_path))[0] + ".NC"
    output_path = os.path.join("./tmp", output_filename)
    save_csv(output_path, nc_data)
    logging.info(f"Updated NC file saved to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m src.main config/all_scenarios.json")
    else:
        main(sys.argv[1])