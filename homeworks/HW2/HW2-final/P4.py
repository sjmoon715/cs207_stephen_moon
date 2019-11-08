import sys

def dna_complement(sequence):
    sequence = sequence.upper()
    valid_bases = ['A','T','C','G']
    complement_bases = {'A':'T','T':'A','C':'G','G':'C'}
    seq_list = list(sequence)
    
    for i in range(len(seq_list)):       
        if seq_list[i] not in valid_bases:
            return None         
    else:
        for i in range(len(sequence)):
            seq_list[i] = complement_bases[seq_list[i]]
        new_sequence = "".join(seq_list)
        return new_sequence

test_sequence = 'ACTTGCAGT'
print("Example Sequence: {}".format(test_sequence))
test_complement = dna_complement(test_sequence)
print("Complement: {} \n".format(test_complement))

lower_sequence = 'aggttac'
print("Example Lower Case Sequence: {}".format(lower_sequence))
lower_complement = dna_complement(lower_sequence)
print("Complement: {} \n".format(lower_complement))

invalid_sequence = 'atgewafy'
print("Example Invalid Sequence: {}".format(invalid_sequence))
invalid_complement = dna_complement(invalid_sequence)
print("Complement: {}".format(invalid_complement))



