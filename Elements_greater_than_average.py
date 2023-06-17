n=int(input())
lst=list(map(int,input().split()))
avg=sum(lst)//n
cnt=0
for i in lst:
    if i>=avg:
        cnt+=1
print(cnt)
