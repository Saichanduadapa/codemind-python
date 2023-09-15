s=input()
m=0
s=s.split()
for i in s:
    m=max(len(i),m)
print(m)