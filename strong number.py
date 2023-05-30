# a number is called as strong number if the sum of the factorials of each digit in
# number is equal to the original number.
# for example 145 = 1! + 4! + 5!

def find_fact(n):
    if n == 1:
        return 1
    return n*find_fact(n-1)


def strong_number_test(num, strong = 0):
    if num == 0:
        return strong
    strong = strong + find_fact(num % 10)
    return strong_number_test(num//10,strong)

test = int(input())
print(strong_number_test(test)==test)
