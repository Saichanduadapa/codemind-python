n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in lst:
    if(i>=a and i<=b):
       print(i,end=" ")
       c+=1
if(c==0):
    print(-1)