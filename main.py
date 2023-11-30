#!/usr/bin/env python3
# Name: Daisy Cortes (djcortes)

# Count AT
"""This program is supposed to ask the user to enter a DNA sequence and
then output the number of As and Ts divided by the sequencing length
as a fraction of the total sequence length"""

class dnaString (str):
    def length (self):
        return (len(self))

    def getAT(self):
        num_A = self.count('A')
        num_T = self.count('T')
        return ((num_A + num_T) / len(self))

dna = input("Enter a dna sequence: ")
upperDNA = dna.upper()
coolString = dnaString(upperDNA)

print("AT content = {0:0.1f}".format(coolString.getAT()))

# Counting DNA Letters
""" Create program that will ask the user to enter a DNA sequence then output 
the total sequence length and number of each base {total of As, Cs, Gs, Ts} 
found in each sequence """


class dnaString(str):
    def length(self):
        return (len(self))

    def getAT(self):
        num_A = self.count(A)
        num_T = self.count("T")
        return ((num_A + num_T) / self.len())

    # Counting the number of A's found in the string and will repeat till last letter
    def countNucleotideA(self):
        num_A = self.count('A')
        return num_A

    def countNucleotideC(self):
        num_C = self.count('C')
        return num_C

    def countNucleotideT(self):
        num_T = self.count('T')
        return num_T

    def countNucleotideG(self):
        num_G = self.count('G')
        return num_G


dna = input("Enter a dna sequence: ")
upperDNA = dna.upper()
coolString = dnaString(upperDNA)

print("number A's = {}, number C's = {}, number T's {}, number G's {}".format(
    coolString.countNucleotideA(),
    coolString.countNucleotideC(), coolString.countNucleotideT(), coolString.countNucleotideG()))
