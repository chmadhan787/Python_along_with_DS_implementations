def binary_search(lst,n,l,u):
    if n in lst:
        m = (l+u)//2
        if lst[m]==n:
            return True
        else:
            if n>lst[m]:
                return binary_search(lst,n,m+1,u)
            else:
                return binary_search(lst,n,m-1,u)

lst = [1,2,3,4,5,6,7]
l = 0
u = len(lst)-1
n = int(input())
if binary_search(lst,n,l,u):
    print("target is found at index {}".format(lst.index(n)))
else:
    print("target is not found in the list.")