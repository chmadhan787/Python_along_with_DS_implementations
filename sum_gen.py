def sum_gen(end):
    for i in range(end):
        yield i

print(sum(list(sum_gen(10))))