from collections import deque
#stack using deque is efficient when compared to stack using list because
# the append and pop time complexities for
#deque are O(1) where as they are O(n) for list
# stack = deque()
# # print(dir(deque))
# stack.append('www.cnn.com')
# stack.append('www.cnn.com/world')
# stack.append('www.cnn.com/india')
# stack.append('www.cnn.com/china')
# print(stack.pop())
# print(stack.pop())

#implementing stack using deque and oops concept
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
print(s.peek())
s.push(6)
s.push(7)
s.push(8)
s.peek()
