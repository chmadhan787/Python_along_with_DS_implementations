from queue import LifoQueue
stack = LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('g')
stack.put('f')
stack.put('g')
print(stack.full())#true if number of elements reaches the maxsize
print(stack.qsize())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.empty())#true if number of elements = 0
