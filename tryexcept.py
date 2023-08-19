print("enter first number")
num1=input()
print("enter second number")
num2=input()
try:
    print("the sum is",int(num1)/int(num2))
except exception as e:
    print(e)
finally:
    print("this is important")