n=int(input())
while(True):
    n+=int(str(n)[::-1])
    if str(n)==str(n)[::-1]:
        break
print(n)