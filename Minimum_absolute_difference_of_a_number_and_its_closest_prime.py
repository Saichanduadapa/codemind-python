import math
def is_prime(n):
    if(n<2):
        return False
    else:
        for i  in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
p=int(input())
if(is_prime(p)):
    print(0)
else:
    np,bp=p+1,p-1
    while(not is_prime(np)):
        np+=1
    while(not is_prime(bp)):
        bp-=1
    if(np-p<p-bp):
        print(np-p)
    else:
        print(p-bp)