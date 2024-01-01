n=int(input())
for _ in range(n):
    a=int(input())
    m=1
    for i in range(1,a+1):
        m*=i
    print(m)