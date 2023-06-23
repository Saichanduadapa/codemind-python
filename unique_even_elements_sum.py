n=int(input())
lst=list(map(int,input().split()))
c=0
for i in set(lst):
    if i%2==0:
        c+=i
print(c)