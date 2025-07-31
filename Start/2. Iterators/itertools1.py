# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
_iteratorcycle = itertools.cycle(names)
#print(next(_iteratorcycle))

# use count to create a simple counter
_itercount = itertools.count(start=5, step=5)
#print(next(_itercount))

# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
_iteraccumulate = itertools.accumulate(vals)
# iterate through the accumulated values
print(list(_iteraccumulate))
print(list(vals))

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
