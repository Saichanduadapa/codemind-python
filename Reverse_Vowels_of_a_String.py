n=input()
r=""
for i in n:
    if i in 'aeiouAEIOU':
        r+=i
res=""
r=r[::-1]
k=0
for i in n:
    if i in "AEIOUaeiou":
        res+=r[k]
        k+=1
    else:
        res+=i
print(res)