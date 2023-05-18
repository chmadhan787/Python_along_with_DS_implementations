from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())