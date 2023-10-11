n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in lst:
    if(i>=a and i<=b):
        m+=i
print(m)