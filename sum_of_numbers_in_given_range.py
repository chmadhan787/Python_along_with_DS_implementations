start,stop = map(int,input().split())
print(sum([i for i in range(start,stop+1)]))

print(((stop*(stop+1))//2)-((start*(start+1))//2)+start)

def recursum(num1,num2):
  if num1 > num2:
    return 0
  return num2+ recursum(num1,num2-1)

#or
def recsum(num1,num2):
    if num1>num2:
        return 0
    return num1 + recsum(num1+1,num2)


num1, num2 = start,stop
print(recursum(num1,num2))
print(recsum(num1,num2))

