n=int(input())
lst=list(map(int,input().split()))
o,e=0,0
for i in lst:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))