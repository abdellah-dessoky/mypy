#operators 
"""
- arithmatic operators in addition to floored division '//' and Exponentiation 
- logical operators and,not, and or (&&,!,and ||)
- comparison operators (==,<=,>=,<,>,and !=)
- assignment operators (= ,+= ,-= ,*=,/=,//= ,%=,and **=)
- Membership operators (in and not in)
- identity operator (is and is not) 
- 
"""
#"""
#casting using default methods in python
name = str(123)           # converts int to string 
age = int("18")           # converts string to int 
height = float("1.73")    # converts string to floar 
passed = bool(1)        # converts int to boolean
failed = bool(0)
subjects_failed = bool("")  #converts string to boolean which is false
#there are other conversion methods for lists and tuples as well as dicts
#"""
#boolean casting details
bool(0)   # => False
bool(2)   # => True
bool(0 and 2)   # => 0
bool(0 or 2)   # => 2
bool(-5)  # => True
bool(2)   # => True
bool(int("5"))  #=> True
# Chaining 
1 < 2 < 3  # => True
2 < 3 < 2  # => False
#"""
# opertions done on boolean variables
variable = True
newVariable = variable+10
print("The value of adding 10 to True ")
print(newVariable)
false = False 
newFalse = false*5
print("The value of multiplying false by 5 :")
print(newFalse)
#"""
# find the length of a string
len("This is a string")  # => 16
#  f-strings or formatted string literals.
name = "mac"
f"hello {name}!"
# Any valid Python expression inside these braces is returned to the string.
f"{name} is {len(name)} characters long."  
#"""
# None is an object
None  # => None
#"""