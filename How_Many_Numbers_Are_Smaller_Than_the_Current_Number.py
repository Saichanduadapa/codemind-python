n=int(input())
lst=list(map(int,input().split()))
ar=[]
for i in range(n):
    c=0
    for j in range(n):
        if i==j:
            continue
        if lst[i]>lst[j]:
            c+=1
    ar.append(c)
print(*ar)