# Python split() method splits the string into a comma separated list. It separates string based on the separator delimiter. This method takes two parameters and both are optional. It is described below.
#
# Signature
# split(sep=None, maxsplit=-1)
# Parameters
# sep: A string parameter acts as a seperator.
#
# maxsplit: Number of times split perfome.
#
# Return
# It returns a comma separated list.

# Variable declaration
str = "Java is a programming language"
# Calling function
str2 = str.split()
# Displaying result
print(str2)

str2 = str.split('a')
print(str2)

str2 = str.split('a', 1)
print(str2)
str2 = str.split('a', 3)
print(str2)