#stack are also list based data structures and a stack ie like a stack of objects in real life
#stacks are very useful when you only care about the most recent elements
# terminology
#push - means adding elements to stack
#pop - means removing elements form the stack
#for both operations time complexity is O(1)
#we can use linked list to implement stack and to keep track of front of single linked list (top of stack) and
# it works in last in first out manner ie LIFO
class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head = None):
        self.head = head

    # def append(self,new_element):
    #     current = self.head
    #     if self.head:
    #         while current.next:
    #             current = current.next
    #         current.next = new_element
    #     else:
    #         self.head = new_element

    #insert new element as head of linked list
    def insert_first(self,new_element):
        new_element.next = self.head
        self.head = new_element

    #delete first (head)element in the linked list and return it
    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else :
            return None

class Stack(object):
     def __init__(self,top = None):
         self.l1 = LinkedList(top)

     #push(add) new element on to top of stack
     def push(self,new_element):
         self.l1.insert_first(new_element)

    # pop the first element off the top of stack
     def pop(self):
         return self.l1.delete_first()

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

stack = Stack(e1)

stack.push(e2)
stack.push(e3)

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())

stack.push(e4)

print(stack.pop().value)