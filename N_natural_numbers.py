def num(n):
    if n>0:
        num(n-1)
        print(n,end=' ')
n=int(input())
num(n)
