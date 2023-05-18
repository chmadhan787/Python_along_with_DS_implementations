# #simple program related to vending machine
# av = 10
# x=int(input('enter no. of candys : '))
# i=1
# while i<=x:
#     if i>av:
#         print('out of stock')
#         break
#     print('candy')
#     i+=1
# print('bye')
#
#
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue#skips values when condition is true
#     print(i)
#
#
# for i in range(1,51):
#     if i%2!=0:
#         pass
#     else:
#         print(i)

for i in range(5):
    if i==3:
        continue
    print('hello',i)

print()

for i in range(5):
    if i==3:
        break
    print('hello',i)

print()

for i in range(5):
    if i==3:
        pass#if we want to keepa block empty then we use pass
    print('hello',i)

def fun():
    pass

class human:
    #if you dont know how use this class then
    pass

#passing(skips) the empty function we can do further tasks
print()
a=5
print(a)

