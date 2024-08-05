# NC File Processor

This tool processes NC files, either directly or within PJNZ files, updating coverage rates based on a provided configuration.

## Prerequisites

- Python 3.6 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - csv
  - json
  - logging
  - typing
  - zipfile

## File Structure

```
.
├── src/
│   ├── main.py
│   └── nc_processor.py
├── data/
│   ├── constants.csv
│   └── mapped_risk_ids.csv
├── config/
│   └── your_config_file.json
├── tmp/
│   └── (output files will be saved here)
└── README.md
```

## Usage

The tool can be used in two modes:

### 1. Processing PJNZ Files

To process a PJNZ file, extracting and updating its NC content:

```
python -m src.main pjnz <path_to_pjnz_file> <path_to_config_file>
```

Example:
```
python -m src.main pjnz ./data/example.PJNZ ./config/all_scenarios.json
```

### 2. Processing NC Files Directly

To process an NC file directly:

```
python -m src.main nc <path_to_nc_file> <path_to_config_file>
```

Example:
```
python -m src.main nc ./data/example.NC ./config/all_scenarios.json
```

## Running the tool for multiple countries and scenarios

This repository contains scripts for processing configuration templates and generating outputs. Here's a quick guide on how to use it:

### Main Components

1. `create_and_run_configurations.sh`: The main shell script that orchestrates the entire process.
2. `scripts/create_configurations.py`: Python script for creating configurations from templates.
3. `scripts/batch_individual_json_configs.sh`: Shell script for processing individual JSON configs.

### How to Run

1. Open a terminal and navigate to the repository root.

2. Run the main script:
   ```
   ./create_and_run_configurations.sh
   ```

3. Follow the prompts to select a configuration template.

### What Happens

1. The script lists available templates from `./templates/*.json`.
2. You select a template.
3. The script runs `python -m scripts.create_configurations` with your selected template.
4. It then processes the baseline configurations using `./scripts/batch_individual_json_configs.sh`.
5. Finally, it processes the scaleup configurations using the same script.

### Directory Structure

- Templates: `./templates/*.json`
- Output: `./config/{scenario}/{config_type}/`

### Tips

- Ensure all scripts are executable (`chmod +x script_name.sh`).
- Check that Python and required dependencies are installed.
- Make sure your template JSON files are in the `./templates/` directory.

Remember, this script automates the entire process from template selection to final output generation. If you need to run individual steps, you can use the component scripts directly.

## Output

The tool will generate the following outputs in the `./tmp` directory:

- For PJNZ processing: An updated PJNZ file and a log file
- For direct NC processing: An updated NC file and a log file

Output files are named based on the input file or configuration file name.

## Configuration

The configuration file (JSON format) should specify:

- Treatment associations
- Prevention associations
- Risk factors

Refer to the existing configuration files in the `config/` directory for the correct structure.

## Data Files

Ensure that `constants.csv` and `mapped_risk_ids.csv` are present in the `data/` directory. These files are used for lookups during processing.

## Logging

Detailed logs of the processing are saved alongside the output files in the `./tmp` directory.

## Contributing

For bug reports or feature requests, please open an issue on the project's GitHub repository.

