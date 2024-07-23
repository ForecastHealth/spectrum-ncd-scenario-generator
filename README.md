# spectrum-ncd-scenario-generator
CLI application to generate NCD scenarios by modifying PJNZ files

# Notes
map_data.txt is obtained from Spec5 -> NC -> NCDATA -> NCGBData.pas
This is the "master list" which seems to be accurate in terms of the map I would expect in Foo.nc
For example DiseaseID,14 corresponds to Asthma, whereas Spec5 -> NC -> NCData -> NCConst.pas -> DiseaseID, 14 corresponds to NC_Conduct
This is also true of the InterventionIDs
