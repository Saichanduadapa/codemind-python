import math
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    s+=math.sqrt(i)
print("%.2f"%s)