# the main theme us to use bitwise operators

def add(x,y):
    #lets relate this to full adder in transistor gates concept
    #there we will have sum and carry output for bitwise sum of two binary numbers
    # so from that concept to get carry we do and of binary values of given inputs
    while y!=0:
        # Iterate till there is no carry
        # carry now contains common
        # set bits of x and y
        carry = x&y
        # Sum of bits of x and y where at
        # least one of the bits is not set
        #then we do bitwise xor opertion to find the sum of those binary values
        x = x^y
        # Carry is shifted by one so that
        # adding it to x gives the required sum
        #now we perform bitwise shift on carry and store it in y
        y = carry << 1
        # the value of x before the step when y becomes 0 will be the answer
    return x
print(add(5,4))

# here the main logic is we get carry , do bitwise xor , leftshift carry by 1 till y becomes 0

#we can implement this using recursion
def addrec(a,b):
    xor = a^b
    carry = a&b
    if carry == 0:
        return xor
    else:
        return addrec(xor,carry<<1)
print(addrec(5,4))