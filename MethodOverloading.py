#if a method has same name as previously defined method but different
# number of actual parameters then it is called "method overloading"

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a,b):
        s = a + b
        return  s

    def sum(self,a,b,c):#overloaded method for sum() or else we can use default
        #arguments in sum() function
        s = a + b + c
        return s

    # def sum(self,a=None,b=None,c=None):
    #     s = 0
    #     if a!=None and b!=None and c!=None:
    #         s = a + b + c
    #     elif a!=None and b!=None:
    #         s = a + b
    #     else:
    #         s = a
    #     return s


s1 = Student(56,65)

print(s1.sum())
#so this is called method Overloading