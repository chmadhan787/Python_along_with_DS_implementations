#in this sorting technique we repeatedly find the minimum element from the usorted part and put it a beginning
#this algorithm maintains two sub arrays one is sorted and one is unsorted
# for every iteration the minimum element in the unsorted array is moved in to the sorted array
# selection mostly focuses on the position of the minimum element.
#time complexity is O(n^2)
#Auxiliary space is O(1)

lst = [2,6,5,3,4,1]
for i in range(len(lst)-1):
    min = i
    for j in range(i+1,len(lst)):
        if lst[j]<lst[min]:
            min = j
    lst[i],lst[min]=lst[min],lst[i]
print(lst)