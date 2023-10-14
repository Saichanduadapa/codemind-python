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
for i in range(2,n+1):
    for j in range(i+1,n+1):
        if(is_prime(i) and is_prime(j) and i*j==n):
            print(i,j)
            c+=1
            break
if(c==0):
    print(-1)