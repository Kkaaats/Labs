from lab3 import PB
from random import choices, randint

a = PB(''.join(choices('01', k=580)))
b = PB(''.join(choices('01', k=580)))
c = PB(''.join(choices('01', k=100)))
n1=((a+b)*c).n
n2=((a*c + b*c).n)
# print(len(n1))
# print(len(a.n))
if n1 != n2:
    print("Error1")
else: print("Cat")

k = PB(''.join(choices('01', k=100)))
m=randint(1,10)
res=PB("1")
for i in range(m):
    res1=res*k
    res=res1
res2=k**m
if res1.n != res2.n: 
    print("Error2")
else: print("Cat")

