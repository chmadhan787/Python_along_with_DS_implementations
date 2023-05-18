#ABC module is used to acheive abstract classes and ABC means
#abstract base classes
from abc import ABC, abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass
class WhiteBoard(Computer):
    def write(self,obj):
        print('its writing')
        obj.process()

class Laptop(Computer):
    def process(self):
        print('its running')

class Programmer:
    def work(self,com):
        print('solving bugs')
        com.process()

lap = Laptop()
#lap.process()
prog = Programmer()
prog.work(lap)
wh = WhiteBoard()
wh.write(lap)

#a class which have abstract methods are known as abstract classes
#python by default doesnt support abstract classes
#for creating abstract classes we need to import abc module
#we cannot create object for abstract classes