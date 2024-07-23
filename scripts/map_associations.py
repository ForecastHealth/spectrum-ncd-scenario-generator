import csv
from collections import defaultdict
import sys
import argparse

def read_csv(file_path):
    with open(file_path, 'r') as f:
        return list(csv.DictReader(f))

def create_mapping(constants):
    mapping = defaultdict(dict)
    for row in constants:
        mapping[row['category']][row['value']] = row['label']
    return mapping

def map_associations(associations, mapping, show_all):
    mapped = []
    seen = set()
    for row in associations:
        if show_all or row['active'] == '1':
            disease_id = mapping['diseaseID'].get(row['diseaseID'], 'No Mapping Available')
            assoc_id = mapping['treatmentID'].get(row['id'], 'No Mapping Available')
            
            # Create a tuple of the key fields to check for duplicates
            key = (disease_id, row['association'], assoc_id)
            
            if key not in seen:
                seen.add(key)
                mapped.append({
                    'diseaseID': disease_id,
                    'association': row['association'],
                    'id': assoc_id,
                    'active': 'Active' if row['active'] == '1' else 'Inactive'
                })
    return mapped

def print_csv(data):
    writer = csv.DictWriter(sys.stdout, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

def main():
    parser = argparse.ArgumentParser(description='Map associations, filter by active status, and remove duplicates.')
    parser.add_argument('--all', action='store_true', help='Show both active and inactive associations')
    args = parser.parse_args()

    associations = read_csv('./src/associations.csv')
    constants = read_csv('./src/constants.csv')
    
    mapping = create_mapping(constants)
    mapped_associations = map_associations(associations, mapping, args.all)
    
    print_csv(mapped_associations)

if __name__ == "__main__":
    main()
