n = 5
print(id(n))#to print adrress of variable
nn = 'madhan'
print(id(nn))
a=10
b=a
print(a,b)
print(id(a),id(b))
#hence in python if two variables have same values then they points to same
#box where the values is stored hence python is memory efficient
print(id(10))
k = 10
print(id(k))
a=9
print(id(a))
k=a
print(id(k))
b=8
#now no one is using 10 hence it is ready for garbage collection
#we cannot make a variable final or constant in python
#to know the type of varable use type() function
print(type(b))