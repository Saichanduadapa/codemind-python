n=int(input())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
res=[]
for i in range(len(lst1)):
    res.append(lst1[i]+lst2[i])
print(*res)
