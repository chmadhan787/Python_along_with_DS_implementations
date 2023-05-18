# we have 3 kinds of methods 1. instance method, 2.class method, 3.static method
# instance variables are owned by the objects of a class similarly instance methods
# variables outside the init belong the class and owned by class and can be accessed
# by class similarly class methods class variables can be created directly but
# creation of class methods require decorator this also applies to static methods.
# we can call class methods using the class name as well as the object of that class
# we already know that the regular methods in a class will take the instance as
# the first argument by default and by convention we call it as self. in order
# to change the first argument to a class we need to use classmethods
# we can convert a regular method to a class method by using a decorator called
# '@classmethod' for example

class Employee :

    number_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first+'.'+last+'@gmail.com'
        self.pay = pay

        Employee.number_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay+self.raise_amt)

    @classmethod # basically this alters the functionality of a method
     # silmilar to self here cls is automatically taken as the first arg
    # and here we work with class instead of the instance/object
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # class-methods as alternative constructors : that means the class-method
    # provides multiple ways of creating the class objects.
    @classmethod
    # this works as an alternate constructor for Employee class
    def from_string(cls, emp_str):
        first, last, pay = empstr1.split('-')
        return cls(first, last, pay)

    # static methods : static methods don't pass any argument automatically
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'Schafer', 50000)
# print(emp1.__dict__) this can be used to check what values are assigned to
# variables inside the object.
emp2 = Employee('Test', 'Employee', 60000)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

Employee.set_raise_amt(1.05)
# emp1.set_raise_amt --> running the class-method using the instance still
# changes the raise_amt

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

empstr1 = 'John-Doe-70000'
empstr2 = 'Steve-Smoth-30000'
empstr3 = 'Jane-Doe_90000'

# first, last, pay = empstr1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(empstr1)

print(new_emp_1.mail)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))




