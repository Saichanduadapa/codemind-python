def bags(a,b,c):
    res=b*c
    if a%res==0:
        return(a//res)
    elif a%res!=0:
        return((a//res)+1)

a,b,c=map(int,input().split())
print(bags(a,b,c))