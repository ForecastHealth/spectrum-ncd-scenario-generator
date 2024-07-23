import csv
import sys
from pathlib import Path

def generate_risk_mapping(constants_file, output_file):
    # Read risk IDs from constants file
    risk_ids = []
    with open(constants_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['category'] == 'riskID':
                risk_ids.append(row['label'])

    # Generate mapping
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['index', 'riskID', 'level', 'sex'])
        index = 0
        for risk_id in risk_ids:
            for level in range(1, 5):
                for sex in ['Both', 'Male', 'Female']:
                    writer.writerow([index, risk_id, level, sex])
                    index += 1

    print(f"Mapping generated successfully. Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <constants_file_path> <output_file_path>")
        sys.exit(1)

    constants_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not constants_file.is_file():
        print(f"Error: Constants file {constants_file} not found.")
        sys.exit(1)

    generate_risk_mapping(constants_file, output_file)