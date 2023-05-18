
class Binary_search_tree :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_search_tree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_search_tree(data)

    def i_o_t(self):
        elements = []
        if self.left :
            elements += self.left.i_o_t()

        elements.append(self.data)

        if self.right :
            elements += self.right.i_o_t()
        return elements

def build_tree(elements = [17,4,1,20,9,23,18,34]):
    root = Binary_search_tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
root = build_tree()

print(root.i_o_t())