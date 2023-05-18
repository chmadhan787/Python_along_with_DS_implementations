print(10*'m')
print('madhan\'s "laptop"')#slash makes ignore special meaning of '
print(r"c:user\me\name")#raw string
name = 'madhan'#name will be converted to array with index values starting from 0
print(name)
print(name[0])
print(name[-1])#strinf array will be numbered from -1 in reverse order indexing
print(name[0:4])#for printing a range of characters used in string 4 is not included
print(name[1:])#starts from mentioned and prints till end
print(name[:4])#starts from first and ends at mentioned
print(name[3:10])# ends at last one available
#string in python is immutable
r=len(name)
print(r)
print(name[::-1])