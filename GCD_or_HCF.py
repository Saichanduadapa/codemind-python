a,b=map(int,input().split())
lst=[]
for i in range(1,max(a,b)):
    if a%i==0 and b%i==0:
        lst.append(i)
print(max(lst))