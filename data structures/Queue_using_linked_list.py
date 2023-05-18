class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enQueue(self,data):
        node = Node(data)
        if self.rear == None:
            self.front = self.rear = node
        self.rear.next = node
        self.rear = node

    def deQueue(self):
        if self.front == None or self.rear == None:
            print('queue is empty')
        if self.front:
            temp = self.front
            self.front = temp.next
            print(temp.data)

q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()

