#when we talk about errors generally there are three types of errors
# 1.compile time
#syntactical errors like wrong spelling of keywords ,missing colon etc
# 2.logical error
#getting wrong output
# 3.run time error
#not working for specific input like
#divide by zero(there will be no compile time error,logical error but there will
# runtime error while dividing by zero here basically the mistake will not done
# by the programmer but it will be done by the user)
# we can find the compile time error more easily.
#as a programmer we should also consider that what mistakes a user may do
#we use exceptions because even we give the wrong input our execution should
# not stop. for example
#normal statement : which does give you error in any case
#critical statement : which may give you error in certain conditions

a=4#norm stmnt
b=0#norm stmnt
try:
    print('resource open')
    k = int(input('enter any number : '))
    print(a/b)#critical stmnt
# except Exception:
#     print('hey, you cannot divide a number by zero')
# except Exception as e:#Exception can handle all the exceptions
#     print(e,'Exception')
#except block will be executed only when you have an error
# print('execution will not be stopped in \nbetween so bye will be printed')
# print('bye')
except ZeroDivisionError as e:
    print(e,"exception")
except ValueError as e:
    print(e,'exception')
except Exception as e:
    print(e,'exception')
#whenever we open the resource we should always close the resource
#for this we use finally block
finally:
    print('resource closed')
    #even there is error finally block will be executed