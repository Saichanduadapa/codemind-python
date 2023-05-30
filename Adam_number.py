n=int(input())
sq1=n*n
rev=str(n)[::-1]
sq2=int(rev)*int(rev)
if str(sq1)==str(sq2)[::-1]:
    print(True)
else:
    print(False)