"""
Selecting sequences that have frequencies higher than certain threshold
"""
from Bio import SeqIO
import argparse, os
import numpy as np
# Read in arguments for the script
def parse_args():
    usage = "%prog -i INPUT_FASTA_FILE -f Frequency_cutoff -o Output_directory"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputf', help = 'input fasta file', default='', required = True)
    parser.add_argument('-f', '--freq', help = 'frequency cutoff', type = float, default='', required = True)
    parser.add_argument('-o', '--outdir', help = 'output directory', default='', required = True)
    args = parser.parse_args()
    return args

def selecting_sequence(fasta,freq,outfile):
    output_handle = open(outfile, "w")
    for record in SeqIO.parse(fasta, "fasta"):
	if np.log10(float(record.id)) > freq:
	    record.id = record.name = record.description = str(np.log10(float(record.id)))
	    SeqIO.write(record, output_handle, "fasta")
    output_handle.close()

def run():
    ## Step 1
    args = parse_args()
    ## Step 2: Make an directory to store the info
    ## Step 3: Store info
    outfile = args.outdir + '/' + args.inputf
    selecting_sequence(args.inputf, args.freq, outfile)


### Run it!
run()
