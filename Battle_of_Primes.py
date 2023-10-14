import math
def is_prime(n):
    if(n<2):
        return False
    else:
        for i  in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
n=int(input())
m=int(input())
if(is_prime(m+n)):
    for i in range(n+m+1,10000000):
        if(is_prime(i)):
            print(i-(n+m))
            break
else:
    for i in range(n+m,10000000):
        if(is_prime(i)):
            print(i-(n+m))
            break