"""i=0
while(True):
    print(i+1,end="")
    if(i==44):
        break
        i=i+1"""# never ending loop

"""i=0

while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        break
    i=i+1"""

while(True):
    inp=int(input("enter number"))
    if inp>100:
        print("congrates you are pass")
        break
    else:
        print("try again")
        continue

