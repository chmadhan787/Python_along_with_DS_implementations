n = input()
if len(n)<=100:#constraints check
    print("CHAT WITH HER!") if len(set(n))%2==0 else print("IGNORE HIM!")
else:
    print("constraints not satisfied")
