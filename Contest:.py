def contest(a,b,c):
    if b*1+c*2>=a:
        return("Qualify")
    else:
        return("Not Qualify")
a,b,c=map(int,input().split())
print(contest(a,b,c))