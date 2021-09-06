from math import comb
b,g = map(float, input().split())
p = b / (b + g)
q = 1 - p
print(round(sum([comb(6,r)*(p**r)*(q**(6-r)) for r in range(3,7,1)]), 3))
