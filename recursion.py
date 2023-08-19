# def fac_fun(n):
#     fac=1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# print("enter")
# numbers=int(input())
# print(fac_fun(numbers)

"""recursive approach"""

def fac_rec_fun(n):
    if n==1:
        return 1
    else:
        return n* fac_rec_fun(n-1)

numbers=int(input("enter"))
print("factorial is ",)
a=fac_rec_fun(numbers)
print(a)

