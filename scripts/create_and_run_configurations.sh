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
echo "Welcome to the configuration processing script."

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

# Process configurations
echo "Processing configurations..."
./scripts/batch_individual_json_configs.sh "./config/$scenario"

# Check if the processing was successful
if [ $? -ne 0 ]; then
    echo "Error: Configuration processing failed. Exiting."
    exit 1
fi

# Handle ExtractConfig.EX
echo "Updating ExtractConfig.EX for scenario $scenario..."

# Copy and rename ExtractConfig.EX
cp ./templates/ExtractConfig.EX "./tmp/$scenario/$scenario.EX"

# Count the number of .PJNZ files in the scenario directory
file_count=$(find "./tmp/$scenario" -name "*.PJNZ" | wc -l)

# Update the number of chosen projections and add filenames
sed -i "s/Number of chosen projections: ,1/Number of chosen projections: ,$file_count/" "./tmp/$scenario/$scenario.EX"

# Remove existing chosen projections
sed -i '/^,C:\\Users\\Administrator\\Documents\\/d' "./tmp/$scenario/$scenario.EX"

# Add new chosen projections
for file in "./tmp/$scenario"/*.PJNZ; do
    filename=$(basename "$file")
    echo ",C:\\Users\\Administrator\\Documents\\$scenario\\$filename" >> "./tmp/$scenario/$scenario.EX"
done

echo "All processing complete. Output files are located in tmp/$scenario/"
echo "ExtractConfig file updated: tmp/$scenario/$scenario.EX"