n=int(input())
lst=list(map(int,input().split()))
s=0
res=[]
for i in lst:
    if i==lst.count(i) and i not in res:
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print("%.2f"%(sum(res)/len(res)))