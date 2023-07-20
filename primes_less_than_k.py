import math
n=int(input())
lst=list(map(int,input().split()))
k=int(input())
c=0
#print(lst,k)
for i in lst:
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            break
    else:
        if i<=k:
            c+=1
print(c)