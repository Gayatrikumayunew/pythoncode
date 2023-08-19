def febo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return  febo(n-1)+febo(n-2)

n=febo(5) #we are providing the index number
print(n)
