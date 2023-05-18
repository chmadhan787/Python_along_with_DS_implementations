#worst case : O(n^2) comparisons and swaps
#best case : O(n) comparisons and O(1) swaps
#average case : O(n^2) comparisons and swaps
#worst case space complexity : O(n) total, O(1) auxiliary
#when the list is very big it is not efficient because we always swap the elements when they are not in order
# in this sorting technique we insert one element at a time in its correct position
def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j-=1
        elements[j+1] = anchor

elements = [21,38,29,17,4,25,11,32,9]
insertion_sort(elements)
print(elements)