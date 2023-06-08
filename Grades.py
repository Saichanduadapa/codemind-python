a,b,c,d,e=map(int,input().split())
per=(a+b+c+d+e)/5
if per>=90:
    print("Grade A")
elif per<90 and per>=80:
    print("Grade B")
elif per<80 and per>=70:
    print("Grade C")
elif per<70 and per>=60:
    print("Grade D")
elif per<60 and per>=40:
    print("Grade E")
else:
    print("Grade F")