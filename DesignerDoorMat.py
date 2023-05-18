# n,m = map(int,input().split())
# if n%2!=0:
#     for i in range(n+1):
#         for j in range(m+1):
#             if j==m//2:
#                 print('|', end='')
#                 continue
#             print('-',end='')
#         print()
# else:
#     print('enter odd number but not even')
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))