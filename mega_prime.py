import math
def is_prime(n):
    if(n<2):
        return False
    else:
        for i  in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
n=int(input())
if(is_prime(n)):
    s=str(n)
    c=0
    for i in s:
        if(is_prime(int(i))):
            pass
        else:
            print("Not Mega Prime")
            c+=1
            break
    if(c==0):
        print("Mega Prime")
        
else:
    print("Not Mega Prime")