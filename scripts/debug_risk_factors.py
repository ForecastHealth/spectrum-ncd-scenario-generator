import sys
import csv

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file.csv")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(sys.stdout)

        for row_number, row in enumerate(reader):
            if row_number == 0:
                # Assuming the first row is the header
                writer.writerow(['int', 'level', 'sex', 'value'])
                continue
            else:
                data_row_number = row_number - 1  # Adjusting for header
                sex = data_row_number % 3
                level = (data_row_number // 3) % 4 + 1
                int_value = (data_row_number // 12) + 1
                value = row[3] if len(row) > 3 else ''
                writer.writerow([int_value, level, sex, value])

if __name__ == "__main__":
    main()
