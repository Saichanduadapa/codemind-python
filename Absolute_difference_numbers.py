a,b=map(int,input().split())
a=str(a)
l=len(a)
r1=a[:b]
r2=a[l-b:]
print(abs(int(r1)-int(r2)))