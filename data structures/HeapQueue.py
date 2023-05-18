#heapq module in python provides a heap data structure that is mainly used to represent a priority
#queue in data structure. the prperty of this data structure in python is that each time the smallest
#heap element is popped(min - heap). whenever the elements are pushed or popped , heap structure is maintained
# the heap[0] element also return the smallest element each time
# it supports the extraction and insertion of smallest element in O(logn) times

import heapq

li = [5,7,9,1,3]

heapq.heapify(li)

print(list(li))

heapq.heappush(li,4)
print(list(li))

print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
