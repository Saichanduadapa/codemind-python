n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
m=max(lst)
for i in lst:
    if(i>=a and i<=b and i<m):
        m=i
if(m==max(lst)):
    print(-1)
else:
    print(m)