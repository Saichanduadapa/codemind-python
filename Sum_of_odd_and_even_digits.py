n=int(input())
lst=list(map(int,input().split()))
s1,s2=0,0
for i in range(n):
    if i%2==0:
        s1+=lst[i]
    else:
        s2+=lst[i]
if abs(s1-s2)==0:
    print('YES')
else:
    print("NO")