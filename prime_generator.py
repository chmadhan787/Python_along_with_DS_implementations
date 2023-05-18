def prime_gen(end):
    for i in range(2,end):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
                yield i

print(list(prime_gen(10)))
