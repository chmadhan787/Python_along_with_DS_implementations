x=12
print(~x)
#we only store positive numbers not negative
#so in order to store negative numbers we need to convert them into positive
#thos can be done using 2's complement
#by calculating we can obsevrve complement of 12 is 2's complement of -13
x= 12&13#performs bitwise and in binary
print(x)
x=12|13
print(x)
#we also have left and right shift operator