# first,*rest = input().split()
# print(first)
# print(rest)

# one,two,*then = range(5)
# print(one)
# print(two)
# print(then)

# start,*middle,end = range(7)
# print(start)
# print(middle)
# print(end)
#access is done with respect to index values and indexes are according to spaces

students_marks = {}#this a dictionary
for i in range(int(input())):
    name,*line = input().split()

    scores = list(map(float,line))

    students_marks[name] = scores#we can assign keys and values to a dictionary
    #using this statement
print(name)
print(line)
print()
print(scores)
print()
print(students_marks)

query_name = input()
for i in students_marks:
    if i==query_name:
        sum = 0
        #for j in students_marks.get(query_name):
        for j in students_marks[i]:
        #for j in students_marks[query_name]:
            sum = sum + j
print("{:.2f}".format(sum/3))

#to get result in two decimal places
# fnum = 7.154327
#
# res = "{:.2f}".format(fnum)
#
# print(res)
