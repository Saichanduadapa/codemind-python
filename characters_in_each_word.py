s=input()
s=s.split()
res=[]
for i in s:
    res.append(len(i))
print(*res)