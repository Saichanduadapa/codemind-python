n=input()
c=0
res=''
for i in n:
    if i=='6' and c==0:
        res+='9'
        c+=1
    else:
        res+=i
print(res)