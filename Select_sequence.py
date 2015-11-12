"""
Selecting sequences that begin with certain sequences
"""
from Bio import SeqIO
import argparse, os
# Read in arguments for the script
def parse_args():
    usage = "%prog -i INPUT_FASTA_FILE -s Sequence_to_select -o Output_FASTA"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputf', help = 'input fasta file', default='', required = True)
    parser.add_argument('-s', '--seqs', help = 'input starting sequence', default='', required = True)
    parser.add_argument('-o', '--outputf', help = 'output fasta file', default='', required = True)
    args = parser.parse_args()
    return args

def selecting_sequence(fasta,sequence,outfile):
    L = len(sequence)
    output_handle = open(outfile, "w")
    for record in SeqIO.parse(fasta, "fasta"):
	if record.seq[0:L] == sequence:
	    SeqIO.write(record, output_handle, "fasta")
    output_handle.close()

def run():
    ## Step 1
    args = parse_args()
    ## Step 2: Make an directory to store the info
    os.system('mkdir '+args.seqs)
    ## Step 3: Store info
    outfile = args.seqs + '/' + args.outputf
    selecting_sequence(args.inputf, args.seqs, outfile)


### Run it!
run()

