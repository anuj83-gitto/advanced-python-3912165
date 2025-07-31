# Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
def findname(target):
    for name in names:
        if name == target:
            print("Name found");
            return True
    
    print("Name not found")
    return False

print(findname("Creed"))
print(findname("Tom"))

# Check if a number is prime
def isprime(n):
    if n < 2:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not prime")
            return False
    print(f"{n} is prime")
    return True

print(isprime(7))
print(isprime(10))
print(isprime(13))