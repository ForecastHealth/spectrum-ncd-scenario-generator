BEGIN {
    FS = ","
    in_association = ""
}

/<Treatment Association>/ {
    in_association = "Treatment"
    print "Found Treatment Association"
}

/<Prevention Association>/ {
    in_association = "Prevention"
    print "Found Prevention Association"
}

/DiseaseID/ && in_association == "Treatment" {
    print "DiseaseID:", $3
}

/treatID/ && in_association == "Treatment" {
    print "treatID:", $3
}

/NumImpacts/ && in_association == "Treatment" {
    print "Status:", ($5 == "Active" ? "Active" : "Inactive")
    print "---"
    in_association = ""
}

/DiseaseID/ && in_association == "Prevention" {
    print "DiseaseID:", $3
}

/PreventionID/ && in_association == "Prevention" {
    print "PreventionID:", $3
    print "Prevention Description:", $4
}

/NumImpacts/ && in_association == "Prevention" {
    print "Status:", ($5 == "Active" ? "Active" : "Inactive")
    print "---"
    in_association = ""
}