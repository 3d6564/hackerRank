from math import comb
percent, pistons = map(int, input().split())
p = percent / 100
q = 1 - p
n = pistons
# No more than 2 rejects
print(round(sum([comb(n,r)*(p**r)*(q**(n-r)) for r in range(0,3)]), 3))
# At least 2 rejects
print(round(sum([comb(n,r)*(p**r)*(q**(n-r)) for r in range(2,n+1)]), 3))

