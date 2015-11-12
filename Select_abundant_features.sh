#SH code, do large scale selecting for all files
A='.sel'
while read line
do python ~/scripts/Select_abundant_features.py -i $line -o $line$A 
done < filenames.txt




