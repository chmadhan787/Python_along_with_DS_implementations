# String rjust() and ljust() in python()
# Last Updated : 08 Jan, 2018
# 1. String rjust() The string rjust() method returns a new string of given
# length after substituting a given character in left side of original string
#
# Syntax:
#
# string.rjust(length, fillchar)
#
# Parameters:
#
# length: length of the modified string. If length is less than or equal to
# the length of the original string then original string is returned.
# fillchar: (optional) characters which needs to be padded. If it’s not
# provided, space is taken as a default argument.
#
# Returns:
#
# Returns a new string of given length after substituting a given character
# in left side of original string.
t = 'madhan'
l = 10
print(t.rjust(l))#it adjusts at right
print(t.ljust(l))#it adjusts at list
print(t.rjust(l,'*'))
print(t.ljust(l,'*'))
#
# 2. String ljust()
# The string ljust() method returns a new string of given length after
# substituting a given character in right side of original string.
#
# Syntax:
#
# string.ljust(length, fillchar)
#
# Parameters:
#
# length: length of the modified string. If length is less than or equal to
# the length of the original string then original string is returned.
# fillchar: (optional) characters which needs to be padded. If it’s not
# provided, space is taken as a default argument.
#
# Returns:
#
# Returns a new string of given length after substituting a given character
# in right side of original string.