# TigSPLIT
**A tool for splitting up .fasta files, creates a new file for each contig.**

## Dependencies
- Python 3
- Biopython

## Quick start
    tigsplit.py -i /path/to/input_directory/ -o /path/to/output_directory/
    
## Usage:     
    usage: tigsplit.py [-h] -i INPUT -o OUTPUT

    Splits .fasta's creating a new file for each contig.

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            Path to directory containing .fasta files.
      -o OUTPUT, --output OUTPUT
                            Path to output destination.

## Why?
I use it to extract plasmid sequences from large, complete/very-nearly-completed bacterial genome datasets. Once the script finishes, I remove any file at or close to the target genome size (i.e. the chromosome) and process the remaining files (mostly plasmids) separately. 
