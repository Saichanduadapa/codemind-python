import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    res=prime(i)
    if res:
        print(i)