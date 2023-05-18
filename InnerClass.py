
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(s1.name, s1.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.gen = 'i5'
            self.ram = '8gb'
            #we can create object of Laptop in outer class (Student)
        def show(self):
            print(self.brand, self.gen, self.ram)


s1 = Student('madhan',1)
s2 = Student('kumar',2)

s1.show()
#s1.lap.brand or
# lap1 = s1.lap
# lap2 = s2.lap
# print(id(lap1))
# print(id(lap2))
#print(lap1.brand,lap1.gen,lap1.ram)
#print(lap2.brand,lap2.gen,lap2.ram)
#you can create object of inner class inside the outer class
#you can create object of inner class outside the outer class provided
#you use the outer class name to call it
#like
#lap1 = Student.Laptop()