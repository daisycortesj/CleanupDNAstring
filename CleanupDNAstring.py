#!/usr/bin/env python3
# Name: Daisy Cortes (djcortes)

"""Create a program to "clean up" a sequence of DNA by removing ambiguous bases
(denoted by "N") output from the sequence. Read a DNA string from user input
and return a collapsed substring of embedded Ns to: {count}.
Example:
 input: AaNNNNNNGTC
output: AA{6}GTC
Any lower case letters are converted to uppercase"""

class DNAstring(str):
    def __init__(self, data):
        self.data = data

    def length(self):
        return len(self.data)  # Corrected the method to use len() instead of calling an undefined function.

    def purify(self):
        """Return an upcased version of the string, collapsing a single run of Ns."""
        self.data = self.data.upper()  # change string to uppercase
        N_count = self.data.count("N")  # count the number of N's in the string
        start_N = self.data.find("N")   # find the first occurrence of N
        end_N = self.data.rfind("N") + 1  # find the last occurrence of N and add 1 to exclude N itself
        replace_N = self.data[0:start_N] + '{' + str(N_count) + '}' + self.data[end_N:]
        # format: start of sequence, {number of Ns}, end of sequence
        return replace_N

def main():
    """Get user DNA data and clean it up."""

    data = input('DNA data? ')
    thisDNA = DNAstring(data)
    pureData = thisDNA.purify()
    print(pureData)

if __name__ == "__main__":
    main()
