# # import demo_name
# #
# # print('demo_name says : ',__name__)
# # #as we know from java main is the starting point of the program
# # #the first module name is always main and that is where your code starts
# def main():
#     print("hello")
#     print("welcome user")
#
# # if want to call main() only when this program is executed but not while executing
# # program in which this program imported as another file
# #for acheiving this we can use __name__=="__main__" like
# if __name__ == "__main__":
#     main()
#
from demo_name import add
def fun1():
    add()#here the __name__ prints module name
    print("from fun1")

def fun2():
    print("from fun2")

def main():

    fun1()
    fun2()

main()

# conclusion:
 # when we use if __name__=="__main__":
# and when we run the file which contains above statement then __name__ holds
# __main__
# or else when we execute a file by importing a file  as module which contain
# above statement in it then __name__ holds the name of imported module in which
# the above statement exists and also it doesnt invoke uncalled functions from
#imported module else it will invoke all the function of imported module
