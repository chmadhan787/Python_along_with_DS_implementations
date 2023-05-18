#this concept is very similar to addition and we can implement it by
#just replacing the x with negation of x as
#in this check that the x value is greater than the y value else it will
#enter into infinite loop
def sub(x,y):
    while y!=0:
        borrow = (~x)&y
        x = x^y
        y = borrow<<1
    return x
print(sub(8,5))


#in recursion also make sure that the value of a is greater than the value of b
def subrec(a,b):
    xor = a^b
    borrow = (~a)&b
    if borrow == 0:
        return xor
    else:
        return subrec(xor,borrow<<1)
print(subrec(6,3))

# in order to overcome that infinite loop we dont need to extra code , when that condition occur we
# we just swap a and b then we compute the result