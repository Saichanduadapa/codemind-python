s1=input()
s2=input()
s1,s2=s1.lower(),s2.lower()
c=0
for i in s2.split():
    if i in s1.split() :
        c+=1
print(c)