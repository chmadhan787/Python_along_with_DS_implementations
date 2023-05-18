#There are three steps for recursion
#1.divide bigger problem into smaller and simpler problem
#2.find the base condition with the simple answer
#3.return base condition answer to solve all the problems

def find_sum(num):
    if num == 1:
        return 1
    return num+find_sum(num-1)

num = int(input())
print(find_sum(num))

def fibb(num):
    if num == 0 or num==1:
        return num
    return fibb(num-1)+fibb(num-2)

print(fibb(num))

#becuse of recursion the code looks simple
