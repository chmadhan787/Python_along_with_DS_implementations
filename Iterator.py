nums = [2,3,4,5,6]
it = iter(nums)#iter is an iterator which converts nums into an iterator
print(it.__next__())#this gives the first value of nums
# when we use iterator it will preserve the last value of the list and by using
# next function we can access the values one by one
print(it.__next__())
print(it.__next__())
#we can also use next function in other way like
print(next(it))#it also prints the next value of list

print()
for i in nums:
    print(i)
print()

#to create our own iterator let us use class and object concept
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):#it returns the object of itertor
        return self
    def __next__(self):#next will give the next object
        if self.num <= 10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values = TopTen()

# print(values.__next__())
print(next(values))
#since we next function it will print 1 and points towards two
#then starts printing from 2 in the for loop
for i in values:
    print(i)
