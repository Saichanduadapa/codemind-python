import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    t1=n
    t2=n
    while not prime(t1):
        t1-=1
    while not prime(t2):
        t2+=1
    if(n-t1>t2-n):
        print(t2)
    else:
        print(t1)
        