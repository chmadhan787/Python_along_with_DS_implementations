x=int(input("enter 1st number: "))
print(type(x))
y=int(input("enter 2nd number: "))
a=x+y
print(a)
#input fuction in python always give you string type
#so we need to do type casting when ever we require
#before int if we print type of x then we get str type after typecasting to
#int we get int type
ch = input("enter a character : ")[0]
#print(ch[0])
#input will fetch entire pqr but it will assign only p to ch
print(ch)
result = eval(input("enter an expression : "))#eval function evaluates the
#given expression and gives result
print(result)