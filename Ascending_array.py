n=int(input())
lst=list(map(int,input().split()))
l=sorted(lst)
if(len(lst)!=len(set(lst))):
    print("no")
else:
    if(lst==l):
        print("yes")
    else:
        print("no")