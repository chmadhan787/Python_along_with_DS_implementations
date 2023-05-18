
class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        print('feature1 is working from A')
    def feature2(self):
        print('feature2 is working from A')

class B:
    #B inherits features of A
    def __init__(self):
        #super().__init__()
        print('in B init')

    def feature1(self):
        print('feature3 is working from B')
    def feature4(self):
        print('feature4 is working from B')

class C(A,B):
    def __init__(self):
        super().__init__()#this calls inti of A according to MRO
        #it always go from left to right ie first A then B
        print('in C init')
    def feat(self):
        super().feature2()
        #we can also use super() to call methods not only init

#a1 = B()#even if we create object for B it will automatically calls constructor
#of A scine init is only in A
#but if we also create init in B it calls init in B
#hence if you create object of sub class it will first try to find init of
#sub class and if it is not found then it search init of super class
#but we can call init of super class even there is init present in sub class
#using super().any method of super class

c1 = C()
c1.feature1()#calls according to MRO ie first checks in A then B
c1.feat()