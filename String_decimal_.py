n=int(input())
for i in range(n):
    s=input()
    flag=0
    for i in s:
        if i.isdigit():
            pass
        else:
            flag+=1
    if flag!=0:
        print(False)
    else:
        print(True)