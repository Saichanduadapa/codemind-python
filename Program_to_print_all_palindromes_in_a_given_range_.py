n=int(input())
m=int(input())
for i in range(n,m+1):
    if i==int(str(i)[::-1]):
        print(i,end=" ")