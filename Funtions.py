#functoins
#it makes code reusable
#first we define a function and then we call that function
#for example
def greet():#funtion definition
    print('hello')
    print('good morning')
greet()#function call
#after defining function we can call it multiple times
greet()

# print()
# def add(x,y):
#     c=x+y
#     print("sum of num1 and num2 is : ",c)
# p=int(input("enter num1 : "))
# q=int(input('enter num2 : '))
# add(p,q)
print()
#using return keyword
# def add(x,y):
#     c=x+y
#     return 'sum of num1 and num2 is : ',c
# p=int(input("enter num1 : "))
# q=int(input('enter num2 : '))
# result = add(p,q)
# print(result)
# #we can also return multiple values
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
p=int(input("enter num1 : "))
q=int(input('enter num2 : '))
result1,result2 = add_sub(p,q)#as we returning two values we need to accept
#two values
print(result1,"and",result2)
#in future if you want to modify the code you need to change only one
#function
# def romaninteger(self,s: str)->int
#the above line means that the input s must be of str type and the function
#will return the int type