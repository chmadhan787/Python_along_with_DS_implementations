l = list(map(int,input('Enter any array').split(' ')))

subarrays = []

for i in range(len(l)):
    for j in range(i+1,len(l)+1):
            subarrays.append(sum(l[i:j]))

print(sum(subarrays))
#output
# Enter any array1 2 3 4 5
# sub arrays = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [3], [3, 4], [3, 4, 5], [4], [4, 5], [5]]
# sub arrays sums = [1, 3, 6, 10, 15, 2, 5, 9, 14, 3, 7, 12, 4, 9, 5]
# sum of sums of subarrays = 105