# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)
#############################################################################
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 4         # x is of type int
a = "Sally"   # x is now of type str
print(a)
#############################################################################
# If you want to specify the data type of a variable, this can be done with CASTING.
b = str(3)    # x will be '3'
c = int(3)    # y will be 3
d = float(3)  # z will be 3.0
print(b)
print(c)
print(d)
#############################################################################
# String variables can be declared either by using single or double quotes:
e = "John"
print(e)
#double quotes are the same as single quotes:
e = 'John'
print(e)
#############################################################################
# Variable names are case-sensitive.
f = 4
F = "Sally"
print(f)
print(F)
#############################################################################
# Python - Variable Names
#======================
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
myvar = "John1"
my_var = "John2"
_my_var = "John3"
myVar = "John4"
MYVAR = "John5"
myvar2 = "John6"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "Pawan Kalyan"
print(myVariableName)
# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "Pawan Kalyan2"
print(MyVariableName)
# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "Pawan Kalyan3"
print(my_variable_name)
#####################################################################################################
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection - UNPACKING
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called UNPACKING.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
#####################################################################################################
# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# NOTE: when you try to print like above i.e. print(x, y, z) then space will be automatically entered in the output between words in Python i.e "Python is awesome", unlike Java where it will be "Pythonisawesome".

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is"
z = "awesome"
print(x + y + z)
# NOTE: when you try to print like above i.e. print(x + y + z) then space will NOT be automatically entered in the output between words in Python i.e "Python is awesome", so to demonstrate that I kept a space after "Python ".

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x,y)
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an ERROR:
# x = 5
# y = "John"
# print(x + y)
# ERROR OUTPUT BELOW:
# Traceback (most recent call last):
# File "C:\Users\bhara\IdeaProjects\KBTPython\PythonVariableNames.py", line 89, in <module>
# print(x + y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
a = 5
b = "John"
print(a, b)
#####################################################################################################
# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Example
# Create a variable outside of a function, and use it inside the function

x = "aade PANDUGADU..."

def myfunc():
    print("Evadu kodithe dimma tirigi mind block aypoddo " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# Example
# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

















