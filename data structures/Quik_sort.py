#quick sort follows divide and conquer algorithm
#process of putting pivot in its right position is called partitioning that means that when we
# our pivot in right position it automatically partitions the list in to two
# #there are two famous partitioning schemes 1.hoare partitioning and 2.lomuto partitioning
#average complexity of this algorthm is O(nlogn)
#and the worst case time complexity is O(n^2) ie when the array is already sorted
#space complexity is O(logn)
def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b] = arr[b],arr[a]

def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start += 1

        while elements[end]>pivot:
            end -= 1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)

    return end

def quick_sort(elements,start,end):
    if start<end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)#left partition
        quick_sort(elements,pi+1,end)#right partition

# elements = [11,9,29,7,2,15,28]
elements = [10,16,8,12,15,6,3,9,5]
quick_sort(elements,0,len(elements)-1)
print(elements)

# to reduce the time complexity in this sorting technique we can always choose the middle element as pivot.