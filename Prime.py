import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
    
n=int(input())
s,sq=0,0
for i in str(n):
    s+=int(i)
    sq+=int(i)**2
if(prime(sq-s)):
    print("Prime")
else:
    print("Not Prime")