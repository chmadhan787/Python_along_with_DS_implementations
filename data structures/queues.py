#queue is a first in first out structure
#FIFO
#first element is called as head and last element is called as tail
#if you add element to the tail it is called enqueue
#and if you remove element from the head then it is called dequeue
#there is also an operation called peek ,where you look at the head element but we dont actually remove it
#again we can implement the queue data structure with a Linkedlist , where you also save references to head and
# tail so you can loop them both up in constant time. we have two popular types of queues
#1. DEQUES : this is a double ended queue ,in this we can enqueue or dequeue from either end,deque is a generalised
#version of both stacks and queues (ie we can treat it like stack where we can add and remove elements from the
# same end or you can treat it like a queue in which we can add elements at one end and remove at other end)
#PRIORITY QUEUE: in a priority queue we assign each element a numerical priority when you insert it into a queue
#when you dequeue you remove the element with highest priority,this doesnt really follow the rules of a normal
#queue, where you remove the oldest element first, howevr if the element have same priority then the oldest element
#is the one they dequeue first.

wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)
print(wmt_stock_price_queue)
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())
#as we can implement queue with list ,we get problems associated with the dynamic array so to overcome this we use
#collections module to implement queue
from collections import deque
q = deque()
q.appendleft(131.10)
q.appendleft(132.12)
q.appendleft(135)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())

#implementing queue class using python
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enque(self,val):
        self.buffer.appendleft(val)
    def deque(self):
        self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer) == 0

pq = Queue()
pq.enque({'company':'Wall Mart','timestamp':'15 April,11:01 AM','price':131.10})
pq.enque({'company':'Wall Mart','timestamp':'15 April,11:02 AM','price':132.12})
pq.enque({'company':'Wall Mart','timestamp':'15 April,11:03 AM','price':135})
print(pq.buffer)
print(pq.deque())