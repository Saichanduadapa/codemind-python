import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if prime(n):
    flag=0
    for i in str(n):
        if prime(int(i)):
            pass
        else:
            flag=1
    if flag==0:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')