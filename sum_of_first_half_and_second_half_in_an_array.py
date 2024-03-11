n=int(input())
lst=list(map(int,input().split()))
m=n//2
a,b=0,0
for i in range(m):
    
    a+=lst[i]
print(a)
for i in range(m,n):
    b+=lst[i]

print(b)