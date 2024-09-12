import sys
import os
import zipfile
import tempfile
import subprocess

def edit_nc_in_pjnz(pjnz_path):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract the NC file from the PJNZ
        with zipfile.ZipFile(pjnz_path, 'r') as pjnz_file:
            nc_filename = next(name for name in pjnz_file.namelist() if name.endswith('.NC'))
            pjnz_file.extract(nc_filename, temp_dir)
        
        nc_path = os.path.join(temp_dir, nc_filename)
        
        # Open the NC file in nvim
        subprocess.call(['nvim', nc_path])
        
        # After nvim is closed, update the PJNZ with the modified NC file
        with zipfile.ZipFile(pjnz_path, 'a') as pjnz_file:
            pjnz_file.write(nc_path, nc_filename)

    print(f"PJNZ file updated: {pjnz_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python edit_pjnz_nc.py <path_to_pjnz_file>")
        sys.exit(1)

    pjnz_path = sys.argv[1]
    if not os.path.exists(pjnz_path):
        print(f"Error: File not found: {pjnz_path}")
        sys.exit(1)

    edit_nc_in_pjnz(pjnz_path)
