#for all cases time complexitity is O(nlogn)
#space complexity is O(n)
def merge_sort(arr):
    len_arr = len(arr)
    if len_arr<=1:
        return
    mid = len_arr//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i=j=k = 0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k] = b[j]
        j+=1
        k+=1

arr = [10,3,15,7,8,29,98,23]
merge_sort(arr)
print(arr)
#in order to use space optimally we shall stop returning and creating new lists
#Tim sort is a hybrid algorithm which uses merge sort and insertion sort