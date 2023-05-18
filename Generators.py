#generator will give you iterator
# generators are simple and powerful tool to create iterators.
def topten1():
    #since we use yield this function is not just a function but it is a generator
    yield 1#we can use multiple yields
    yield 2
    yield 3
    yield 4
    yield 5
    #hence by using generator we can create iterator without using iter fnction
     #yield is a special keyword which makes your function as a generator

values = topten1()
print(values)#prints generator object
#in order to fetch values from iterator we need to use next function
print()
print(values.__next__())
print(values.__next__())
#yield is same as return but return will terminate the function but yield wont
for i in values:
    print(i)
print()
def topten():
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

values1 = topten()

for i in values1:
    print(i)

#application
#lets say we need to fetch 1000 records from the database we need to load
#those 1000 files into the memory but we need to check records one at time
#for that we use generator concept to fetch one record at a time

def reverse(data):
    for i in range(len(data)-1,-1,-1):
        yield data[i]
print(list(reverse('golf')))
print(type(reverse('golf'))) # the generator returns a generator object
for char in reverse('golf'):
    print(char)
