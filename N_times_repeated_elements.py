n=int(input())
lst=list(map(int,input().split()))
k=int(input())
c=0
for i in set(lst):
    if lst.count(i)==k:
        print(i,end=" ")
        c+=1
if c==0:
    print(-1)