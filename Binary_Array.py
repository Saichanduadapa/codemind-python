n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i==1 or i==0:
        c+=1
if c==len(lst):
    print(True)
else:
    print(False)