s=input()
s=s.split()
m=min(s[len(s)-1])
if m.lower() in s[len(s)-1]:
    print(m.lower())
else:
    print(m)