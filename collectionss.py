# collections has methods like Counter,namedtuple,Ordereddict,defaultdict,deque
# Counter contains elements as keys and count as values of dictionary.
from collections import *
a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())#gives all key value pairs
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))#gives 1 most common element
#returns list with tuples in it but if you only want to see the tuple
print(my_counter.most_common(1)[0])
#if only want the element
print(my_counter.most_common(1)[0][0])
print(my_counter.most_common(2))#gives two most common elements
#to get the elements of my_counter
print(list(my_counter.elements()))
#namedtuple is easy to create and light weight object type
point = namedtuple('point','x,y')
#it creates a class named point with fields x and y
pt = point(1,-4)
print(pt)
print(pt.x,pt.y)
#Ordereddict(it remembers the order in wich items where inserted)
ordered_dict = OrderedDict()
# dictionary in newer versions of python can remember order by default hence there
# we dont use ordereddict
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)
#defaultdict (sets a default value for the key if the key value is not given)
d = defaultdict(int)#int is default type of value
print(d['a'])#prints default value of int as a if not given any value
#deque(it is a double ended queue and it is used to add or remove elements
# from both ends)
d1 = deque()
d1.append(1)
d1.append(2)
d1.appendleft(3)
print(d1)
d1.pop()
print(d1)
d1.popleft()
print(d1)
d1.clear()
print(d1)
d1.extend([4,5,6])
print(d1)
d1.extendleft([6,7,8])
print(d1)
d1.rotate(1)#rotates one place to the right
print(d1)
d1.rotate(-1)#rotates all elements one place to the left
print(d1)
print('unpacked deque can be printed as : ',*d1)

