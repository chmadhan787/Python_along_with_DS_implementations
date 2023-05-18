#if a method has same name and same number of actual parameters as
# previously defined method then it is called "method overriding"
#this concept is used very heavily

class A:
    def show(self):
        print('in A show')

class B(A):
    def show(self):#this show method overrides the earlier method show in A
        print('in B show')

a1 = B()
a1.show()#first searches method show() in B then goes to A
#show in b has more priority when we create object of B and call method show()