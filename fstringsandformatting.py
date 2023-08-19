me = "harry"
a1 = 3
# a = "this is %s %s" % (me, a1)
# print(a)

a = "this is {1} {0}"
b = a.format(me, a1) # places change
print(b)
