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

# Risk ID Mapping Script Development

## Problem Statement
We needed to develop a Python script to generate a CSV file mapping risk IDs to their corresponding levels and sexes. This mapping is based on the structure of a risk factor coverage data file, but without including the actual coverage data.

## Key Requirements
1. Generate a CSV with columns: index, riskID, level, sex
2. Use risk ID information from a constants file (`./src/constants.csv`)
3. Match the structure of the risk factor coverage data file (4 levels, 3 sexes per risk ID)
4. Do not include the actual coverage data in the output

## Solution Overview
We developed a Python script that:

1. Reads risk ID information from the constants file
2. Generates a mapping based on the structure of the risk factor coverage data
3. Outputs a CSV file with index, riskID, level, and sex information

## Key Features of the Script
- Reads and processes risk IDs from the constants file
- Generates a mapping without needing to read the full coverage data file
- Creates an index for each combination of riskID, level, and sex
- Handles potential errors in the constants file (e.g., empty or invalid entries)
- Outputs warnings and error messages to stderr for easier debugging

## Usage
The script is run from the command line and outputs the mapping data to stdout, which can be redirected to a file.

## Structure of the Output
- Index: A unique identifier for each row
- RiskID: The risk identifier from the constants file
- Level: Values from 1 to 4, representing different levels for each risk
- Sex: 'Both', 'Male', or 'Female'

## Future Considerations
- If the structure of risk levels or sex categories changes, the script will need to be updated
- The script relies on the format of the constants file remaining consistent
- If additional mapping information is needed in the future, the script can be easily extended

## Conclusion
This script provides a straightforward solution for generating a mapping of risk IDs to levels and sexes, based on the structure of the risk factor coverage data. It creates a useful reference file that can be used in conjunction with the actual coverage data for further analysis or processing.

# Claude Prompt for src/main.py

I am creating a small bit of software, which generates a .NC file. 

A .NC file is actually just a csv, but very idiosyncratically created for a particular piece of software. 

The goal is simple: take the instructions pass via a configuration e.g. config/all_scenarios.json, use the configuration to adjust template/foo.NC and output the data as e.g.`tmp/all_scenarios.NC`. Let's call the software that achieves this goal src/main.py and main.py for short.

Here is the structure of the repository:

.

├── config

│   └── all_scenarios.json

├── data

│   ├── associations.csv

│   ├── constants.csv

│   ├── mapped_associations.csv

│   ├── mapped_risk_ids.csv

│   ├── risk_factor_coverage_output.csv

│   └── unique_row_variables.txt

├── docs

│   └── index.html

├── README.md

├── scripts

│   ├── associations_to_csv.awk

│   ├── extract_associations.awk

│   ├── find_values.awk

│   ├── map_associations.py

│   └── map_risk_ids.py

├── src

│   └── main.py

├── templates

│   └── foo.NC

└── tmp

7 directories, 16 files

The configuration file is a JSON and has three keys: "treatment association", "prevention assocation" and "risk factor". These hold a list of dictionaries, which are largely the same. 

So main.py, has the following explicit requirements

- take a configuration as an argument
- load the .NC file as a CSV
- load ./data/constants.csv

Then, for any values in treatment association e.g, or prevention association, the following applies. 

```json
  "treatment associations": [

    {

      "disease": "NC_mstARF_RHD",

      "treatment": "NC_mstARF_PrimaryPrevention",

      "baseline_coverage": 0.05,

      "target_coverage": 0.05,

      "scaling_start_index": 1,

      "scaling_stop_index": 3

    }
]
```
or with prevention
```json
  "prevention associations": [
    {
      "disease": "NC_mstCVD",
      "prevention": "NC_mstPreventNonDiabSBPgt140",
      "baseline_coverage": 0.05,
      "target_coverage": 0.05,
      "scaling_start_index": 1,
      "scaling_stop_index": 3
    }
]
```

We are looking for the following structure: 

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
or with prevention
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
You'll notice that the DiseaseID an integer (17) and the treatID is an integer (93). So the first goal for treatment is to convert the "disease" key in the dictionary, to its corresponding DiseaseID. Then convert the "treatment" key into the corresponding treatID. For the prevention associations, instead of "treatment" and "treatID" it is "prevention" and "preventionID".

These can be found in the constants.csv that was loaded. 
The schema for constants.csv is: category,label,value
for disease, the category is diseaseID. The label will be the string value in the configuration, and the value is the corresponding integer.
For treatment and prevention association, the schema is the same, but the category is treatmentID (for both treatment and prevention).

So, to recap
- iterate through the list of dictionaries in treatment associations, then prevention associations
- for each dictionary, get the "disease" and get it's corresponding diseaseID from constants.csv (category "diseaseID")
- for each dictionary, get the "treatment" or "prevention" and get it's corresponding treatID or preventionID from constants.csv (category "treatmentID")

Then, the goal is to find this block of data within the foo.NC csv. We want to change the coverage rates. To do that, you need to:
- find either <Treatment Association> or <Prevention Association> in the first column. 
- Look to see whether it has the correct DiseaseID and treatID, or DiseaseID and PreventionID
- If true, go to the row of values in the row under <Coverages> and before <End>

From here, we have a few rules that will decide what our coverages should be. 
In each dictionary, we have the following keys and values:
```json
"baseline_coverage": 0.05,
"target_coverage": 0.15,
"scaling_start_index": 1,
"scaling_stop_index": 3
```
baseline_coverage says what the initial value should be. We need to convert this to a percentage, so if it is 0.05, we convert that to 5.
target coverage says what the final value should be after we "scale up", which is linearly scale from baseline_coverage to target_coverage.
scaling_start_index indicates the index where start linearly scaling up.
scaling_stop_index indicates the index where the target is reached.
All values after the stop_index are the same as the target_coverage.

so if we had the parameters above, and a simple coverages array of X,X,X,X,X,X: 
we would end up with an array of 5,5,10,15,15,15
that is, anything before and including the scaling_start_index of 1, is the baseline_coverage (array positions 0 and 1)
anything after and including the scaling_stop_index of 3 is the target_coverage array positions 3, 4, 5)
then array position two, is a result of the linear scale-up i.e. half way between 5 and 15, which is 10

That is all we need to do for treatment and prevention associations.

For risk factors, we are editing the coverage as well, in exactly the same manner, but the way we find the correct array is quite different.
Here is an example configuration for risk factors
```json
"risk factors": [
    {
      "risk factor": "NC_mstRFTobaccoPolicy",
      "baseline_coverage": 0.05,
      "target_coverage": 0.05,
      "scaling_start_index": 1,
      "scaling_stop_index": 3,
      "level": [1]
    }
]
```
You can see that all the coverage parameters are the same, and will be used in the same way (there is one more parameter, level, which we will get to).
However, there is only one variable to target the risk factor, in this example it is NC_mstRFTobaccoPolicy.

Within the foo.NC, risk factors are structured differently.
All coverages for risk factors exist under the tag 
 <RF Coverage V2 now with more levels>, for example
 ```csv
  <RF Coverage V2 now with more levels>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,58,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,4,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,,,,,,,,,
```
Importantly, the first two rows (the row with the value of 58, and the row with the value of 4) should be skipped.
After this, we have 696 rows of coverages, which are similar to the row of 100s. 
To find the appropriate index (e.g. position 0 thru position 695), you need to load ./data/mapped_risk_ids.csv. 

This csv has the schema: 
index,riskID,level,sex
The goal is to get the list of indices that we need, which give the correct rows of the coverags. 
To do this, take the "risk factor" e.g. NC_mstRFTobaccoPolicy, and take the levels e.g. [1]. Then search the csv, and retrieve all the indices that come back. 
For a particular risk factor with one level, there will be three indices, which represent coverages for "both sexes", "male" and "female". There are a total of four levels, therefore they may be a total of twelve indices for each risk factor variable. 

Then, you simple change the coverage rates in the same way you did for treatment associations and prevention associations.

Once this has been done for all entries in "treatment associations", "prevention associations", and "risk factors", you then save the full CSV (with the changed coverage rates) under ./tmp/ with the same filename as the configuration e.g. ./tmp/all_scenarios.NC

# Comprehensive NC File Generator Prompt

## Overview
You are tasked with creating a Python script (src/main.py) that generates a .NC file based on a JSON configuration. The .NC file is essentially a CSV with a specific structure used by particular software. The script should take a configuration as an argument, load the .NC file as a CSV, and load ./data/constants.csv.

## Repository Structure
```
.
├── config/
│   └── all_scenarios.json
├── data/
│   ├── associations.csv
│   ├── constants.csv
│   ├── mapped_associations.csv
│   ├── mapped_risk_ids.csv
│   ├── risk_factor_coverage_output.csv
│   └── unique_row_variables.txt
├── docs/
│   └── index.html
├── README.md
├── scripts/
│   ├── associations_to_csv.awk
│   ├── extract_associations.awk
│   ├── find_values.awk
│   ├── map_associations.py
│   └── map_risk_ids.py
├── src/
│   └── main.py
├── templates/
│   └── foo.NC
└── tmp/
```

## Input Configuration
The configuration file (JSON) has three main keys:
1. "treatment associations"
2. "prevention associations"
3. "risk factors"

Each key contains a list of dictionaries with similar structures.

### Example of "treatment associations":
```json
"treatment associations": [
  {
    "disease": "NC_mstARF_RHD",
    "treatment": "NC_mstARF_PrimaryPrevention",
    "baseline_coverage": 0.05,
    "target_coverage": 0.05,
    "scaling_start_index": 1,
    "scaling_stop_index": 3
  }
]
```

### Example of "prevention associations":
```json
"prevention associations": [
  {
    "disease": "NC_mstCVD",
    "prevention": "NC_mstPreventNonDiabSBPgt140",
    "baseline_coverage": 0.05,
    "target_coverage": 0.05,
    "scaling_start_index": 1,
    "scaling_stop_index": 3
  }
]
```

### Example of "risk factors":
```json
"risk factors": [
  {
    "risk factor": "NC_mstRFTobaccoPolicy",
    "baseline_coverage": 0.05,
    "target_coverage": 0.05,
    "scaling_start_index": 1,
    "scaling_stop_index": 3,
    "level": [1]
  }
]
```

## NC File Structure

### Treatment Association Structure:
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

### Prevention Association Structure:
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

### Risk Factor Structure:
```csv
<RF Coverage V2 now with more levels>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,58,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,4,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,,,,,,,,,
```

## Processing Steps

### For Treatment and Prevention Associations:
1. Iterate through the list of dictionaries in "treatment associations" and "prevention associations".
2. For each dictionary:
   a. Get the "disease" and its corresponding diseaseID from constants.csv (category "diseaseID").
   b. Get the "treatment" or "prevention" and its corresponding treatID or preventionID from constants.csv (category "treatmentID").
3. Find the corresponding block of data within the foo.NC csv:
   a. Look for either <Treatment Association> or <Prevention Association> in the first column.
   b. Check if it has the correct DiseaseID and treatID, or DiseaseID and PreventionID.
   c. If true, go to the row of values in the row under <Coverages> and before <End>.
4. Update the coverage rates based on the following parameters:
   - baseline_coverage: Initial value (convert to percentage, e.g., 0.05 to 5)
   - target_coverage: Final value after scaling up
   - scaling_start_index: Index where start linearly scaling up
   - scaling_stop_index: Index where the target is reached

### For Risk Factors:
1. Iterate through the "risk factors" list in the configuration.
2. For each risk factor:
   a. Find the correct array under the tag <RF Coverage V2 now with more levels>.
   b. Skip the first two rows (with values 58 and 4).
   c. Use ./data/mapped_risk_ids.csv to find the appropriate indices:
      - Schema: index,riskID,level,sex
      - Search for the "risk factor" (e.g., NC_mstRFTobaccoPolicy) and the specified levels.
      - Retrieve all matching indices (typically 3 per level for "both sexes", "male", and "female").
   d. Update the coverage rates for the retrieved indices using the same method as for treatment and prevention associations.

## Coverage Rate Calculation
- For values before and including the scaling_start_index: Use the baseline_coverage
- For values after and including the scaling_stop_index: Use the target_coverage
- For values between scaling_start_index and scaling_stop_index: Apply linear scaling

Example:
If baseline_coverage = 0.05 (5%), target_coverage = 0.15 (15%), scaling_start_index = 1, scaling_stop_index = 3, and we have 6 values:
Result: 5, 5, 10, 15, 15, 15

## Constants.csv
- Schema: category,label,value
- For diseases: category is "diseaseID"
- For treatments and preventions: category is "treatmentID"
- The label is the string value in the configuration
- The value is the corresponding integer

## mapped_risk_ids.csv
- Schema: index,riskID,level,sex
- Used to find the correct indices for risk factor coverages
- There may be up to 12 indices per risk factor (4 levels * 3 sex categories)

## Output
- Save the full CSV (with the changed coverage rates) under ./tmp/ with the same filename as the configuration (e.g., ./tmp/all_scenarios.NC)

## Additional Considerations
1. Code Structure:
   - Implement modular functions for each main task (e.g., parsing config, updating treatment associations, updating prevention associations, updating risk factors)
   - Use clear variable names and add comments for complex logic

2. Documentation:
   - Add detailed comments explaining the purpose and functionality of each major code block
   - Create a README.md file explaining how to use the script, its dependencies, and any setup required

3. Logging:
   - Implement logging to track the script's progress and any issues encountered during execution


## Sample Execution
```
python -m src.main.py config/all_scenarios.json
```

This command should:
1. Load the configuration from config/all_scenarios.json
2. Read the template from templates/foo.NC
3. Process the treatment associations, prevention associations, and risk factors
4. Update the coverage rates as specified
5. Save the result to tmp/all_scenarios.NC

## Dependencies
- Python 3.x
- Required Python libraries (e.g., csv, json) - list any additional libraries if needed

Remember to handle potential issues such as file I/O errors, invalid data formats, and unexpected input gracefully, providing clear error messages when problems occur.
