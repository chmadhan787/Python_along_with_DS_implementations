#it is the simplest algorithmthat works by repeated swapping of adjacent elements if they are in the wrong order
# this algorithm is not suitable for large data sets because its average ang worst time complexities are high.
#time complexity is O(n^2) for worst and average case and O(n) for best case
#auxiliary space is O(1)
#can be optimised by stopping the algorithm if inner loop didnt cause any swap
lst = [2,4,3,1]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)
