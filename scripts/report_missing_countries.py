import os
import csv
import argparse

def get_countries(file_path, is_csv=True):
    countries = set()
    if is_csv:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                countries.add(row[0].lower())
    else:
        for filename in os.listdir(file_path):
            name = os.path.splitext(filename)[0].lower()
            countries.add(name)
    return countries

def print_list(title, items):
    print(f"\n{title} ({len(items)}):")
    for item in sorted(items):
        print(item)

def main(args):
    csv_countries = get_countries('./data/GBModData_CountryMaster_0.csv', is_csv=True)
    example_countries = get_countries('examples', is_csv=False)

    in_csv_not_examples = csv_countries - example_countries
    in_examples_not_csv = example_countries - csv_countries
    in_both = csv_countries.intersection(example_countries)

    if args.summary:
        print("High-level Summary:")
        print(f"Countries in CSV: {len(csv_countries)}")
        print(f"Countries in examples: {len(example_countries)}")
        print(f"In CSV but not in examples: {len(in_csv_not_examples)}")
        print(f"In examples but not in CSV: {len(in_examples_not_csv)}")
        print(f"In both CSV and examples: {len(in_both)}")
    
    if args.csv_not_examples or args.all:
        print_list("In CSV but not in examples", in_csv_not_examples)
    
    if args.examples_not_csv or args.all:
        print_list("In examples but not in CSV", in_examples_not_csv)
    
    if args.in_both or args.all:
        print_list("In both CSV and examples", in_both)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare country lists in CSV and examples directory")
    parser.add_argument("--summary", action="store_true", help="Print high-level summary")
    parser.add_argument("--csv-not-examples", action="store_true", help="List countries in CSV but not in examples")
    parser.add_argument("--examples-not-csv", action="store_true", help="List countries in examples but not in CSV")
    parser.add_argument("--in-both", action="store_true", help="List countries in both CSV and examples")
    parser.add_argument("--all", action="store_true", help="Show all lists")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    else:
        main(args)