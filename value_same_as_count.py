n=int(input())
lst=list(map(int,input().split()))
c=0
for i in set(lst):
    if i==lst.count(i):
        c+=1
print(c)
        