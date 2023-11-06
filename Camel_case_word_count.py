s=input()
c=0
for i in range(1,len(s)):
    if s[i]==s[i].upper():
        c+=1
print(c+1)