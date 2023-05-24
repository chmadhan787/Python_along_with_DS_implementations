
def merge(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)

    return merging(left,right)

def merging(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:

        if a[i] < b[j]:
            sorted_list.append(a[i])
            i = i+1
        else:
            sorted_list.append(b[j])
            j = j+1

    while i < len_a:
        sorted_list.append(a[i])
        i = i+1
    while j < len_b:
        sorted_list.append(b[j])
        j = j+1

    return sorted_list

elements = [9,3,7,5,6,4,8,2]
print(merge(elements))