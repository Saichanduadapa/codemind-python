n=input()
lst=list(map(int,input().split()))
r=[]
c=0
for i in lst:
    r.append(len(str(i)))
for i in lst:
    if len(str(i))==max(r):
        c+=1
print(c)