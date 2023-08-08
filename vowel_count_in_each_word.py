s=input()
s.lower()
s=s.split()
res=[]
for i in s:
    c=0
    for j in i:
        if j in 'aeiou'  :
            c+=1
    res.append(c)
print(*res)