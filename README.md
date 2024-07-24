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
