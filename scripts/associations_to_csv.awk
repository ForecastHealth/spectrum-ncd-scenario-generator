#!/usr/bin/awk -f

BEGIN {
    FS = ","
    OFS = ","
    in_association = ""
    print "diseaseID,association,id,active"  # CSV header
}

/<Treatment Association>/ {
    in_association = "Treatment"
}

/<Prevention Association>/ {
    in_association = "Prevention"
}

/DiseaseID/ && (in_association == "Treatment" || in_association == "Prevention") {
    disease_id = $3
}

/treatID/ && in_association == "Treatment" {
    treat_id = $3
}

/PreventionID/ && in_association == "Prevention" {
    prevention_id = $3
}

/NumImpacts/ {
    for (i = 1; i <= NF; i++) {
        if ($i == "Active" || $i == "Inactive") {
            active = ($i == "Active" ? 1 : 0)
            break
        }
    }
    
    if (in_association == "Treatment") {
        print disease_id, "treatment", treat_id, active
    } else if (in_association == "Prevention") {
        print disease_id, "prevention", prevention_id, active
    }
    in_association = ""
}