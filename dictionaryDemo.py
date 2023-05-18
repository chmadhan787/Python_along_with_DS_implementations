#dictionary uses a key and a value in curly braces
d = {1:'madhan',2:'kumar',3:'sameer',4:'suhaas'}
print(d)
print(d[1])
#print(d[5])#return an error becaues there is no value with key 5
print(d.get(5))#it does give error but returns none
print(d.get(5,'not found'))
keys={1,2,3}
values={'madhan','kumar','harsh'}
dic=dict(zip(keys,values))
print(dic)
print(dic[1])
#zip function is used merge to function into a dictionary
#adding values to dictionary
dic[4]='sameer'
print(dic)
del dic[3]#we can delete data from a dictionary
print(dic)
#list and dictionary in dictionary
data = {'python':['pycharm','sublime'],'java':{'JSE':'netbeans','JEE':'ECLIPSE'}}
print(data)
print(data['python'])
print(data['python'][1])
print(data['java'])
print(data['java']['JSE'])