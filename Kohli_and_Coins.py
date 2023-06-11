n=int(input())
if n%10==0:
    print(int(n/10))
elif (n%10)%5==0:
    print(int((n/10)+(n%10)/5))
else:
    print(-1)