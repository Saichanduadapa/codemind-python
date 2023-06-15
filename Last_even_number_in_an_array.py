n=int(input())
lst=list(map(int,input().split()))
lst.reverse()
for i in range(n):
    if lst[i]%2==0:
        print(lst[i])
        break