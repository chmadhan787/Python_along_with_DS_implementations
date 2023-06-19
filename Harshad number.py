# if the number id perfectly divisible by the sum of digits of the number then it
# is a harshad number.

n = int(input())
if n%sum(map(int,list(str(n)))) == 0:
    print('given number is harshad number')
else:
    print('given number is not a harshad number')