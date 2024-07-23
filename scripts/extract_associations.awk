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
    prevention_id = $3
    prevention_desc = ""
    for (i = 4; i <= NF; i++) {
        if ($i ~ /^"/) {
            prevention_desc = $i
            for (j = i + 1; j <= NF; j++) {
                prevention_desc = prevention_desc "," $j
                if ($j ~ /"$/) break
            }
            break
        }
    }
    gsub(/^"|"$/, "", prevention_desc)  # Remove surrounding quotes
    print "PreventionID:", prevention_id
    print "Prevention Description:", prevention_desc
}

/NumImpacts/ && in_association == "Prevention" {
    print "Status:", ($5 == "Active" ? "Active" : "Inactive")
    print "---"
    in_association = ""
}