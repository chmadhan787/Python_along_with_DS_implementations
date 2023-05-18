#what kind of problem does a binary tree solve?
#Binary search tree is use to implement set
# #in binary tree every node has atmost two child nodes
# the values of nodes at left sub tree are less the value of root node
# and the values of nodes at right sub tree are greater than the value of root node
# Binary tree doesnt allow duplicates
# Search complexity is O(logn)
# Insertion complexity is also O(logn)
# Complete binary tree : all levels except possibly the last are completely filled and all nodes are
# as left as possible
# Max number of nodes at level i is 2^i
# to search through the binary search tree we have two approaches
# 1. Breadth First Search and 2. Depth First Search
# in Breadth First Search we perform level order traversal of a binary tree.
# in Depth First Search we have Inorder traversal, Preorder traversal and Postorder traversal
# Inorder = (left,root,right)
# Preorder = (root,left,right),(remember we always visit left subtree first)
# Postorder = (left,right,root).


# we can use binary search tree to sort the elements and we can also use Bst to perform set operation ie it
# will remove the duplicate elements

# BFS on a binary tree is a level order on a binary tree.
# and DFS on a binary tree is a pre order traversal on a binary tree.
class Binary_Search_Tree_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            #we add data into the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Search_Tree_Node(data)
        else:
            #we add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_Search_Tree_Node(data)

    def search(self,val):
        if self.data == val:
            return True

        if val<self.data:
            #val might be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val>self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        #visit left subtree first
        if self.left:
            elements += self.left.in_order_traversal()

        #now visit root node or base node
        elements.append(self.data)

        #then visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = Binary_Search_Tree_Node(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17,4,1,20,9,23,18,34]
numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(20))
numbers_tree.delete(23  )
print(numbers_tree.in_order_traversal())