s=input()
s=s.split()
res=[]
for i in s:
    if s.index(i)%2==0:
        res.append(i[::-1])
    else:
        res.append(i)
print(*res)
