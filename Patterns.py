for i in range(4):
    for j in range(4):
        print('m ',end = "")
    print()

print()

for i in range(4):
    for j in range(i+1):
        print("# ",end = "")
    print()

print()

for i in range(4):
    for j in range(4-i):
        print("# ",end = "")
    print()

print()

for i in range(4):
    for j in range(1,5-i):
        print(j," ",end = "")
    print()

print()

for i in range(1,5):
    for j in range(5-i):
        print(i," ",end = "")
    print()

print()

str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])

