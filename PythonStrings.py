# Python Strings
#===============
# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print("Hello")
print('Hello')
# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)
# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Note: in the result, the line breaks are inserted at the same position as in the code.
# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Example
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)
# String Length
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
# Use it in an if statement:
# Example
# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Example
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
# Use it in an if statement:
# Example
# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
########################################################################################################################################################################################################################
# Python - Slicing Strings
#=========================
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
# Note: The first character has index 0.
# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Example
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
# Slice To the End
# By leaving out the end index, the range will go to the end:
# Example
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
########################################################################################################################################################################################################################
# Python - Modify Strings
#========================
# Python has a set of built-in methods that you can use on strings.
# Upper Case
# Example
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# Lower Case
# Example
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# Example
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# Replace String
# Example
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# Example
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
########################################################################################################################################################################################################################
# Python - String Concatenation
#==============================
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Example
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
# Example
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
########################################################################################################################################################################################################################
# Python - Format - Strings
#==========================
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# THE ABOVE 3 LINES CODE WILL RETURN ERROR AS WE ARE TRYING TO CONCATENATE str type AND int type, using concatenate operator i.e., "+".

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example
# Use the format() method to insert numbers into strings:
age =32
txt = "My name is PAWAN KALYAN and my age is {}"
print(txt.format(age))
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to buy the item {1} for {2} USD and the quantity I need are {0}."
print(myorder.format(quantity, itemno, price))
########################################################################################################################################################################################################################
# Python - Escape Characters
#===========================
# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# Example
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north."
# print(txt)
# THE ABOVE 2 LINES CODE WILL RETURN ERROR AS WE ARE TRYING TO use " in the middle of the string.

# Example
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# THE ABOVE 2 LINES CODE WILL NOT RETURN ERROR AS WE ARE TRYING TO HANDLE the use of " by using escape character "\" in infront.

# Escape Characters
# Other escape characters used in Python:
#===========
# Code	Result
#===========
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# Examples:
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x38\x65\x6c\x6c\x6f"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\120\145\154\154\157"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#CARRAIGE RETURN 2 Examples for better understanding
# Carriage_return(\r): To take control at starting of same line.
# Carriage return: It's a printer terminology meaning changing the print location to the beginning
txt = "Hello\rWorld!"
print(txt)

txt2 = "stackoverflow\rnine"
print(txt2)

#new line
txt = "Hello\nWorld!"
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = 'It\'s alright.'
print(txt)

# NOTE: The "\f" escape character is to handle "Form Feed" but w3schools did not give example for that.So got the below from stackoverflow.
# form_feed(\f): To take control at starting of next page.
# \f is form feed, its use has become obsolete but it is used for giving indentation like
# stackoverflow
#              tennine
print("stackoverflow\ftennine")
print("stackoverflow\fnine\fgreat")
# stackoverflow
#              tennine
#                     great
########################################################################################################################################################################################################################
# Python - String Methods
#========================
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.

# Python String capitalize() Method
# Example
# Upper case the first letter in this sentence:
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# Syntax
# string.capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
# Example
# The first character is converted to upper case, and the rest are converted to lower case:
txt = "python is FUN!"
x = txt.capitalize()
print (x)
# Example
# See what happens if the first character is a number:
txt = "36 is my age."
x = txt.capitalize()
print (x)

# Python String casefold() Method
# Definition and Usage
# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
# Syntax
# string.casefold()
# Example
# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Python String center() Method
# Definition and Usage
# The center() method will center align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.center(length, character)
# Parameter Values
#   length	--->  Required. The length of the returned string
#   character --->	Optional. The character to fill the missing space on each side. Default is " " (space)
# Example
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)
# Example
# Using the letter "O" as the padding character:
txt = "banana"
x = txt.center(20, "O")
print(x)

# Python String count() Method
# The count() method returns the number of times a specified value appears in the string.
# Syntax
# string.count(value, start, end)
# Parameter Values
# value	--->  Required. A String. The string to value to search for
# start	--->  Optional. An Integer. The position to start the search. Default is 0
# end	--->  Optional. An Integer. The position to end the search. Default is the end of the string
# Example
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
# Example
# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# Python String encode() Method
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# Syntax
# string.encode(encoding=encoding, errors=errors)
# Parameter Values
# encoding	--->  Optional. A String specifying the encoding to use. Default is UTF-8
# errors	--->  Optional. A String specifying the error method. Legal values are:
#     'backslashreplace'	- uses a backslash instead of the character that could not be encoded
#     'ignore'	- ignores the characters that cannot be encoded
#     'namereplace'	- replaces the character with a text explaining the character
#     'strict'	- Default, raises an error on failure
#     'replace'	- replaces the character with a questionmark
#     'xmlcharrefreplace'	- replaces the character with an xml character
# Example
# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)
# Example
# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# Python String endswith() Method
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# Syntax
# string.endswith(value, start, end)
# Parameter Values
# value	--->  Required. The value to check if the string ends with
# start	--->  Optional. An Integer specifying at which position to start the search
# end	--->  Optional. An Integer specifying at which position to end the search
# Example
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# Example
# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
# Example
# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith(",")
print(x)
# Example
# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# Python String expandtabs() Method
# The expandtabs() method sets the tab size to the specified number of whitespaces.
# Syntax
# string.expandtabs(tabsize)
# Parameter Values
# tabsize	---> Optional. A number specifying the tabsize. Default tabsize is 8
# Example
# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(txt)
print(x)
# Example
# See the result using different tab sizes:
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())   #Default tabsize is 8
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# Python String find() Method
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
# Syntax
# string.find(value, start, end)
# Parameter Values
# value ---> Required. The value to search for
# start ---> Optional. Where to start the search. Default is 0
# end   ---> Optional. Where to end the search. Default is to the end of the string
# Example
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
# Example
# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
# Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
# Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))  #---->If this line of code is un-commented then an exception is thrown

# Python String format() Method
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.
# Syntax
# string.format(value1, value2...)
# Parameter Values
# value1, value2...	Required. One or more values that should be formatted and inserted in the string.
#                     The values are either a list of values separated by commas, a key=value list, or a combination of both.
#                     The values can be of any data type.
# The Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
# Example
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# Example
# Using different placeholder values:
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Ram",33)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Bheem",32)
print(txt1)
print(txt2)
print(txt3)
# Formatting Types
# Inside the placeholders you can add a formatting type to format the result:
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
# :c		Converts the value into the corresponding unicode character                                                 # W3SCHOOLS DIDNT GIVE EXAMPLE
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
# :g		General format                                                                                              # W3SCHOOLS DIDNT GIVE EXAMPLE
# :G		General format (using a upper case E for scientific notations)                                              # W3SCHOOLS DIDNT GIVE EXAMPLE
#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
# :n		Number format                                                                                               # W3SCHOOLS DIDNT GIVE EXAMPLE
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))

# format_map()	Formats specified values in a string                                                                    # W3SCHOOLS DIDNT GIVE EXAMPLE

# Python String index() Method
# Definition and Usage
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
# Syntax
# string.index(value, start, end)
# Parameter Values
# value   --->   Required. The value to search for
# start   --->   Optional. Where to start the search. Default is 0
# end     --->   Optional. Where to end the search. Default is to the end of the string
# Example
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
# Example
# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)
# Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)
# Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))    #THIS THROWS EXCEPTION AS EXPLAINED ABOVE. SO COMMENTED.

# Python String isalnum() Method
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.
# Syntax
# string.isalnum()
# Example
# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)
# Example
# Check if all the characters in the text is alphanumeric:
txt = "Company 12"
x = txt.isalnum()
print(x)

# Python String isalpha() Method
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.
# Syntax
# string.isalpha()
# Example
# Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)
# Example
# Check if all the characters in the text is alphabetic:
txt = "Company10"
x = txt.isalpha()
print(x)

# Python String isdecimal() Method
# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
# Syntax
# string.isdecimal()
# Example
# Check if all the characters in the unicode object are decimals:
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
# Example
# Check if all the characters in the unicode are decimals:
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

# Python String isdigit() Method
# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
# Syntax
# string.isdigit()
# Example
# Check if all the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x)
# Example
# Check if all the characters in the text are digits:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

# Python String isidentifier() Method
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# Syntax
# string.isidentifier()
# Example
# Check if the string is a valid identifier:
txt = "Demo"
x = txt.isidentifier()
print(x)
# Example
# Check if the strings are valid identifiers:
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# Python String islower() Method
# The islower() method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
# Syntax
# string.islower()
# Example
# Check if all the characters in the text are in lower case:
txt = "hello world!"
x = txt.islower()
print(x)
# Example
# Check if all the characters in the texts are in lower case:
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print("this is 'Hello world!' " + str(a.islower()))
print("this is 'hello 123' " + str(b.islower()))
print("this is 'mynameisPeter' " + str(c.islower()))

# Python String isnumeric() Method
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
# Syntax
# string.isnumeric()
# Example
# Check if all the characters in the text are numeric:
txt = "565543"
x = txt.isnumeric()
print(x)
# Example
# Check if the characters are numeric:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

# Python String isprintable() Method
# The isprintable() method returns True if all the characters are printable, otherwise False.
# Example of none printable character can be carriage return and line feed.
# Syntax
# string.isprintable()
# Example
# Check if all the characters in the text are printable:
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
# Example
# Check if all the characters in the text are printable:
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

# Python String isspace() Method
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
# Syntax
# string.isspace()
# Example
# Check if all the characters in the text are whitespaces:
txt = "   "
x = txt.isspace()
print(x)
# Example
# Check if all the characters in the text are whitespaces:
txt = "   s   "
x = txt.isspace()
print(x)

# Python String istitle() Method
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.
# Syntax
# string.istitle()
# Example
# Check if each word start with an upper case letter:
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# Example
# Check if each word start with an upper case letter:
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

# Python String isupper() Method
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
# Syntax
# string.isupper()
# Example
# Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
# Example
# Check if all the characters in the texts are in upper case:
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper())

# Python String join() Method
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Parameter Values
# iterable   --->   Required. Any iterable object where all the returned values are strings
# Example
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# Example
# Join all items in a dictionary into a string, using the word "TEST" as separator:
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.

# Python String ljust() Method
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.ljust(length, character)
# Parameter Values
# length   --->   Required. The length of the returned string
# character   --->   Optional. A character to fill the missing space (to the right of the string). Default is " " (space).
# Example
# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
# Note: In the result, there are actually 14 whitespaces to the right of the word banana.
# Example
# Using the letter "O" as the padding character:
txt = "banana"
x = txt.ljust(20, "O")
print(x)

# Python String lower() Method
# The lower() method returns a string where all characters are lower case.
# Symbols and Numbers are ignored.
# Syntax
# string.lower()
# Example
# Lower case the string:
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# Python String lstrip() Method
# The lstrip() method removes any leading characters (space is the default leading character to remove)
# Syntax
# string.lstrip(characters)
# Parameter Values
# characters   --->   Optional. A set of characters to remove as leading characters
# Example
# Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
# Example
# Remove the leading characters:
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

# Python String maketrans() Method
# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
# Syntax
# string.maketrans(x, y, z)
# Parameter Values
# Parameter	Description
# x   --->   Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
# y   --->   Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
# z   --->   Optional. A string describing which characters to remove from the original string.
# Example
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
# Example
# Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
# Example
# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
# Example
# The maketrans() method itself returns a dictionary describing each replacement, in unicode:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))

# Python String partition() Method
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
# Note: This method searches for the first occurrence of the specified string.
# Syntax
# string.partition(value)
# Parameter Values
# value   --->   Required. The string to search for
# Example
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
# Example
# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

# Python String replace() Method
# The replace() method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
# Syntax
# string.replace(oldvalue, newvalue, count)
# Parameter Values
#           oldvalue   --->   Required. The string to search for
#           newvalue   --->   Required. The string to replace the old value with
#           count      --->   Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
# Example
# Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
# Example
# Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
# Example
# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

# Python String rfind() Method
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
# Syntax
# string.rfind(value, start, end)
# Parameter Values
# value   --->   Required. The value to search for
# start   --->   Optional. Where to start the search. Default is 0
# end     --->   Optional. Where to end the search. Default is to the end of the string
# Example
# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
# Example
# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)
# Example
# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)
# Example
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
# print(txt.rindex("q"))    #THIS THROWS EXCEPTION AS EXPLAINED ABOVE. SO COMMENTED.

# Python String rindex() Method
# The rindex() method finds the last occurrence of the specified value.
# The rindex() method raises an exception if the value is not found.
# The rindex() method is almost the same as the rfind() method. See example below.
# Syntax
# string.rindex(value, start, end)
# Parameter Values
# value     --->   Required. The value to search for
# start     --->   Optional. Where to start the search. Default is 0
# end       --->   Optional. Where to end the search. Default is to the end of the string
# Example
# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
# Example
# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)
# Example
# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)
# Example
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
#print(txt.rindex("q"))       #THIS THROWS EXCEPTION AS EXPLAINED ABOVE. SO COMMENTED.

# Python String rjust() Method
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.rjust(length, character)
# Parameter Values
# length       --->   Required. The length of the returned string
# character    --->   Optional. A character to fill the missing space (to the left of the string). Default is " " (space).
# Example
# Return a 20 characters long, right justified version of the word "banana":
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
# Note: In the result, there are actually 14 whitespaces to the left of the word banana.
# Example
# Using the letter "O" as the padding character:
txt = "banana"
x = txt.rjust(20, "O")
print(x)

# Python String rpartition() Method
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
# Syntax
# string.rpartition(value)
# Parameter Values
# value    --->   Required. The string to search for
# Example
# Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
# Example
# If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string:
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

# Python String rsplit() Method
# The rsplit() method splits a string into a list, starting from the right.
# If no "max" is specified, this method will return the same as the split() method.
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# Syntax
# string.rsplit(separator, maxsplit)
# Parameter Values
# separator   --->   Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit    --->   Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
# Example
# Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
# Example
# Split the string into a list with maximum 2 items:
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

# Python String rstrip() Method
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# Syntax
# string.rstrip(characters)
# Parameter Values
# characters   --->   Optional. A set of characters to remove as trailing characters
# Example
# Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
# Example
# Remove the trailing characters if they are commas, s, q, or w:
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

# Python String split() Method
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# Syntax
# string.split(separator, maxsplit)
# Parameter Values
# separator   --->   Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit    --->   Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
# Example
# Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)
# Example
# Split the string, using comma, followed by a space, as a separator:
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
# Example
# Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
# Example
# Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

# Python String splitlines() Method
# The splitlines() method splits a string into a list. The splitting is done at line breaks.
# Syntax
# string.splitlines(keeplinebreaks)
# Parameter Values
# keeplinebreaks   --->   Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False
# Example
# Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
# Example
# Split the string, but keep the line breaks:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

# Python String startswith() Method
# The startswith() method returns True if the string starts with the specified value, otherwise False.
# Syntax
# string.startswith(value, start, end)
# Parameter Values
# value   --->   Required. The value to check if the string starts with
# start   --->   Optional. An Integer specifying at which position to start the search
# end     --->   Optional. An Integer specifying at which position to end the search
# Example
# Check if the string starts with "Hello":
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
# Example
# Check if position 7 to 20 starts with the characters "wel":
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

# Python String strip() Method
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# Syntax
# string.strip(characters)
# Parameter Values
# characters   --->   Optional. A set of characters to remove as leading/trailing characters
# Example
# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
# Example
# Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

# Python String swapcase() Method
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
# Syntax
# string.swapcase()
# Example
# Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# Python String title() Method
# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
# If the word contains a number or a symbol, the first letter after that will be converted to upper case.
# Syntax
# string.title()
# Example
# Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x)
# Example
# Make the first letter in each word upper case:
txt = "Welcome to my 2nd world"
x = txt.title()
print(x)
# Example
# Note that the first letter after a non-alphabet letter is converted into a upper case letter:
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

# Python String translate() Method
# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# Use the maketrans() method to create a mapping table.
# If a character is not specified in the dictionary/table, the character will not be replaced.
# If you use a dictionary, you must use ascii codes instead of characters.
# Syntax
# string.translate(table)
# Parameter Values
# table   --->   Required. Either a dictionary, or a mapping table describing how to perform the replace
# Example
# Replace any "S" characters with a "P" character:
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
# Example
# Use a mapping table to replace "S" with "P":
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
# Example
# Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
# Example
# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
# Example
# The same example as above, but using a dictionary instead of a mapping table:
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

# Python String upper() Method
# The upper() method returns a string where all characters are in upper case.
# Symbols and Numbers are ignored.
# Syntax
# string.upper()
# Example
# Upper case the string:
txt = "Hello my friends"
x = txt.upper()
print(x)

# Python String zfill() Method
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
# Syntax
# string.zfill(len)
# Parameter Values
# len   --->   Required. A number specifying the desired length of the string
# Example
# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)
# Example
# Fill the strings with zeros until they are 10 characters long:
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
########################################################################################################################################################################################################################




