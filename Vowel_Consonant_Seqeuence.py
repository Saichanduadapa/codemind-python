n=input()
res=""
if  n[0] in 'aeiouAEIOU':
    res+='V'
else:
    res+='C'
for i in n:
    if i in 'aeiouAEIOU' and res[len(res)-1]!='V':
        res+='V'
    elif i not in 'aeiouAEIOU' and res[len(res)-1]!='C':
        res+='C'
print(res)