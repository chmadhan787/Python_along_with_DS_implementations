#for all cases time complexitity is O(nlogn)
#space complexity is O(n)
# if we merge only two lists then it is called two-way merging
# similarly for 3 lists it's called three-way merging
# for 4 lists called four-way merging( n lists -> n-way merging )
# difference between merge sort and two-way merge sort is that two way merge sort is the iterative process/ repeating
# procedure but merge sort is a recursive procedure.

# this is with using the temporary array :
def merge_sort(arr):
    len_arr = len(arr)

    if len_arr <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two(left,right)


def merge_two(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
        k += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
        k += 1
    while j < len_a:
        sorted_list.append(b[j])
        j += 1
        k += 1
    return sorted_list

print(merge_sort([10,3,15,7,8,29,98,23]))

# this is without using temporary array :
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

# pros of merge sort :
# 1. large size lists can be sorted easily
# 2. suitable for linked list
# 3. merging supports external sorting
# 4. merge sort is stable ( if i have a list with duplicates then the order of
#                           duplicates is maintained )
#
# cons of merge sort :
# 1. Extra space ( not in place sort )
# 2. no small problem
# 3. if size of list is very small then merge sort will waste lot of time in
#       recursion and becomes slower compared to insertion sort .