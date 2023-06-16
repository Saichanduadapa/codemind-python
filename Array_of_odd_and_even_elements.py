n=int(input())
lst=list(map(int,input().split()))
lst1=[]
lst2=[]
for i in lst:
    if i%2!=0:
        lst1.append(i)
    else:
        lst2.append(i)
for j in lst2:
    lst1.append(j)
for i in lst1:
    print(i,end=' ')