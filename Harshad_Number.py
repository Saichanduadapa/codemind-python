n=int(input())
for _ in range(n):
    a=input()
    s=0
    for i in a:
        s+=int(i)
    if int(a)%s==0:
        print("YES")
    else:
        print("NO")