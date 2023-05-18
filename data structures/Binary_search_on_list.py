#array must be sorted before
#time complexity is O(Logn)
#space complexity is O(1)
l = [1,2,3,4,5,6]
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

