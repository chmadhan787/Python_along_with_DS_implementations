#time complexity :
#average and worst case = O(n^2) and best case O(n)
#space complexity is O(n)
def bubble_sort(number_list):
    for j in range(len(number_list)-1):
        swapped = False
        for i in range(len(number_list)-1):
            if number_list[i]>number_list[i+1]:
                number_list[i],number_list[i+1]=number_list[i+1],number_list[i]
                swapped = True
        if not swapped:#this increases efficiency if the given array is presorted
            break
    return number_list

number_list = [1,8,6,7,5,4,2,3]
print(bubble_sort(number_list))

#this code is not so efficient , it had a couple of inefficiences to make it efficient we can replace
#len((number_list)-1 with len(number_list)-1-i ,so from the second iteration we no need to traverse the array
#till the last element
#we can use the sorting algorithm for the strings too ,scince we can use the comparision operators on the strings
#as bubble sort uses the most power of cpu we go with selection sort