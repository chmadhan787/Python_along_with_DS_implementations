start,stop = map(int,input().split())

#iteratinf inner loop as (2,number-1)
f=1
if start>=stop:
    print('Please enter valid range')

for i in range(start,stop):
    for j in range(2,i-1):
        if i%j==0:
            f=0
    if f:
        print(i,end=' ')
    f = 1
print()
#iterating through (2,number/2)
f=1
if start>=stop:
    print('Please enter valid range')

for i in range(start,stop):
    for j in range(2,int((i)/2)+1):
        if i%j==0:
            f=0
    if f:
        print(i,end=' ')
    f = 1
print()
#iterating through (2,sqrt(number))
from math import sqrt
f=1
if start>=stop:
    print('Please enter valid range')

for i in range(start,stop):
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            f=0
    if f:
        print(i,end=' ')
    f = 1
print()
#iterating through odd number only
f=1
if start>=stop:
    print('Please enter valid range')

for i in range(start,stop):
    for j in range(3,int(sqrt(i)),2):
        if i%j==0:
            f=0
    if (i%2 == 0 or i%3==0) and i>3:
        f=0
    if f:
        print(i,end=' ')
    f = 1