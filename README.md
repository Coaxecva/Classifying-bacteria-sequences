# Classifying-bacteria-sequences


awk "{outfile=sprintf(\"file%02d.txt\",NR/150+1);print > outfile}" bacteria.txt
