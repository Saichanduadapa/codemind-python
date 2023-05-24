n=int(input())
for i in range(n):
    a=input()
    if int(a)==int(a[::-1]):
        print (True)
    else:
        print (False)