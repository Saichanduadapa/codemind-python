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
c=0
for i in range(1,n+1):
    if(n%i==0 and is_prime(i)==False):
        c+=1
print(c)