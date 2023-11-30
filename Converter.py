C
''' The purpose of this script is to convert and display information
about three-letter DNA or RNA codons. It includes dictionaries representing
the genetic code for amino acids and codons, as well as a class (Converter)
to find and display information about a given codon
'''
# A dictionary mapping short three-letter amino acid codes to their corresponding one-letter codes.
short_AA = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
# A dictionary mapping one-letter amino acid codes back to their corresponding short three-letter codes.
long_AA = {value: key for key, value in short_AA.items()}
# A dictionary mapping RNA codons to the corresponding amino acids or stop codons.
RNA_codon_table = {
    # Second Base
    # U C A G
    # U
    'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
    'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
    # C
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
    'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
    'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
    # A
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
    'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
    # G
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
    'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
    'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}
# A dictionary similar to RNA_codon_table but with 'U' replaced by 'T' to represent DNA codons.
dnaCodonTable = {key.replace('U', 'T'): value for key, value in RNA_codon_table.items()}


class Converter(str):
    def __init__(self, codons):
        self.codons = codons

    # finding_codons method searches for the provided codon in the dictionaries
    # (short_AA, long_AA, RNA_codon_table, and dnaCodonTable),
    # converts it to uppercase, and prints the result.
    def finding_codons(self):
        find_codons = short_AA.get(self.codons) or long_AA.get(self.codons) or RNA_codon_table.get(
            self.codons) or dnaCodonTable.get(self.codons)
        find_codons = find_codons.upper()
        print("{0} = {1}".format(self.codons, find_codons))


def main():
    ''' Creates an instance of the Converter class with the entered codon.'''
    codons = input('3-letter codon code: ')  # asking for three letter codon code
    codons = codons.upper()  # change input codon to uppercase
    funct_codon = Converter(codons)  # calling class Convector
    funct_codon.finding_codons()


main()
