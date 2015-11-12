"""
(1)Testing script, create entire fastafile
(2)For checking sequence distribution
"""
import argparse, sys, util, os
import subprocess
import numpy as np
# Read in arguments for the script
def parse_args():
    usage = "%prog -i INPUT_FASTQ_FILE"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputf', help = 'input fastq file for jellyfish excecution', default='', required = True)
    args = parser.parse_args()
    return args
# Find read length and read number, for calculating frequencies
def len_n_reads(fastq):
    fn = fastq
    # Using command line to calculate the read number
    command = ('wc -l '+str(fn))
    p = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE)
    text = p.stdout.read()
    words = text.split(' ')
    reads_number = int(words[0])/4
    # Read first line, find the length of each reads
    infile = open(fn, 'r')
    firstLine = infile.readline()
    Len=int(firstLine.split('=')[-1])
    return Len, reads_number

# Calculate frequencies for each reads from the fasta file...
def Freq_calculate(fasta, k, l, n, outfile):
    # Open the fasta file
    fn = fasta
    f = open(outfile,'w')
    for record in util.iter_fst(fn):
        sid, seq = record[:2]
        C = float(sid[1:])
        l = float(l)
        n = float(n)
        k = float(k)
        freq = C/((l-k+1)*n)
	if np.log10(freq) > -8.5:
	    q = '>'+str(freq)+'\n'+seq+'\n'
            f.write(q)
# Main function to run
def run():
    ## 1. Parse arguments
    args = parse_args()
    ## 2. Jellyfish calculation
    command3 = 'jellyfish count -m 35 -s 1000M -t 10 -C ' + args.inputf + '.fastq ' + '-o ' + args.inputf + '.jf'
    print command3
    os.system(command3)
    ## 3. Convert to fasta file
    command = 'jellyfish dump ' + args.inputf + '.jf > ' + args.inputf + '.fasta'
    os.system(command)
    ## 4. Find read length and read numbers
    [l,n] = len_n_reads(args.inputf + '.fastq')
    ## 5. Calculate sequence frequencies
    fasta = args.inputf + '.fasta'
    outfile = args.inputf + '.fasta' + '.norm'
    Freq_calculate(fasta,35,l,n,outfile)
    ## 6. Delete the fasta file
    os.system('rm '+ fasta)
    os.system('rm '+ args.inputf + '.jf')
## Run it...
run()
