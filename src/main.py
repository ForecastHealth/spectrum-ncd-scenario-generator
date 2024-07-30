import os
import sys
from .nc_processor import process_pjnz_file, process_nc_file_direct

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("1. For PJNZ processing: python -m src.main pjnz <path_to_pjnz_file> <path_to_config_file> [output_filename]")
        print("2. For direct NC processing: python -m src.main nc <path_to_nc_file> <path_to_config_file>")
        sys.exit(1)

    command = sys.argv[1]
    file_path = sys.argv[2]
    config_path = sys.argv[3]

    output_dir = "./tmp"
    os.makedirs(output_dir, exist_ok=True)

    if command == "pjnz":
        output_filename = sys.argv[4] if len(sys.argv) > 4 else None
        process_pjnz_file(file_path, config_path, output_dir, output_filename)
    elif command == "nc":
        process_nc_file_direct(file_path, config_path, output_dir)
    else:
        print("Invalid command. Use 'pjnz' or 'nc'.")
        sys.exit(1)

if __name__ == "__main__":
    main()