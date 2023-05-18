us = sorted(list(map(int,input()[1:-1].split(","))))
check = [i for i in us if -109<=i<=109]#constraints check
if 0<=len(us)<=105 and len(us)==len(check):#constrains check
    c = 1
    for i in range(len(us)-1):
        if abs(us[i]-us[i+1])==1:
            c+=1
    print(c)
else:
    print("constraints not satisfied")
