n=input()
p=1
s=0
for i in n:
    p*=int(i)
    s+=int(i)
print(p-s)