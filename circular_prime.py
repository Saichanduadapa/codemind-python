import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if prime(n):
    s=str(n)[::-1]
    if prime(int(s)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
    
