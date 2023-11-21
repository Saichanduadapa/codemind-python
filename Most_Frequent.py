n=int(input())
l1=list(map(int,input().split()))
d={}
res=[]
for i in l1:
    if  i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v==max(d.values()):
        res.append(k)
print(min(res))