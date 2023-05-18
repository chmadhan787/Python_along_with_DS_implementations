#creating node of a linked list
#you have no need to reallocate the space as compared to arrays
#insertion is easier when compared to arrays
#insertion complexity is O(n)
#always remember that the next of a current node always points to the reference of next node and the value
#always points to the value of the current node
#in linked list the elements are stored at different memory locations
# and then they are linked with pointers
#inserting or deleting at the beginning has acomplexity of O(1)
#inserting or deleting at the end or in the middle has the complexity of O(n)
#linked list traversal has a complexity of O(n)
#accessing element of linked list by value also have a complexity of O(n)

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head == None:
            print("linked list is empty!!!")
            return
        else:
            itr = self.head
            ll = ''
            while itr:
                ll += str(itr.data) + '--->'
                itr = itr.next
            print(ll)

#inserting at the end
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert(self,data_list):
        self.head = None
        for i in data_list:
            l1.insert_at_end(i)

    #method to get length of the linked list
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

    #method to remove linked list at specified index
    def remove_at(self,index):
        if index<0 or index>=l1.get_length():
            raise Exception("invalid input.")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return

    #method to insert a node at specified position
    def insert_at(self,index,data):
        if index<0 or index>l1.get_length():
            raise Exception("index invalid")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1 :
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def reversing_by_changing_links(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

l1 = LinkedList()
# l1.insert_at_beginning(5)
# l1.insert_at_beginning(89)
# l1.insert_at_end(79)
# l1.insert_at_end(987)
# l1.insert_at_end(98)
# l1.insert(['banana','apple','mango'])
l1.insert([1,2,3,4,5,6])
l1.print()

print("length of my linked list is :",l1.get_length())

l1.remove_at(2)

l1.print()

# l1.insert_at(0,'figs')
l1.insert_at(0,0)
# l1.insert_at(2,'jackfruit')
l1.insert_at(2,7)
l1.print()
l1.reversing_by_changing_links()
l1.print()