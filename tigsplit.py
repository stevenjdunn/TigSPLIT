#!/usr/bin/env python
import os
import argparse
import sys
import glob
from Bio import SeqIO

# Version
_verion_= "0.1"

# Argparse Setup
parser = argparse.ArgumentParser(description="A tool for splitting up .fasta files, creates a new file for each contig.")
parser.add_argument("-i", "--input", required=True, help="Path to directory containing .fasta files.")
parser.add_argument("-o", "--output", required=True, help="Path to output destination.")
args = parser.parse_args()

# Orientation + Directory Creation
print('####################')
print('Welcome to TigSPLIT!')
print('####################', '\n', '\n')
invoked_from = os.getcwd()
if not os.path.exists(args.output):
	try:
		os.makedirs(args.output)
		print('Output directory created.','\n')
	except Exception:
		print('Could not create output directory.','\n','\n', 'Please check whether you have the required permissions.')
		sys.exit(1)
os.chdir(args.output)
output_directory = os.getcwd()
os.chdir(invoked_from)
os.chdir(args.input)
input_directory = os.getcwd()
os.chdir(invoked_from)

# Fasta discovery
fasta_in = list(glob.glob(os.path.join(input_directory,'*.fasta')))
file_names = [x.replace(input_directory,'').replace('/','').replace('.fasta','') for x in fasta_in]
if len(fasta_in) == 0:
	print("Couldn't find any '.fasta' files in the input directory: ", input_directory,'\n')
	sys.exit(1)

# File splitting
print('Commencing file splits','\n','\n')

for input_file, file_ids in zip(fasta_in, file_names):
	for record in SeqIO.parse(open(input_file), "fasta"):
		output_file = os.path.join(output_directory,file_ids+'_'+record.id+'.fasta')
		SeqIO.write([record],open(output_file,'w'),"fasta")

# Farewell
print('Done!','\n')
print('Output files located in:', output_directory,'\n','\n')
print('Author: www.github.com/stevenjdunn','\n','\n')
print('#########')
print('Finished!')
print('#########')
