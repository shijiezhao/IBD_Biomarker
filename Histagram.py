"""
For ploting the distribution of kmer frequencies
"""
import argparse, sys, util, os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Read in arguments for the script
def parse_args():
    usage = "%prog -i INPUT_FASTA_FILE"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputf', help = 'input fasta file for ploting', default='', required = True)
    args = parser.parse_args()
    return args

# Read fasta file and plot distribution
def dist(fasta):
    data = []
    for i,record in enumerate(util.iter_fst(fasta)):
	sid, seq = record[:2]
	logfreq = np.log10(float(sid[1:]))
	data.append(logfreq)
	if i > 100000:
	    break
    data = np.array(data)
    np.savetxt('test100000.out', data, delimiter = '\t')

# Main function
def run():
    ## 1. Read in arguments
    args = parse_args()
    ## 2. plot dist
    dist(args.inputf)

### Run it:
run()
