#inorder to use the existing features of alredy defined classes we use
#inheritance
class A:#super , parent , base class
    def feature1(self):
        print('feature1 is working from A')
    def feature2(self):
        print('feature2 is working from A')

class B(A):#sub , child , derived class(single level)
    #B inherits features of A
    def feature3(self):
        print('feature3 is working from B')
    def feature4(self):
        print('feature4 is working from B')

class C(B):#multilevel
    def feature5(self):
        print('feature5 is working from C')

class B1:
    def feature6(self):
        print('feature6 is working from B1')

class D(A,B1):#multiple inheritance
    def feature7(self):
        print('feature7 is working from D')

b1 = B()
b1.feature1()
b1.feature2()#we can access features of a using object of B
#because B inherits the features of A
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()

d1 = D()
d1.feature1()
d1.feature6()
d1.feature7()