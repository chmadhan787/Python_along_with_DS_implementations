#function which returns number of even and odd numbers in the list
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else :
            odd+=1
    return even,odd

lst=[1,2,3,4,5,6,7,8,9]
even,odd = count(lst)

print(even)
print(odd)
#format(parameters...) is a function in the string
print("even : {} , odd : {}".format(even,odd))
#the format function replaces the curly braces with values of parameters passed
print()
#program to print names with letters more than 5
def count1(lst1):
    c1=0
    for i in range(len(lst1)):
        if len(lst1[i])>5:
             c1+=1
    print("number of names with more than 5 letters",c1)
lst1 = []
for i in range(10):
    x=input('enter name : ')
    lst1.append(x)
print(lst1)
count1(lst1)
