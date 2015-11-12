"""
Create table from fasta file list...
"""
import argparse, sys, util, os
import numpy as np
from Bio import SeqIO
# Read in arguments for the script

def parse_args():
    # usage = "%prog -i INPUT_FASTQ_FILE"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inlist', help = 'input fasta file list', default='', required = True)
    parser.add_argument('-o', '--out_tb', help = 'output table file', default='', required = False)
    args = parser.parse_args()
    return args
    
# Find read length and read number, for calculating frequencies
def Create_table(inlist):
    # initiate dictionary
    dict = {}
    # read in each file:
    for i, fasta in enumerate(open(inlist)):
    	fastafile = fasta[:-1]
    	print i
	for item in dict:
            dict[item] += [-20]
    	for record in util.iter_fst(fastafile):
		sid, seq = record[:2]
    		sfreq = float(sid[1:])
    		if dict.has_key(seq) == False:
    			dict[seq] = [-20]*i + [sfreq]
    		else:
    			dict[seq][-1]= sfreq
#    print dict
    return dict
    
def write_table(dict,inlist,outfile):
    # open file, write first line
    f = open(outfile, 'w')
    f.write('id')
    for fasta in open(inlist):
	f.write('\t'+str(fasta[:-1]))
    f.write('\n')
    for item in dict:
	f.write(item)
	numbers = dict[item]
	for num in numbers:
	    f.write('\t'+str(num))
	f.write('\n')
    # Write everything...

def run():
	## Step 1
	args = parse_args()
	## Step 2
	dict = Create_table(args.inlist)
	## Step 3
	write_table(dict,args.inlist,args.out_tb)	
### Run it:
run()
