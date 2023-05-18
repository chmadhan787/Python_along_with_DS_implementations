#str() function returns string function of object
n = str('madhan')
print(n)
print(type(n))

#Signature
# str(object, encoding=encoding, errors=errors)

# Parameters
# object: It is the encoding of the object.The default value is UTF - 8.
#
# encoding: It is the encoding of the object.The default value is UTF - 8.
#
# errors: It specifies the actions that need to be performed if the
# decoding fails.

#String center() method
# Python center() method alligns string to the center by filling paddings left
# and right of the string. This method takes two parameters, first is a width
# and second is a fillchar which is optional. The fillchar is a character
# which is used to fill left and right padding of the string.
#
# Signature
# center(width[,fillchar])
# Parameters
# width (required)
# fillchar (optional)
# Return Type
# It returns modified string.
print()
str1 = 'hello'
str2 = str1.center(20,'-')
#or
print(str('hello').center(20,'-'))
print()
print(str1)
print()
print(str2)
print()
print(str('hello'*2).center(20,'-'))