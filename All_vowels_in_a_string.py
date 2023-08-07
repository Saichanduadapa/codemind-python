s=input()
res=[]
for i in s:
    if i in 'aeiou' and i not in res:
        res.append(i)
if len(res) ==5 :
    print(True)
else:
    print(False)