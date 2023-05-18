# priority queue is an abstract data structure where each data or value is assigned with a priority
# for example in airlines ,baggage with the little 'Business' or 'First class' arrive earlier than the rest
# priority queue is extension of queue with the following properties
# An element with higher priority is dequed first than the element with the lower priority
# if two elements have same priority then they are served according to their order in the queue.

class Priority_Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self,data):
        self.queue.append(data)

    def delete(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[max]:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item

MyQueue = Priority_Queue()
MyQueue.insert(7)
MyQueue.insert(1)
MyQueue.insert(14)
MyQueue.insert(2)

print(MyQueue.delete())
print(MyQueue.delete())
print(MyQueue.delete())
print(MyQueue.delete())