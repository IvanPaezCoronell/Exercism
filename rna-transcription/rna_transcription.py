adn = {
       'G': 'C',
       'C': 'G',
       'T': 'A',
       'A': 'U'
       }


def to_rna(dna_strand):
    x = ''.join([adn[i] for i in dna_strand])
    return x
