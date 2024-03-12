import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in lst:
    if is_prime(i):
        cnt+=1
print(cnt)