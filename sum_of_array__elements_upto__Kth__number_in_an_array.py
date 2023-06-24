n=int(input())
lst=list(map(int,input().split()))
k=int(input())
s=0
for i in range(k):
    s+=lst[i]
print(s)