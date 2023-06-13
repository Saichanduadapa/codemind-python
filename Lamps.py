n,k,x,y=map(int,input().split())
r=k*x
n=n-k
if x>y:
    c=n*y
else:
    c=n*x
print(r+c)