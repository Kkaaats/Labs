from lab1 import BigInteg
from random import choices

x = BigInteg("".join(choices("0123456789abcdef", k=100)))
y = BigInteg("".join(choices("0123456789abcdef", k=2048)))
w=x+y
w=BigInteg(w)
test1=w-y
test1=test1.lstrip('0')
test1=BigInteg(test1)
if test1.LongCmp(x) !=0:
        print('ERROR1!')
else: print("Cat")


for i in range(1):
    a = BigInteg("".join(choices("0123456789abcdef", k=2048)))
    res=BigInteg("0")
    res1=BigInteg("64")
    for j in range(100):
        res=res+a
        res = BigInteg(res)
    res1=res1*a 
    res1 = BigInteg(res1)
    b=res.n
    b = BigInteg(b)
    c=res1.n
    c = BigInteg(c)
    if b.LongCmp(c)!=0:
        print('ERROR1!')
    else: print("Cat")

