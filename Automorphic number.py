
# if units digit of a square of a number is same as the number then it is an
# automorphic number

n = int(input())
l = len(str(n))
sq = n*n
s = sq%(10**l)

print(True if s == n else False)

# in one line
print(True if str(sq)[-l:] == str(n) else False)

print(True if str(sq).endswith(str(n)) else False)