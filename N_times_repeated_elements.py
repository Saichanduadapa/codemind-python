n=int(input())
lst=list(map(int,input().split()))
k=int(input())
ls=[]
for i in set(lst):
    if lst.count(i)==k:
        ls.append(i)
if len(ls)!=0:
    for i in ls:
        print(i,end=' ')
else:
    print(-1)
