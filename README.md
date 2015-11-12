# IBD_Biomarker
1. preprocessing.sh
	-- This is the script that download SRA files, calculate the abundances of each 35-mers, then discard the raw files, 
	-- Only the processed files are reserved, for space purpose.

2. Jellyfish.py
	-- (1)Count 10, 20, 35 mer counts for every files
	-- (2)Select top freq. sequences

3. KmerFreq.py

4. Util.py

## Problem to solve:
1. How to kill a iterative nohup process... shit...

## TODOs:
1. Choose about 20/20 samples
2. Make unique sequence table out of that
3. Figure out a way to do statistical analysis: LefSe or others? Figure out LefSe first...
4. Clustering? Based on distribution? 





