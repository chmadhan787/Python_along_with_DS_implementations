#inorder to implement threading concept we need to import tthreading module
#when we break down a large process into small parts each part will be called
# a thread
# thread is a light weight path
# by default every execution will have one thread called main thread.
from time import sleep
from threading import *
class Hello(Thread):
    #thread internally have method run
    def run(self):
        for i in range(5):
            #to slow down the execution we need to use the sleep form time
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
#when you say t1.start() internally it will call run()
sleep(0.2)#this will save threads from collision
t2.start()
#sometimes two thresds collide each other tht means they will be executed at the
#same time
t1.join()
t2.join()
#main thread will continue after joining t1 and t2 in execution then prints bye
print('bye')