#!/bin/bash

# Check if a directory is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide a directory path as an argument."
    exit 1
fi

# Directory containing the JSON config files
CONFIG_DIR="$1"

# Check if the directory exists
if [ ! -d "$CONFIG_DIR" ]; then
    echo "Directory does not exist: $CONFIG_DIR"
    exit 1
fi

# Iterate through each JSON file in the directory
for config_file in "$CONFIG_DIR"/*.json; do
    # Check if the file exists (in case there are no JSON files)
    [ -e "$config_file" ] || continue

    # Extract metadata using jq
    pjnz_filename=$(jq -r '.metadata.pjnz_filename' "$config_file")
    iso3=$(jq -r '.metadata.iso3' "$config_file")
    scenario=$(jq -r '.metadata.scenario' "$config_file")

    # Check if all required metadata is present
    if [ -z "$pjnz_filename" ] || [ -z "$iso3" ] || [ -z "$scenario" ]; then
        echo "Warning: Missing required metadata in $config_file. Skipping."
        continue
    fi

    # Construct the PJNZ file path
    pjnz_path="$pjnz_filename"

    # Check if the PJNZ file exists
    if [ ! -f "$pjnz_path" ]; then
        echo "Warning: PJNZ file not found: $pjnz_path. Skipping."
        continue
    fi

    # Construct the output filename
    output_filename="${iso3}_${scenario}"
    echo "Processing: $iso3 ($scenario)"
    python -m src.main pjnz "$pjnz_path" "$config_file" "$output_filename"

    # Add a blank line for readability
    echo
done

echo "Processing complete."