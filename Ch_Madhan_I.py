s = list(input())
check = [i for i in s if i=='(' or i==')']#constraints check
if 0<=len(s)<=3*104 and len(s)==len(check):#constraints check
    c=e=0
    for i in s:
        if i=="(":
            c+=1
        else:
            e+=1
    print(min(c,e)*2)
else:
    print("0")#when other than parantheses occur then constraints will not be satisfied