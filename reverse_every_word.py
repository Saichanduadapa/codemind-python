s=input()
s=s.split()
res=[]
for i in s:
    res.append(i[::-1])
print(*res)