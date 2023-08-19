l=10
# def fun1(n):
#    # l=5
#    #  print(l)
#    #  print(n,"hi")
#
# fun1("rohna")

# def fun1(n):
#    # l=5
#     global l
#     l=l+45
#     print(l)
#     print(n,"hi")
#
# fun1("rohna")
"""function inside a function==nested function"""

def har():
    l=2
    def roh():
        global l
        l=45 #it create a global varible out from all the functions
    print("before calling",l)
    roh()
    print("after calling",l)
har()
print(l)