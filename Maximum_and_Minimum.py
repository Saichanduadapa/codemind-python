n=int(input())
lst=list(map(int,input().split()))
res=[]
for i in (lst):
    if i==lst.count(i) and i not in res:
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print(res[0],res[len(res)-1])