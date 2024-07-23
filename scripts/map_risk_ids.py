import csv
import sys
import os

def process_risk_data(input_file):
    # Read the risk IDs from the CSV data
    risk_ids = []
    constants_file = './src/constants.csv'
    if not os.path.exists(constants_file):
        print(f"Error: {constants_file} not found. Please ensure the file exists in the correct location.", file=sys.stderr)
        sys.exit(1)

    with open(constants_file, 'r') as f:
        reader = csv.DictReader(f)
        for row_num, row in enumerate(reader, start=2):  # start=2 because row 1 is the header
            if row['category'] == 'riskID':
                if not row['value']:
                    print(f"Warning: Empty value for riskID on row {row_num} in {constants_file}. Skipping this row.", file=sys.stderr)
                    continue
                try:
                    risk_ids.append((int(row['value']), row['label']))
                except ValueError:
                    print(f"Error: Invalid value '{row['value']}' for riskID on row {row_num} in {constants_file}. Skipping this row.", file=sys.stderr)
    
    risk_ids.sort(key=lambda x: x[0])  # Sort by value
    
    print(f"Number of valid risk IDs: {len(risk_ids)}", file=sys.stderr)

    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        writer = csv.writer(sys.stdout)

        # Write header
        writer.writerow(['RiskID', 'Level', 'Sex'] + [f'Year_{i}' for i in range(1, 42)])

        risk_index = 0
        for row_index, row in enumerate(reader):
            if not any(row):  # Skip empty rows
                continue

            if risk_index < len(risk_ids):
                risk_id, risk_label = risk_ids[risk_index]
            else:
                print(f"Warning: Extra row found at row {row_index + 1}. Using 'Unknown' as risk label.", file=sys.stderr)
                risk_label = f"Unknown_{risk_index - len(risk_ids) + 1}"

            level = (row_index // 3) % 4 + 1
            sex_index = row_index % 3
            sex = ['Both', 'Male', 'Female'][sex_index]

            # Only write non-empty rows
            if any(row[3:]):
                writer.writerow([risk_label, level, sex] + row[3:44])  # Assuming 41 years of data

            # Move to the next risk ID when we've processed all levels and sexes
            if row_index % 12 == 11:
                risk_index += 1

        print(f"Processed {row_index + 1} rows", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.map_risk_ids input_file", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    process_risk_data(input_file)