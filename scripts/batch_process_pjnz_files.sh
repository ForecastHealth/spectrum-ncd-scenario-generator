#!/bin/bash

# Directory containing PJNZ files
PJNZ_DIR="./examples"

# Directory containing configuration files
CONFIG_DIR="./templates"

# Output directory
OUTPUT_DIR="./tmp"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# List available configurations
echo "Available configurations:"
configs=($(ls "$CONFIG_DIR"/*.json))
for i in "${!configs[@]}"; do
    echo "$((i+1)). $(basename "${configs[$i]}" .json)"
done

# Prompt user to select a configuration
echo "Select which configuration you'd like to use:"
read -p "Enter the number: " config_num

# Validate user input
if ! [[ "$config_num" =~ ^[0-9]+$ ]] || [ "$config_num" -lt 1 ] || [ "$config_num" -gt "${#configs[@]}" ]; then
    echo "Invalid selection. Exiting."
    exit 1
fi

# Get selected configuration
selected_config="${configs[$((config_num-1))]}"
config_name=$(basename "$selected_config" .json)

echo "Selected configuration: $config_name"

# Process each PJNZ file
for pjnz_file in "$PJNZ_DIR"/*.PJNZ; do
    if [ -f "$pjnz_file" ]; then
        pjnz_filename=$(basename "$pjnz_file")
        output_filename="${pjnz_filename%.*}_${config_name}.PJNZ"
        echo "Processing $pjnz_filename..."
        python -m src.main pjnz "$pjnz_file" "$selected_config"
        # Rename the output file to match the desired naming convention
        mv "$OUTPUT_DIR/$pjnz_filename" "$OUTPUT_DIR/$output_filename"
        echo "Output saved as $output_filename"
    fi
done

echo "Processing complete. All output files are in the $OUTPUT_DIR directory."
