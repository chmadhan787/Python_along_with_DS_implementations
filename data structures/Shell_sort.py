#it is optimization over insertion sort
#disadvantage of insertion sort is that there are many comarisions and swaps
#shell sort overcomes these kind of disadvantages
#shell sort uses the concept of gap
#1.start with gap = n/2 and sort sub arrays
#2.keep reducing gap as n/2 and keep in sorting sub arrays
#3.last iteration should have a gap = 1. at this point it is same as insertion sort.
#worst and average case : O(n(logn)^n) and best case is O(nlogn)
#space complexity is O(1)

def shell_sort(elements):
    size = len(elements)
    gap = size//2
    while gap>0:
        for i in range(gap,size):
            anchor = elements[i]
            j = i
            while j>=gap and elements[j-gap]>anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap//=2

elements = [21,38,29,17,4,25,11,32,9]
shell_sort(elements)
print(elements)