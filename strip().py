# Python code to illustrate the working of strip()
string = '   Geeks for Geeks   '
#it will strip the starting and ending spaces when kept blank
# Leading spaces are removed
print(string.strip())

# Geeks is removed since number of spaces matches
print(string.strip('   Geeks'))

# Not removed since the spaces do not match
print(string.strip('Geeks'))