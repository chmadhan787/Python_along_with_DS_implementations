# # #if we import this module in other module then __name__ will print
# # # the module name
# # print("hello ",__name__)
# import  SpecialVariable__name__
# print("its time to claculate")
# #if i run demo_name then SpecialVariable__name__ becomes a seperate module
# #for me
# #we can see while running this code the function available in SpecialVariable
# # __name__ module is not called
#
def add():
    print("result 1 is",__name__)
    #here the name prints __main__

def sub():
    print("result 2 is")

def main():
    print("in demo_name main")
    add()
    sub()
if __name__ == "__main__":
    main()

