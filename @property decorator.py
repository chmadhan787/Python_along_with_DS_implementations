# property decorator allow us to

# 1) use class method as attribute:

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # self.msg = self.name + ' got grade ' + self.grade

    @property
    def msg(self):
        return self.name + ' got grade ' + self.grade

    @msg.setter
    def msg(self,msg): # setter method
        sent = msg.split(' ')
        self.name = sent[0]
        self.grade = sent[-1]



std1 = Student('nia','B')

print(std1.name)
print(std1.grade)
# print(std1.msg())
print(std1.msg)

std1.grade = 'A'

print(std1.name)
print(std1.grade)
# print(std1.msg)  this doesn't change
# when we update an attribute in the class then other attributes derived
# from that attribute won't change automatically.
# so to get rid of this problem rather than using an attribute for msg lets
# create a method in the class named msg.
# print(std1.msg()) # before converting the attribute to method there is no need
# use parentheses for accessing but after conversion we need to use parentheses
# for accessing, so it becomes tedious for users to change the code if it is of
# huge number of lines. in these kind of cases we can use property decorator.
# that means the property decorator allows us to change the code inside the class
# without affecting the client code.
print(std1.msg)
# the property attribute allow us to access a method inside the class as an
# attribute.
# if you try to modify that msg method as attribute outside the class as
# sdt1.msg = 'nia got grade A' then we will get an attribute error.
# for that cases we can use the setter and getter methods.
std1.msg = 'Amulya got grade A'
print('name : ',std1.name)
print('grade : ',std1.grade)
print(std1.msg)
print()

# 2) replace setter and getter methods:

class Student1:
    def __init__(self, marks):
        # self.marks = marks
        self.__marks = marks # private variable
    def per(self):
        return (self.__marks/600)*100

    @property
    def marks(self): # getter method
        return self.__marks

    @marks.setter
    def marks(self,value): # setter method
        if value < 0 or value > 600:
            print("can't set value stick to the previous value !!!")
        else:
            self.__marks = value


s = Student1(400)
# s.marks = 500 , in the similar way many users who use the code can modify the data
# by changing the values of the attribute, so in order to hide the data or
# encapsulate the data or implementation details we need to make the marks attribute
# as private. in order to change and access the value of marks without accessing
# the attribute directly we use setter and getter methods.
# hence setter and getter methods are useful to achieve the data encapsulation.
# print(s.marks) no direct access to private variable so this statement gives an
# error message.

# s.setter(500) # the users now has to use this kind of accessing style
# print(s.getter()) # this is also changed
# but the user needs to access that attribute without getting an error using the
# previous style ,so in this kind of situations also we can use the property
# decorator.

s.marks = 500
print(s.marks)
print(s.per(),'%')

# hence now at this point we can change the logic inside the class without
# affecting the client side code. look at the if block added in the setter
# after applying the property decorator.

# when we use the property method then there is no need to change the setter and
# getter methods names to attributes name

"""class Student1:
#     def __init__(self, marks):
#         # self.marks = marks
#         self.__marks = marks # private variable
#     def per(self):
#         return (self.__marks/600)*100
#
#     def marks(self): # getter method
#         return self.__marks
#
#     def marks(self,value): # setter method
#         if value < 0 or value > 600:
#             print("can't set value stick to the previous value !!!")
#         else:
#             self.__marks = value 
      marks = property(getter,setter) # this is the change we need to do."""