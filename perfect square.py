import math

# if the square root of a number is an integer rather than a decimal then that
# number is a perfect square.
n = int(input())

def perfect_sq(n):
    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        print(f'{n} is perfect square')
    else :
        print(f'{n} is not a perfect square')

perfect_sq(n)


def perfect_sqr(n):
    sr = math.sqrt(n)
    if sr*sr == n:
        print(f'{n} is perfect square')
    else :
        print(f'{n} is not a perfect square')

perfect_sqr(n)