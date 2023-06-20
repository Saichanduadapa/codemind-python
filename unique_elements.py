n=int(input())
lst=list(map(int,input().split()))
res=[]
for i in lst:
    if i not in res:
        res.append(i)
for i in res:
    print(i,end=' ')