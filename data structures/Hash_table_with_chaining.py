#handling collision in hashtable using chaining
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]#we initialize every element with empty list instead of None

    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX
#scince python already have inbuilt functions for add and get as __setitem__() and __getitem__() respectively

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found :
            self.arr[h].append((key,value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]



t = HashTable()
t['march 6'] = 130
t['march 1'] = 30
t['march 10'] = 556
t['dec 4'] = 45
t['march 17'] = 467
print(t['march 6'])
print(t['march 17'])
del t['march 17']
print(t.arr)