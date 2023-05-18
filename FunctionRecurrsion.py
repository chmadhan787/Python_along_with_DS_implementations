#by default function recurrsion is 1000 times limited it doesnt enter into
#infinite loop we can cross this limit by importing sys files
import sys

# we can set the recursion limit using
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
try:
    def greet():
        global i
        i+=1
        print('hello ',i)
        greet()
    greet()
except:
    print("limit exceeded")