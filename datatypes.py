#none,numeric,list,tuple,set,dictionary,string,range
#when a variable is not assigned with any value then it is none type
#in numerric we have int,float,complex,bool
a=5.6
b=int(a)#type casting
print(b)
k=6
c=complex(b,k)
print(c)
d=b>k
print(d)
print(b<k)
print(int(True))
print(int(False))
#list,tuple,set,range,string comes under sequence category
#python doesnt have char type and even chracter is read as string in python
#print(list(range(10)))
l=list(range(10))#converting range into list
print(l)
print(list(range(2,20,2)))#range(start,stop,step)
#using dictionary we can fetch data in an efficient way using keys rather than
#index number
dict = {1:'madhan',2:'kumar'}
print(dict.keys())
print(dict.values()) 