n=int(input())
lst=list(map(int,input().split()))
for i in set(lst):
    if lst.count(i)!=1:
        print(i)