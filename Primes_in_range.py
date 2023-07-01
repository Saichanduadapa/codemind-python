import math
a=int(input())
b=int(input())
c,flag=0,0
for i in range(a,b+1):
    if i==1:
        continue
    flag=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        c+=1
print(c)
    
            
