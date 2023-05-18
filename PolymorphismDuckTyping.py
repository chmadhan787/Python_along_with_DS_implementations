#poly = many and morph = forms
#we generally use polymorphism concept in
#loose coupling ,Dependency injection ,inheritance
#there are 4 ways of implementing pyhton
#1.duck typing
#2.operator overloading
#3.method overloadimg
#4.method overriding
#Ducktest : if it looks like a duck,swims like a duck,quack
# like a duck,then probably it is a duck
class Laptop:
    def code(self,ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print('compiling')
        print('running')

class MyEditor:
    def execute(self):
        print('spell check')
        print('convention check')
        print('compiling')
        print('running')

#ide = Pycharm()
ide = MyEditor()
#there no consideration of which type the ide is belong to but it must and
#should have the required method called execute()
#if the class of object ide has the method execute() then ide object do what it
#should do
#if we create ide object of class Pycharm type and if Pycharm contains required
#method called by ide object then ide's job is to call the method and it will be
#excecuted
#even if we create ide object of class MyEditor type and if MyEditor contains
#required method called by ide object then ide's job is to call the method and
#it will be executed
#when compared to duck test what ever be the type of duck we create
#if it look like duck,swims like duck ,quack like duck then probably it will be
#a duck similarly what ever be the type(class) of object(ide) we create
#if it can call the execute method we can probably decide that this method is
#called by ide object and it may belong to any class containg execute() method

lap1 = Laptop()
lap1.code(ide)