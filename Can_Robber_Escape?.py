n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i%2!=0:
        c+=1
if c>2:
    print("NO")
else:
    print("YES")