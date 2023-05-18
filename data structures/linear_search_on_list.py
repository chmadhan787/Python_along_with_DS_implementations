#time complexity of linear search is O(n)
#space complexity is O(1)
#array can be of sorted or unsorted
l = [1,2,3,4,5,6]
target_element = int(input())
i = 0
while i < len(l):
    if l[i] == target_element:
        print("target_element is found at index %d"%(int(l.index(l[i]))))
        break
    i = i + 1
else:
    print("target element is not found.")

