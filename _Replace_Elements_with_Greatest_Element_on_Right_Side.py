n=int(input())
l1=list(map(int,input().split()))
res=[]
for i in range(n-1):
    res.append(max(l1[i+1:n]))
res.append(-1)
print(*res)