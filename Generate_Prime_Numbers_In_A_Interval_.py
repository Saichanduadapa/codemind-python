import math
def is_prime(n):
    if(n<2):
        return False
    else:
        for i  in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(is_prime(i)):
        print(i,end="
")