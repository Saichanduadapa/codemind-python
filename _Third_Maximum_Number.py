n=int(input())
lst=list(map(int,input().split()))
lst=set(lst)
if n<3:
    print(max(lst))
else:
    lst.remove(max(lst))
    lst.remove(max(lst))
    print(max(lst))