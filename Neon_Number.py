n=int(input())
sq=n*n
s=0
for i in str(sq):
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")