import json
import io
import csv
import logging
from typing import Dict, List, Union
import os
import zipfile

def setup_logging(log_file_path: str, enable_logging: bool):
    """Set up logging to both console and file if enabled."""
    if enable_logging:
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler(log_file_path, mode='w'),
                                logging.StreamHandler()
                            ])
        logging.info(f"Logging initialized. Log file: {log_file_path}")
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[logging.NullHandler()])

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

def process_risk_factors(template_nc: List[List[str]], scenario_nc: List[List[str]]) -> List[List[str]]:
    """Process risk factors and update the NC data."""
    logging.info("Processing risk factors")
    rf_start_index = -1
    rf_end_index = -1

    for i, row in enumerate(template_nc):
        if row and row[0] == " <RF Coverage V2 now with more levels>":
            rf_start_index = i
            logging.info(f"Found start of risk factor block at row {i}")
        elif rf_start_index != -1 and row and row[0] == "<Risk Factor Stata>":
            rf_end_index = i
            logging.info(f"Found end of risk factor block at row {i}")
            break

    if rf_start_index == -1 or rf_end_index == -1:
        logging.warning("Risk factor block not found in template NC file")
        return template_nc

    # Find corresponding block in scenario NC
    scenario_rf_start = find_corresponding_block(scenario_nc, " <RF Coverage V2 now with more levels>")
    if scenario_rf_start == -1:
        logging.warning("Risk factor block not found in scenario NC file")
        return template_nc

    # Update risk factor coverages
    for i in range(rf_start_index + 3, rf_end_index):  # +3 to skip header rows
        template_row = template_nc[i]
        scenario_row = scenario_nc[scenario_rf_start + (i - rf_start_index)]

        # Update coverages, trimming scenario values to match template length
        template_nc[i] = template_row[:3] + scenario_row[3:3+len(template_row[3:])]

    logging.info("Finished processing risk factors")
    return template_nc

def load_nc_file(file_path: str) -> List[List[str]]:
    """Load and return an NC file as a list of lists."""
    logging.info(f"Loading NC file: {file_path}")
    try:
        with open(file_path, 'r', newline='') as f:
            data = list(csv.reader(f))
        logging.info(f"NC file loaded successfully: {len(data)} rows")
        return data
    except FileNotFoundError:
        logging.error(f"NC file not found: {file_path}")
        raise

def process_nc_file(template_nc: List[List[str]], scenario_nc: List[List[str]]) -> List[List[str]]:
    """Process the NC file, updating coverages from scenario NC file."""
    logging.info("Starting to process NC file")
    
    updated_nc = template_nc.copy()
    current_block_type = None
    block_start_index = -1
    
    for i, row in enumerate(updated_nc):
        if not row:  # Skip empty rows
            continue

        if row[0] in ["<Treatment Association>", "<Prevention Association>"]:
            current_block_type = row[0].strip('<>')
            block_start_index = i
            logging.info(f"Found start of {current_block_type} block at row {i}")
        elif row[0] == "<End>" and current_block_type in ["Treatment Association", "Prevention Association"]:
            update_coverage_block(updated_nc, scenario_nc, block_start_index, i, current_block_type)
            current_block_type = None
            block_start_index = -1

    # Process risk factors separately
    updated_nc = process_risk_factors(updated_nc, scenario_nc)

    logging.info("Finished processing NC file")
    return updated_nc

def update_coverage_block(template_nc: List[List[str]], scenario_nc: List[List[str]], start_index: int, end_index: int, block_type: str):
    """Update a single Treatment, Prevention, or Risk Factor coverage block."""
    coverages_start = -1
    for i in range(start_index, end_index):
        if template_nc[i][0] == "<Coverages>" or (block_type == "RF Coverage V2 now with more levels" and i == start_index + 3):
            coverages_start = i + 1
            break

    if coverages_start == -1:
        logging.warning(f"No <Coverages> section found in {block_type} block")
        return

    # Find corresponding block in scenario NC
    scenario_block_start = find_corresponding_block(scenario_nc, template_nc[start_index][0])
    if scenario_block_start == -1:
        logging.warning(f"Corresponding {block_type} block not found in scenario NC")
        return

    scenario_coverages_start = scenario_block_start + (coverages_start - start_index)

    for i in range(coverages_start, end_index):
        template_row = template_nc[i]
        scenario_row = scenario_nc[scenario_coverages_start + (i - coverages_start)]

        if block_type == "RF Coverage V2 now with more levels":
            coverage_start = 3
        else:
            coverage_start = 5

        # Update coverages, trimming scenario values to match template length
        template_nc[i] = template_row[:coverage_start] + scenario_row[coverage_start:coverage_start+len(template_row[coverage_start:])]

    logging.info(f"Updated coverages for {block_type} block")

def find_corresponding_block(scenario_nc: List[List[str]], block_header: str) -> int:
    """Find the starting index of the corresponding block in the scenario NC file."""
    for i, row in enumerate(scenario_nc):
        if row and row[0] == block_header:
            return i
    return -1

def process_nc_content(template_nc: Union[str, List[List[str]]], scenario_nc_path: str) -> List[List[str]]:
    """Process NC content based on the template and scenario NC files."""
    if isinstance(template_nc, str):
        template_nc_data = load_nc_file(template_nc)
    else:
        template_nc_data = template_nc
    
    scenario_nc_data = load_nc_file(scenario_nc_path)

    return process_nc_file(template_nc_data, scenario_nc_data)

def process_pjnz_file(pjnz_path: str, config_path: str, output_dir: str, output_filename: str = None, enable_logging: bool = False):
    """Process a PJNZ file, update its NC content, and create a new compressed PJNZ file."""
    config = load_config(config_path)
    metadata = config.get('metadata', {})
    iso3 = metadata.get('iso3', '')
    scenario = metadata.get('scenario', '')
    
    # Ensure output_dir exists
    os.makedirs(output_dir, exist_ok=True)
    
    if output_filename:
        output_filename = f"{output_filename}.PJNZ"
    else:
        output_filename = f"{iso3}_{scenario}.PJNZ"
    
    log_file_path = os.path.join(output_dir, f"{output_filename}.log")
    setup_logging(log_file_path, enable_logging)
    
    scenario_nc_path = os.path.join('./a3_projections', f"{scenario}.NC")

    with zipfile.ZipFile(pjnz_path, 'r') as pjnz_file:
        nc_filename = next(name for name in pjnz_file.namelist() if name.endswith('.NC'))
        template_nc_content = list(csv.reader(pjnz_file.open(nc_filename).read().decode('utf-8').splitlines()))

    updated_nc_content = process_nc_content(template_nc_content, scenario_nc_path)

    output_pjnz_path = os.path.join(output_dir, output_filename)
    with zipfile.ZipFile(output_pjnz_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as new_pjnz_file:
        for item in zipfile.ZipFile(pjnz_path, 'r').infolist():
            if item.filename == nc_filename:
                nc_data = io.StringIO()
                csv.writer(nc_data).writerows(updated_nc_content)
                new_pjnz_file.writestr(item.filename, nc_data.getvalue(), compress_type=zipfile.ZIP_DEFLATED)
            else:
                new_pjnz_file.writestr(item, zipfile.ZipFile(pjnz_path, 'r').read(item.filename), compress_type=zipfile.ZIP_DEFLATED)

    logging.info(f"Updated and compressed PJNZ file saved to {output_pjnz_path}")

def process_nc_file_direct(nc_path: str, config_path: str, output_dir: str, enable_logging: bool = False):
    """Process an NC file directly and output the updated NC file."""
    config = load_config(config_path)
    metadata = config.get('metadata', {})
    iso3 = metadata.get('iso3', '')
    scenario = metadata.get('scenario', '')
    
    # Ensure output_dir exists
    os.makedirs(output_dir, exist_ok=True)
    
    output_filename = f"{iso3}_{scenario}.NC"
    output_nc_path = os.path.join(output_dir, output_filename)
    log_file_path = os.path.join(output_dir, f"{output_filename}.log")
    setup_logging(log_file_path, enable_logging)

    scenario_nc_path = os.path.join('./a3_projections', f"{scenario}.NC")

    updated_nc_content = process_nc_content(nc_path, scenario_nc_path)
    save_csv(output_nc_path, updated_nc_content)

    logging.info(f"Updated NC file saved to {output_nc_path}")
