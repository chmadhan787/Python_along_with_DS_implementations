#return type of raw_input is always a string but
# return type of input need not be a string always
# in python 2.x input function will itself convert the input to corresponding type
# but in python 3.x every input from the user is considered as string only
# and we need to convert that input into corresponding type
# in python 2.x if we use raw input there will be a use
# since raw input only takes in the form of string and input takes in corresponding type
# but in python 3.x both input and raw_input are similar i.e both takes input in
# string form only.
t = tuple(map(int,input().split()))
print(t)
