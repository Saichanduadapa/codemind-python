a,b,c=map(int,input().split())
if a>b and c>b:
    d=(a+c)
elif b>a and c>a:
    d=(b+c)
else:
    d=(a+b)
print(d)