import math
n=int(input())
lst=list(map(int,input().split()))
res=[]
for i in lst:
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            break
    else:
        res.append(i)
print("%.2f"%(sum(res)/len(res)))