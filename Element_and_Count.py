n=int(input())
lst=list(map(int,input().split()))
res=[]
r=[]
for i in lst:
    if i not in r:
        r.append(i)
for i in r:
    res.append(i)
    res.append(lst.count(i))
print(*res)