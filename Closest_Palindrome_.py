n=int(input())
np=0
bp=0
for i in range(n-1,1,-1):
    i=str(i)
    if i==i[::-1]:
        bp=i
        break
for i in range(n+1,1000000):
    i=str(i)
    if i==i[::-1]:
        np=i
        break
bp=int(bp)
np=int(np)
# print([n,np,bp])
if n-bp==np-n:
    print(bp,np)
elif n-bp>np-n:
    print(np)
else:
    print(bp)