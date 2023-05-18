arr =map(int,input().split())
#int is a function in map and input().split() is an iterable
#split() function splits the input according to spaces by using commas inbetween
print(sorted(list(set(arr))))