n=int(input())
lst=list(map(int,input().split()))
s=''
for i in lst:
    s+=str(i)
print(int(s,2))