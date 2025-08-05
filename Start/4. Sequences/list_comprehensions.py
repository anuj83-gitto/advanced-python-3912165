# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
print(list(map(
  lambda e:e*e,
  filter(lambda e: e>7 and e<15, evens))))

# Derive a new list of numbers frm a given list
_list =[o*o for o in odds if o>3 and o<17]
print(_list)

# Limit the items operated on with a predicate condition
