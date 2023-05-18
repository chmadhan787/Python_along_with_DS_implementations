def print_formatted(number):
    binlen = bin(number)
    print(binlen, type(binlen))
    binlen = str(bin(number))
    print(binlen, type(binlen))
    binlen = len(bin(number))
    print(binlen)
    for i in range(1,number+1):

        binary = bin(i).split('b')
        hexa = hex(i).split('x')
        octal = oct(i).split('o')
        print(i,octal[1],hexa[1],binary[1])

    for i in range(1,number+1):

        print(str(i).rjust(binlen,' '),end='')
        print(str(oct(i)[2:]).rjust(binlen,' '),end='')
        print(str(hex(i)[2:]).rjust(binlen, ' '), end='')
        print(str(bin(i)[2:]).rjust(binlen, ' '))

    for i in range(1,number+1):

        print(str(i).ljust(binlen,' '),end='')
        print(str(oct(i)[2:]).ljust(binlen,' '),end='')
        print(str(hex(i)[2:]).ljust(binlen, ' '), end='')
        print(str(bin(i)[2:]).ljust(binlen, ' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)