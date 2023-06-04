a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    if i%2==0 and i%3==0:
        s+=1
print(s)
