
a = 5
#b = 'madhan'
b = 6
print(a+b)#we cannot use + operator for two different types
print(int.__add__(a,b))# for above print statement this will be done behind
# the scene
print()
a = '5'
b = '6'
print(a+b)#we cannot use + operator for two different types
print(str.__add__(a,b))# for above print statement this will be done behind
# the scene
#all the operators behind the scenes will work as methods
#when we use + ,add() will be called and for - , sub() and for * , mul()

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):#gt = grater than function
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1,self.m2
        # return '{} {}'.format(self.m1,self.m2)

s1 = Student(45,56)
s2 = Student(67,55)

#s3 = s1 + s2#this will give error since there is no add method for classes
#but if we define add method it can be done without error

s3 = s1 + s2 #behind the scene it will be taken as Student.__add__(s1,s2)
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

a = 9
#print(a)
print(a.__str__())#behind scene when we call a it calls str

# print(s1)
print(s1.__str__())
# it prints object address but if we need value like we print a we need to
# override str function
#after overloading the str funtion it returns a tuple with marks
#but to change tuple to string format replace return in str with
#return '() ()'.format(self.m1,self.m2)
print(s2.__str__())