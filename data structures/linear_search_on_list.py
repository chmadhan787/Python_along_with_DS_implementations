#time complexity of linear search is O(n)
#space complexity is O(1)
#array can be of sorted or unsorted
l = [1,2,3,4,5,6]
def linear_search_1(l):
    target_element = int(input())
    i = 0
    while i < len(l):
        if l[i] == target_element:
            print("target_element is found at index %d"%(int(l.index(l[i]))))
            break
        i = i + 1
    else:
        print("target element is not found.")
# linear_search_1(l)

def linear_search_2(l):
    target_element = int(input())
    for i,element in enumerate(l):
        if element == target_element:
            print("target element is found at index %d"%(i))
            break
    else:
        print("target element is not found.")
# linear_search_2(l)

def linear_search_3(l):
    target_element = int(input())
    for i in range(len(l)):
        if l[i] == target_element:
            print("target element is found at index {}".format(i))
            print(f"target element is found at index {i}")
            break
    else:
        print("target element is not found.")
# linear_search_3(l)

# using recursion :
def linear_search_4(l,target_element,i=0):
    if l[i] == target_element:
        return i
    return linear_search_4(l,target_element,i+1)
print(linear_search_4(l,3))