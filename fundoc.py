# a=5
# b=8
# c=a+b
# print(c)

# def fun1():
#     print("hello you are in fun1")
# print(fun1())#also can use fun1()

def fun2(a,b):
    """ this is a average calculating function"""
    average=(a+b)/2
    return average
print(fun2.__doc__)
v=fun2(5,5)
print(v)




