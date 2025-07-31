# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope


# define a local function with a variable "x"


# Run the test function and observe the two results


# Nested functions create inner scopes. These are called closures:
def outer(_istring):
    _ostring = _istring + " "
    
    # inner function that modifies the outer variable
    def inner(_istring2):
      _ostring = _istring + _istring2
      return _ostring
    return inner

obj1 = outer("Hello")
print(obj1)
print(obj1("Python"))