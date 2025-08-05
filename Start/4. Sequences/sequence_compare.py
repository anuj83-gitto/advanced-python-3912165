# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 6, 10, 15, 34, 56, 67]
seq2 = [1, 2, 5, 7, 9, 18, 22, 38, 91]
print(seq1<seq2)
print(seq1>seq2)
# define a tuple
seq3 = (1, 2, 3, 6, 10, 15, 34, 56)
seq7 = (1, 2, 5, 7, 9, 18, 22, 38)

print(seq3==seq7) 
# compare the sequences


# sequences that have equal values but different number of items:
seq4 = [10, 20, 30]
seq5 = [10, 20, 30, 40, 50]


# Sequences must be of the same type to be compared


# use the all() function to compare two arbitrary sequences
print(all(x>=y for x,y in itertools.zip_longest(seq1, seq2, fillvalue=0)))