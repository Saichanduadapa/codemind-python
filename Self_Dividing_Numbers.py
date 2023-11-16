a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    for j in str(i):
        if j!='0' and i%int(j)==0:
            pass
        else:
            c=1
    if c==0:
        print(i,end=" ")