"""
Determine the frequencies of each kmer from a fastq/fasta file
"""
import argparse, sys, util
import subprocess
# Read in arguments for the script
def parse_args():
    usage = "%prog -j INPUT_JELLYFISH_FILE -x INPUT_FASTQ/FASTA_FILE -o OUTPUT_FILE"	
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--input_jf_fasta', default='', dest='jfasta')
    parser.add_argument('-q', '--input_fastq', default='', dest='fastq')
    parser.add_argument('-o', '--output_fasta', default='', dest='output')
    parser.add_argument('-k', '--kmer_length', default=35, dest='kl')
    args = parser.parse_args()

    # Check for consistency: not necessary here
    return args

# Find the length and reads number from fastq file
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
	freq = C/((l-k+1)*n)
	#q = '< k:'+str(k)+' l:'+str(l)+' n:'+str(n)+' C:'+str(C)+' Freq='+str(freq)+'\n'+seq+'\n'
	q = '<'+str(freq)+'\n'+seq+'\n'
	f.write(q)

# The main function:
def run():
    ## 1. Get command line arguments
    args = parse_args()
    print args
    ## 2. Determine read length and read number
    [l,n] = len_n_reads(fastq=args.fastq)
    ## 3. Output
    Freq_calculate(fasta=args.jfasta, k=args.kl, l=l, n=n, outfile=args.output)

# Run it...:
run()

