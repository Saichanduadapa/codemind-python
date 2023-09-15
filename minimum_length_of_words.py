s=input()
m=len(s)
s=s.split()
for i in s:
    m=min(len(i),m)
print(m)