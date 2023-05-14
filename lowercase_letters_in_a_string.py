s=input()
cnt=0
for i in s:
    j=i.upper()
    if j!=i:
        cnt+=1
print(cnt)