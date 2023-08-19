
print("enter num1")
num1=int(input())
print("enter mun2")
num2=int(input())
print("enter operator")
ope=input()

if ope=="+" and num1==56 and num2==9:
    print("77")
elif ope=="-":
    print("subtraction is",num1-num2)
elif ope=="*" and num1==45 and num2==3:
    print("multiplication is 555")
elif ope=="/" and num1==16 and num2==6:
    print("division is 4")
else:
    if ope=="+":
        print("sum is",num1+num2)
    elif ope=="/":
        print("divisiom is ",num1/num2)
    elif ope =="*":
        print("multiplication is",num1*num2)
    else:
        print("wrong")
