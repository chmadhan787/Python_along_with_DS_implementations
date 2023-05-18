# if True:
#     print("im madhan")
# if False:
#     print("im not madhan")#this will not be printed
# print("bye")

# i= int(input("enter any number : "))
# r=i%2
# if r==0:
#     print("number is even")
#     if i>5:#nested if
#         print('greater than 5')
#     else:
#         print('less than 5')
# else :
#     print("number is odd")
# if r==1:
#     print("number is odd")
#it is not effitient to use more if conditions because it interpreter always
#checks condition so we use else block for false conditions
#using else improves code performance
#wee can also use round bracets as well to mention the condition and it is optional
n=int(input("enter number from 1 to 4 : "))
if n==1:
     print("one")
elif n==2:
     print("two")
elif n==3:
     print('three')
elif n==4:
     print('four')
else :
     print('wrong input')
