#array must be sorted before
#time complexity is O(Logn)
#space complexity is O(1)
l = [1,2,3,4,5,6]

def binary_search_1(l):
    n = int(input())
    i = 0
    low = 0
    up = len(l)-1
    if n in l:
        while low<=up:
            mid = (low+up)//2
            if l[mid] == n:
                print("target is found at index {}".format(l.index(n)))
                break
            else:
                if n>l[mid]:
                    low = mid + 1
                else:
                    up = mid - 1
    else:
        print("target is not in the list.")
# binary_search_1(l)


# this is the most efficient way
def binary_search_2(l):
    search_element = int(input())
    left = 0
    right = len(l)-1
    while left <= right:
        mid = (left+right)//2

        if search_element < l[mid]:
            right = mid - 1

        elif search_element > l[mid]:
            left = mid + 1

        elif search_element == l[mid]:
            return mid

    return -1
# print(binary_search_2(l))

# using recursion
def binary_search_3(l,left,right,target):
    mid = (left+right)//2
    if target == l[mid]:
        return mid

    if target < l[mid]:
        return binary_search_3(l,left,mid - 1,target)
    if target > l[mid]:
        return binary_search_3(l,mid + 1,right,target)

    return -1
target = int(input())
print(binary_search_3(l, 0, len(l)-1,target))
