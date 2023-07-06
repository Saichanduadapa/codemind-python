n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    ar1=list(map(int,input().split()))
    ar2=list(map(int,input().split()))
    res=sorted(ar1+ar2)
    print(*res)