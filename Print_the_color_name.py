def color(n):
    if n=='V':
        return("Violet")
    elif n=='I':
        return("Indigo")
    elif n=='B':
        return ("Blue")
    elif n=='G':
        return ("Green")
    elif n=='Y':
        return("Yellow")
    elif n=='O':
        return("Orange")
    elif n=='R':
        return ("Red")
    else:
        return(-1)
        
n=input()
print(color(n))
