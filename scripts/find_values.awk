#!/usr/bin/awk -f

BEGIN {
    FS = ","
    association = ""
}

{
    for (i = 1; i <= NF; i++) {
        if ($i ~ /<[^>]+ Association>/) {
            association = $i
            print "Found Association:", association
        }
        if ($i == "<Coverages>") {
            if (association != "") {
                print "Result:", association, "- <Coverages>"
                association = ""  # Reset association after matching
            } else {
                print "Warning: Found <Coverages> but no preceding Association"
            }
        }
    }
}

END {
    if (association != "") {
        print "Warning: Found Association but no subsequent <Coverages>:", association
    }
}