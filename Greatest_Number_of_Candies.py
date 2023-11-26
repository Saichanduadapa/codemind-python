n=int(input())
lst=list(map(int,input().split()))
k=int(input())
res=[]
for i in lst:
    if i+k>=max(lst):
        res.append(True)
    else:
        res.append(False)
print(*res)