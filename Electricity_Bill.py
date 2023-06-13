u=int(input())
if u<=199:
    uc=1.20
elif u>=200 and u<400:
    uc=1.40
elif u>=400 and u<600:
    uc=1.60
elif u>=600 and u<800:
    uc=1.80
else:
    uc=2.00
b=u*uc
if b<=400:
    sc=0
else:
    sc=b*0.15
tb=b+sc
print("Units Consumed: %.0f"%u)
print("Cost per Unit: %.2f"%uc)
print("Bill: %.2f"%b)
print("Surcharge: %.2f"%sc)
print("Total Amount: %.2f"%tb)
