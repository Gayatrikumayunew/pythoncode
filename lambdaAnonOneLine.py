# def minus(x,y):return x-y  # is equal to = minus = lambda x,y:x-y [here both are same]
# print(minus(9,4))

def a_first(a):
    return a[1]


a = [[1, 5], [52, 4], [45, 7]]
a.sort(key=a_first)
print(a)