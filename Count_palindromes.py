n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    i=str(i)
    if i==i[::-1]:
        c+=1
print(c)