queue = []
queue.insert(0,1)
queue.insert(0,2)
queue.insert(0,3)
print(queue)
print(queue.pop())
print(queue.pop())
print(queue.pop())

#if we implement queue using list we face problems associated with dynamic array so we mostly prefer deque to
#implement queue
