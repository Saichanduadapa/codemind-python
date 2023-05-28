a=input()
b=input()
cnt=0
for i in a:
    if i==b:
        cnt+=1
if cnt==0:
    print("-1")
else:
    print(cnt)