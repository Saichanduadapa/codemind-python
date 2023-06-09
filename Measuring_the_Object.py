n,x,y,z=map(int,input().split())
if n==x or n==y or n==z or n==x+y or n==x+z or n==y+z or n==x+y+z:
    print("YES")
else:
    print("NO")