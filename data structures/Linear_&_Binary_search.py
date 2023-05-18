#Linear search is also called sequential search and Binary search is also called half-interval search
#time complexity for linear search is O(n) and for binary search is O(logn)
#multi dimensional array can be used for linear search and single dimensional array for binary search
#Linear search performs quality comparisions and Binary search performs ordering comparisions
#linear search is less complex compared to Binary search
#it is very slow process and Binary search is a very fast process.
#to check every element in the array the time could be big O(n) for linear search if the number is really
# very big or in worst case
#an algorithm is a high level description or trick used to solve a problem
#both searching mechanisms has a space complexity of O(1)

#using Linear search:
def linear_search(number_list,number_to_find):
    for i,element in enumerate(number_list):
        if element == number_to_find:
            return i
    return -1

#using binary search:
def binary_search(number_list,number_to_find):
    low,high = 0,len(number_list)-1
    while low<=high:
        mid_index = (low+high)//2
        mid_number = number_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        elif mid_number<number_to_find:
            low = mid_index+1
        else:
            high = mid_index-1
    return -1

#binary search using recursion:
def bin_rec(number_list,number_to_find,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if mid>=len(number_list) or mid<0:
        return -1
    mid_num = number_list[mid]
    if mid_num == number_to_find:
        return mid
    elif mid_num<number_to_find:
        low = mid+1
    else:
        high = mid-1
    return bin_rec(number_list,number_to_find,low,high)

number_list = [12,15,19,21,24,25,67]
number_to_find = 21
print(linear_search(number_list,number_to_find),' using linear search')
print(binary_search(number_list,number_to_find),' using binary search')
print(bin_rec(number_list,number_to_find,0,len(number_list)),' using binary search recursion')