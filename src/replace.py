import zipfile
import os
import io

def replace_nc_file(source_pjnz: str, target_pjnz: str):
    """
    Replace the NC file in the source PJNZ with the NC file from the target PJNZ.
    """
    # Open source PJNZ
    with zipfile.ZipFile(source_pjnz, 'r') as source_zip:
        source_nc_filename = next(name for name in source_zip.namelist() if name.endswith('.NC'))
        
        # Open target PJNZ
        with zipfile.ZipFile(target_pjnz, 'r') as target_zip:
            target_nc_filename = next(name for name in target_zip.namelist() if name.endswith('.NC'))
            target_nc_content = target_zip.read(target_nc_filename)

        # Create a new PJNZ file with the replaced NC file
        output_filename = f"replaced_{os.path.basename(source_pjnz)}"
        with zipfile.ZipFile(output_filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as new_zip:
            for item in source_zip.infolist():
                if item.filename == source_nc_filename:
                    new_zip.writestr(item.filename, target_nc_content)
                else:
                    new_zip.writestr(item, source_zip.read(item.filename))

    print(f"NC file replaced. New PJNZ saved as {output_filename}")
