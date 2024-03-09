s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=set(s1)
s2=set(s2)
s=""
for i in (s1.intersection(s2)):
    if i!=' ':
        s+=i
s=sorted(list(s))
if(len(s)!=0):
    print("".join(s))
else:
    print(-1)