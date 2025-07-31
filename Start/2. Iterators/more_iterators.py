# Example file for Advanced Python by Joe Marini

import pprint
# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
_enumerate = enumerate(days)
# iterate through the enumerated values
for i, d in _enumerate:
    #pprint.pp(d, indent=4, width=20,compact=True, underscore_numbers=True)
    print(i, end=f"  -  {d}\n")
# use zip to combine sequences


# use enumerate and zip together


# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
    