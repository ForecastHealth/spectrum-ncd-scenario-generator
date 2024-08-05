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
    iso3=$(jq -r '.metadata.iso3 // empty' "$config_file")
    scenario=$(jq -r '.metadata.scenario // empty' "$config_file")
    scaleup_type=$(jq -r '.metadata.scaleup_type // empty' "$config_file")

    # Check if all required metadata is present
    if [ -z "$pjnz_filename" ]; then
        echo "Warning: Missing pjnz_filename in $config_file. Skipping."
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
    if [ -n "$iso3" ] && [ -n "$scenario" ] && [ -n "$scaleup_type" ]; then
        output_filename="${iso3}_${scenario}_${scaleup_type}"
        echo "Processing: $iso3 ($scenario, $scaleup_type)"
        python -m src.main pjnz "$pjnz_path" "$config_file" "$output_filename"
    else
        echo "Processing: $pjnz_filename"
        python -m src.main pjnz "$pjnz_path" "$config_file"
    fi

    # Add a blank line for readability
    echo
done

echo "Processing complete."