#we have three types of methods in python oops
#1.instance method  2.class method  3.static method
#class and static methods are different but in case of variables they are same
#in instance type of methods we have Accessor methods and Mutator methods
#for fetching the values w use accessors and for modifying the values we use
#mutators
class Student:
    school = 'school name : telusko'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return "average marks",(self.m1+self.m2+self.m3)/3
    #
    # def get_m1(self):#accessor
    #     return self.m1
    #
    # def set_m1(self,value):#mutators
    #     self.m1 = value
    @classmethod#decorator(we should always use this for class methods)
    def get_school(cls):#class method
        #when we work with instance variables we use self keyword
        #when we work with class variables we use cls keyword
        return cls.school
    #when we are not concerened about instance and class variables we need
    #to use static methods
    @staticmethod#decorator(we should always use this for static methods)
    def info():#it does not related to class or instance variables so keep
        #it empty
        print("belongs to Student class...")

s1=Student(34,67,78)
s2=Student(55,76,85)

print(Student.get_school())
print(s1.avg())
print(s2.avg())
Student.info()
#class methods work with class variables
#instance methods work with instance variables
#static variables work independently
