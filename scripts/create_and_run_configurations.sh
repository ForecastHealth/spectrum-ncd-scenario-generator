#!/bin/bash

# Function to display the menu and get user selection
display_menu() {
    echo "Available configuration templates:"
    local i=1
    for template in ./templates/*.json; do
        echo "$i) $(basename "$template")"
        templates[$i]=$template
        ((i++))
    done
    echo "0) Exit"

    read -p "Select a template (0-$((i-1))): " choice
    if [[ $choice -eq 0 ]]; then
        echo "Exiting."
        exit 0
    elif [[ $choice -ge 1 && $choice -lt $i ]]; then
        selected_template=${templates[$choice]}
        echo "You selected: $selected_template"
    else
        echo "Invalid choice. Please try again."
        exit 1
    fi
}

# Main script execution
echo "Welcome to the combined processing script."

# Display menu and get user selection
display_menu

# Extract scenario name from the selected template filename
scenario=$(basename "$selected_template" .json | sed 's/.*_//')

# Run the Python script to create configurations
echo "Creating configurations..."
python -m scripts.create_configurations "$selected_template"

# Check if the Python script executed successfully
if [ $? -ne 0 ]; then
    echo "Error: Configuration creation failed. Exiting."
    exit 1
fi

# Process baseline configurations
echo "Processing baseline configurations..."
./scripts/batch_individual_json_configs.sh "./config/$scenario/baseline"

# Check if the baseline processing was successful
if [ $? -ne 0 ]; then
    echo "Error: Baseline configuration processing failed. Exiting."
    exit 1
fi

# Process scaleup configurations
echo "Processing scaleup configurations..."
./scripts/batch_individual_json_configs.sh "./config/$scenario/scaleup"

# Check if the scaleup processing was successful
if [ $? -ne 0 ]; then
    echo "Error: Scaleup configuration processing failed. Exiting."
    exit 1
fi

echo "All processing complete."