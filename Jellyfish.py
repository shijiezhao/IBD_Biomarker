"""
(1)Count 10, 20, 35 mer counts for every files
(2)Select top freq. sequences
"""
import argparse, sys, util, os
import subprocess
# Read in arguments for the script
def parse_args():
    usage = "%prog -i INPUT_FASTQ_FILE"
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_filename', default='', dest='name')
    args = parser.parse_args()

    # Check for consistency: not necessary here
    return args

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

args = parse_args()
command1 = 'jellyfish count -m 10 -s 1000M -t 10 -C ' + args.name + '.fastq ' + '-o ' + args.name + '_10.jf'
command2 = 'jellyfish count -m 20 -s 1000M -t 10 -C ' + args.name + '.fastq ' + '-o ' + args.name + '_20.jf'
command3 = 'jellyfish count -m 35 -s 1000M -t 10 -C ' + args.name + '.fastq ' + '-o ' + args.name + '.jf'

print command3
os.system(command1)
os.system(command2)
os.system(command3)

## See read length
[l,n] = len_n_reads(args.name+'.fastq')
if l == 44:
    com = 'jellyfish dump -L 35 ' + args.name + '.jf > ' + args.name + '.fasta' 
    print com
    os.system(com)
if l == 75:
    com = 'jellyfish dump -L 100 ' + args.name + '.jf > ' + args.name + '.fasta'
    print com
    os.system(com)



