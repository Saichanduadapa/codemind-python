n,m=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
res=[]
for i in lst1:
    if i not in lst2 and i not in res:
        res.append(i)
for i in lst2:
    if i not in lst1 and i not in res:
        res.append(i)
for i in(res):
    print(i,end=' ')