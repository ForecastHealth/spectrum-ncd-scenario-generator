import os
import sys
from .nc_processor import process_pjnz_file, process_nc_file_direct, load_config
from .replace import replace_nc_file

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("1. For PJNZ processing: python -m src.main pjnz <path_to_pjnz_file> <path_to_config_file> [output_filename] [--log]")
        print("2. For direct NC processing: python -m src.main nc <path_to_nc_file> <path_to_config_file> [--log]")
        print("3. For replacing NC file: python -m src.main replace <source_pjnz> <target_pjnz>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "pjnz":
        if len(sys.argv) < 4:
            print("Usage for PJNZ processing: python -m src.main pjnz <path_to_pjnz_file> <path_to_config_file> [output_filename] [--log]")
            sys.exit(1)
        
        file_path = sys.argv[2]
        config_path = sys.argv[3]
        
        # Load config to get scenario
        config = load_config(config_path)
        scenario = config.get('metadata', {}).get('scenario', '')

        # Create scenario-specific output directory
        output_dir = os.path.join("./tmp", scenario)
        os.makedirs(output_dir, exist_ok=True)

        # Check if logging is enabled
        enable_logging = "--log" in sys.argv

        output_filename = next((arg for arg in sys.argv[4:] if not arg.startswith("--")), None)
        process_pjnz_file(file_path, config_path, output_dir, output_filename, enable_logging)

    elif command == "nc":
        if len(sys.argv) < 4:
            print("Usage for direct NC processing: python -m src.main nc <path_to_nc_file> <path_to_config_file> [--log]")
            sys.exit(1)
        
        file_path = sys.argv[2]
        config_path = sys.argv[3]
        
        # Load config to get scenario
        config = load_config(config_path)
        scenario = config.get('metadata', {}).get('scenario', '')

        # Create scenario-specific output directory
        output_dir = os.path.join("./tmp", scenario)
        os.makedirs(output_dir, exist_ok=True)

        # Check if logging is enabled
        enable_logging = "--log" in sys.argv

        process_nc_file_direct(file_path, config_path, output_dir, enable_logging)

    elif command == "replace":
        if len(sys.argv) != 4:
            print("Usage for replace: python -m src.main replace <source_pjnz> <target_pjnz>")
            sys.exit(1)
        source_pjnz = sys.argv[2]
        target_pjnz = sys.argv[3]
        replace_nc_file(source_pjnz, target_pjnz)

    else:
        print("Invalid command. Use 'pjnz', 'nc', or 'replace'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
