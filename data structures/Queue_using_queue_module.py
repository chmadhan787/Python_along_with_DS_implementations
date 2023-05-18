from queue import Queue

q = Queue(maxsize=3)
print(q.qsize())

q.put(1)
q.put(2)
q.put(3)
print(q.full())
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())

print(q.empty())
