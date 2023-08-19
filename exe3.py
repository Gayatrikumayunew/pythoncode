#printing star
print("enter number of rows")
inp=int(input())
print("enter 0 and 1 for increasing and decrising order of pattern")
inp2=int(input())
new=bool(inp2)
print(new)
if new==True:
    for i in range(0,inp+1):
        print("*")


        print()
elif new==False:
    for i in range(inp,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
