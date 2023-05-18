n = int(input())
i = 2
def prime_factor(n,i):
    if n%i == 0:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
    if i == n:
        return ''
    return prime_factor(n,i+1)
prime_factor(n,i)