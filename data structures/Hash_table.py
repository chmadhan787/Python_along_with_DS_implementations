#implementing hash table or hash map
#Dictionary in python is implementation of hashmap
#writing hash function
# def get_hash(key):
#     h = 0
#     for char in key:
#         h+=ord(char)
#     return h%100 #assuming size of list as 100
# print(get_hash('march 9'))

#implementing hashtable:
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]#initializing 100 elements of array with None

    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    # def add(self,key,val):
    #     h = self.get_hash(key)
    #     self.arr[h]=val
    #
    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    #since python already have inbuilt functions for add and get as __setitem__() and __getitem__() respectively
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h]=value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
print(t.get_hash('march 6'))
# t.add('march 6',130)
# print(t.get('march 6'))
t['march 6'] = 130
t['march 1'] = 20
t['dec 17'] = 30
print(t['march 1'])
print(t.arr)
del t['march 1']
print(t.arr)

