nums = [11,44,34,76,36,57]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print('not found')#this else connected with for loop
    #if the desired element is not found in sequence then the else block will
    #be executed