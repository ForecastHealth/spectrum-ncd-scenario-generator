# spectrum-ncd-scenario-generator
CLI application to generate NCD scenarios by modifying PJNZ files

# Notes
map_data.txt is obtained from Spec5 -> NC -> NCDATA -> NCGBData.pas
This is the "master list" which seems to be accurate in terms of the map I would expect in Foo.nc
For example DiseaseID,14 corresponds to Asthma, whereas Spec5 -> NC -> NCData -> NCConst.pas -> DiseaseID, 14 corresponds to NC_Conduct
This is also true of the InterventionIDs

# Treatment Association
Need DiseaseID
treatID
Active
<Coverages>
```csv
<Treatment Association>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,DiseaseID,17,1,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,treatID,93,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,Set,93,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,NumImpacts,1,,1,Active,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,Sens,100,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
<PINByYear>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,<Age ID>,<State ID>,<Trans ID>,<ToState ID>,<Impact Value>,<Start Cov>,<Final Cov>,<Year Final Cov>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,<Start>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,1,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,2,3,2,78,-80,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,3,3,2,78,-80,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,4,3,2,78,0,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,5,3,2,78,0,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,6,3,2,78,0,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,7,3,2,78,0,10,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,8,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,9,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,10,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,11,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,12,3,2,78,0,0,0,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,<End>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
<Coverages>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,,,,,,,
<End>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```

# Prevention Association
DiseaseID
PreventionID
Active
Coverages
```csv
<Prevention Association>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,DiseaseID,1,1,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,PreventionID,2,Comb. Tx for total CVD risk > 30%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,Set,2,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,NumImpacts,2,,1,Inactive,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,Sens,100,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,<Age ID>,<State ID>,<Risk ID>,<ToState ID>,<Impact Value>,<Start Cov>,<Final Cov>,<Year Final Cov>,<State ID>,<Risk ID>,<ToState ID>,<Impact Value>,<Start Cov>,<Final Cov>,<Year Final Cov>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,<Start>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,1,3,14,4,0,0,50,2064,3,14,2,0,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,2,3,14,4,0,0,50,2064,3,14,2,0,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,3,3,14,4,0,0,50,2064,3,14,2,0,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,4,3,14,4,0,0,50,2064,3,14,2,0,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,5,3,14,4,0,0,50,2064,3,14,2,0,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,6,3,14,4,1.41237,0,50,2064,3,14,2,0.85286,0,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,7,3,14,4,10.3076,5,50,2064,3,14,2,8.47574,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,8,3,14,4,10.3076,5,50,2064,3,14,2,8.47574,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,9,3,14,4,8.62998,5,50,2064,3,14,2,7.23987,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,10,3,14,4,4.85155,5,50,2064,3,14,2,2.47749,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,11,3,14,4,2.64557,5,50,2064,3,14,2,0,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,12,3,14,4,2.64557,5,50,2064,3,14,2,0,5,50,2064,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,<End>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
<Coverages>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,5,6.125,7.25,8.375,9.5,10.625,11.75,12.875,14,15.125,16.25,17.375,18.5,19.625,20.75,21.875,23,24.125,25.25,26.375,27.5,28.625,29.75,30.875,32,33.125,34.25,35.375,36.5,37.625,38.75,39.875,41,42.125,43.25,44.375,45.5,46.625,47.75,48.875,50,,,,,,,
,,,,,5,6.125,7.25,8.375,9.5,10.625,11.75,12.875,14,15.125,16.25,17.375,18.5,19.625,20.75,21.875,23,24.125,25.25,26.375,27.5,28.625,29.75,30.875,32,33.125,34.25,35.375,36.5,37.625,38.75,39.875,41,42.125,43.25,44.375,45.5,46.625,47.75,48.875,50,,,,,,,
<End>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```


# NCD Scenario Generator Scripts 2024-07-23 14:14

This repository contains a set of scripts designed to process and analyze data related to Non-Communicable Disease (NCD) scenarios. These scripts work together to extract, transform, and map data from various input files to produce meaningful outputs for further analysis.

## Script Descriptions

### 1. Association Extractor (AWK)

**Filename:** `extract_associations_csv_clean.awk`

**Purpose:** This AWK script processes a complex, custom-formatted CSV file containing information about disease treatments and preventions.

**Functionality:**
- Identifies Treatment and Prevention Associations within the input file.
- Extracts key information including diseaseID, association type (treatment or prevention), ID, and active status.
- Outputs a clean CSV format with columns: diseaseID, association, id, active.

**Usage:**
```
awk -f extract_associations_csv_clean.awk input_file.NC > associations.csv
```

### 2. Constants Extractor (AWK)

**Filename:** `extract_disease_ids.awk` and `extract_treatment_ids.awk`

**Purpose:** These AWK scripts process a text file containing constant definitions for diseases and treatments.

**Functionality:**
- Extracts disease IDs and names from the input file.
- Extracts treatment IDs and names from the input file.
- Outputs two separate CSV files: one for diseases and one for treatments.

**Usage:**
```
awk -f extract_disease_ids.awk constants_input.txt > DiseaseID.csv
awk -f extract_treatment_ids.awk constants_input.txt > TreatmentID.csv
```

### 3. Association Mapper (Python)

**Filename:** `map_associations.py`

**Purpose:** This Python script maps the extracted associations to their corresponding names using the constants files.

**Functionality:**
- Reads the associations CSV produced by the Association Extractor.
- Reads the constants CSVs (DiseaseID.csv and TreatmentID.csv).
- Maps the numeric IDs in the associations file to their corresponding names from the constants files.
- Provides an option to filter results based on active status.
- Outputs the mapped data to stdout in CSV format.

**Features:**
- Command-line flag `--all` to include both active and inactive associations (default is active only).
- Handles missing mappings by displaying "No Mapping Available".
- Converts the active status to readable "Active" or "Inactive" in the output.

**Usage:**
```
python map_associations.py > mapped_active_associations.csv
python map_associations.py --all > mapped_all_associations.csv
```

## Workflow

1. Run the Association Extractor on your input .NC file to generate the associations CSV.
2. Run the Constants Extractors on your constants input file to generate DiseaseID.csv and TreatmentID.csv.
3. Use the Association Mapper to combine the data from steps 1 and 2, mapping IDs to names and filtering as needed.

This set of scripts provides a comprehensive solution for processing complex NCD scenario data, from raw input files to a clean, mapped CSV output suitable for further analysis or reporting.

---

This description provides an overview of each script, its purpose, functionality, and usage instructions. It also outlines the overall workflow for using these scripts together. You can include this in your README file to give users a clear understanding of the tools available in your repository and how to use them.
