n=int(input())
lst=list(map(int,input().split()))
r=[]
for i in lst:
    r.append(len(str(i)))
for i in lst:
    if len(str(i))==max(r):
        print(i,end=' ')