n=input()
s=0
m=1
for i in n:
    s+=int(i)
    m*=int(i)
print(m-s)