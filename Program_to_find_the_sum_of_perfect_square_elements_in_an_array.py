import math
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if math.sqrt(i)==int(math.sqrt(i)):
        c+=i
print(c)