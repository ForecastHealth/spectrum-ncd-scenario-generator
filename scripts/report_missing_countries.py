import os
import csv

# Read country names from CSV
csv_countries = set()
with open('./data/GBModData_CountryMaster_0.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        csv_countries.add(row[0].lower())  # Assuming country name is in second column

# Get filenames from examples directory
example_countries = set()
for filename in os.listdir('examples'):
    name = os.path.splitext(filename)[0].lower()
    example_countries.add(name)

# Find countries in CSV that aren't in examples
missing_countries = csv_countries - example_countries

print("Countries in CSV that aren't in examples:")
for country in sorted(missing_countries):
    print(country)

print(f"\nTotal missing countries: {len(missing_countries)}")
