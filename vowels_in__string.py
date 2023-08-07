s=input()
res=[]
for i in (s):
    if i in 'aeiouAEIOU' and i not in res:
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print(*res)