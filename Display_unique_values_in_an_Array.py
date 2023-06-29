n=int(input())
lst=list(map(int,input().split()))
ls=[]
for i in lst:
    if lst.count(i)==1:
        ls.append(i)
if len(ls)==0:
    print(-1)
else:
    for i in ls:
        print(i,end=" ")