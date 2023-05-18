f = open('madhan','r')
l = f.readline()
while len(l)!=0:
    print(l,end = '')
    l = f.readline()
f.close()