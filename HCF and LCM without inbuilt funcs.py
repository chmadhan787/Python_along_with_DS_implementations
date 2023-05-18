n1 = int(input())
n2 = int(input())

def factors(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l

def hcf(n1,n2):
  n1_factors = set(factors(n1))
  n2_factors = set(factors(n2))
  common = n1_factors.intersection(n2_factors)
  return max(common),min(common)

hcf,lcm = hcf(n1,n2)

print(hcf,' ',lcm)