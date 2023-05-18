i=int(input('enter any number'))
c=0
for k in range(2,i):
    if i%k==0:
        print('given number is not prime')
        break
else:
        print('given number is a prime')