stack = []

#for push operation we use the append operation of list as
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

# for pop operation we can use the pop method of list but without arguments
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# problem with using list as stack is that the list is a dynamic array, so if the
# memory is not sufficient to insert the upcoming elements then the list will go
# any other memory location and assigns additional double amount of spaces than
# present one. so using list for creating stack is not memory efficient
