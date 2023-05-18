list1 = []
for i in range(5):
    list1.append([])
    #for i = 0 creates list1 = [[]]
    #for i = 1 creates list1 = [[],[]]
    for j in range(5):
        list1[i].append(j)
        #for i = 0 and j = 0,1,2,3,4
        #list = [[0,1,2,3,4]]

print(list1)

print()
result = []
scorelist = []
for i in range(int(input())):
    name = input()
    score = int(input())
    result.append([name,score])
    scorelist.append(score)
print(sorted(result))
print(scorelist)
b = sorted(list(set(scorelist)))
#in order to sort a set we need to convert it into a list first
#after sorting we can acces them using index values also
print(b[1])
for a,c in sorted(result):
    if c==b[1]:
        print(a)
print(list(x[1] for x in result))

