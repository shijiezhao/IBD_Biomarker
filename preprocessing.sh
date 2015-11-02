#sh
#Do the preprossing staff

A='_1'
B='_2'
C='.fastq'
D='.jf'
E='.fasta'
F='.norm'

while read line
# Download SRA files
#do fastq-dump $line --split-files -v
# Calculate 10, 20, and 35mers
# Dump fasta for 35mers
do python ~/scripts/Jellyfish.py -i $line$A
python ~/scripts/Jellyfish.py -i $line$B
# Do normalization
python ~/scripts/KmerFreq.py -j $line$A$E -q $line$A$C -k 35 -o $line$A$F
python ~/scripts/KmerFreq.py -j $line$B$E -q $line$B$C -k 35 -o $line$B$F
# Remove the fastq files, for the sake that the storage is not enough...
rm $line$A$C
rm $line$B$C

done < batch1
