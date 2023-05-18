i = 'hi'
string_me = "{0} iam madhan".format(i)#index 0 is optional
#and indexing depends on number of variables in the format
print(string_me)

i = 100
print("{0:b} is binary".format(i))
#{:b} prints the binary value of given number in i
print("{:o} is octal".format(i))
print("{:x} is hexadecimal".format(i))
print("{:d} is decimal".format(i))
print()

#using indexing
i = 10
j = 20
print("{0:b} for i and {1:b} for j".format(i,j))
#here 0 and 1 are index value for variables i and j
print("{1:b} for j and {0:b} for i".format(i,j))
print()

number = int(input("enter any number : "))
width = len("{0:b}".format(number))

for i in range(1, number + 1):
    print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=width))
