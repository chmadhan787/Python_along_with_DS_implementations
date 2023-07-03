

# def function(a,b,n,m):
#     max = -9999
#     for i in a:
#         for j in b:
#             if max<abs(i-j):
#                 max = abs(i-j)
#     return max
#
# n = int(input())
# m = int(input())
# a = list(map(int,input().split(' ')))
# b = list(map(int,input().split(' ')))
#
# print(function(a,b))

def MergeStrings(str1,str2):
    str = [i for i in range(len(str1)+len(str2))]
    print(str)
    for i in range(min(len(str1),len(str2))):
        if str1[i]<str2[i]:
            str[i] = str1[i]
            str[len(str)-i-1] = str2[i]
    print(str)

str1 = input()
str2 = input()
MergeStrings(str1,str2)