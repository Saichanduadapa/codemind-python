n=int(input())
s=0
s1=0
for i in range(1,n+1):
    s+=(i*i)
    s1+=i
print(pow(s1,2)-s)

    