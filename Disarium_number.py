n=input()
s=0
for i in n:
    v=int(i)
    p=n.index(i)+1
    s+=v**p
if int(n)==s:
    print(True)
else:
    print(False)