from math import *
n=int(input())
lst=list(map(int,input().split()))
res=[]
for i in lst:
    res.append(prod(lst)//i)
print(*res)