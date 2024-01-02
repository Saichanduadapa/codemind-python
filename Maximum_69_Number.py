n=input()
s=""
c=0
if len(set(n))==1:
    print(n)
else:
    for i in n:
        if i=='6' and c==0:
            s+='9'
            c+=1
        else:
            s+=i
    print(s)