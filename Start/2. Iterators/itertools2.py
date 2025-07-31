# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple


# chain() creates a single iterable from multiple
x = itertools.chain(5, [1, "A", True, 10])
print(x)

# make a prepend function
def prepend(val, iterable):
    #print(itertools.chain([val], iterable))
   # print(list(itertools.chain([val], iterable)))
    return itertools.chain([val], iterable)

result = prepend(5, [1, "A", True, 10])
#print(list(result))
# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']
