#!/usr/bin/env python3
# Name: Daisy Cortes (djcortes)

# FastqParse
"""Parsing a FASTQ file involves extracting relevant information from the sequence to obtain 
information about the instrument, run ID, flow cell ID, and flow cell lane """

#class is FastqString

class FastqString(str):
    """Class docstring goes here."""
    # takes seq_name argument and initializes
    def __init__(self, seqName):
        self.seqName = seqName
    
    # splits the store sequence name using ":"
    # at least four elements in split sequence name
        # if there are four elements then returns a string
        # string containing information about instrument: run ID, flow cell ID, etc 
    
    def parse(self):
        """Method docstring goes here."""
        split_seq_name = self.seqName.split(':')
        if len(split_seq_name) >= 4:
            return ('Instrument = {0}\n Run ID= {1}\n Flow Cell ID = {2} \n Flow Cell Lane = {3}\n'.format(
                split_seq_name[0],
                split_seq_name[1],
                split_seq_name[2],
                split_seq_name[3]
            ))
        else:
            return 'Error: Invalid FASTQ sequence name format'

# prompts user to enter FASTQ sequence name
# creates an instance of the FastqString with the entered sequence name
# parse to extract info
def main():
    '''Function docstring goes here.'''
    seqName = input('Please enter FASTQ seqname: ')
    FASTQ = FastqString(seqName)
    result = FASTQ.parse()
    print(result)

if __name__ == "__main__":
    main()



