s=set()
"""print(type(s)
      #)
l=[1,2,8,5]
s_from_list=set([1,2,8,5])
s_from_list=set(l)
print(s_from_list)
s.add(9)

s.add(9)
print(s)
s.add(1)
s.add(5)
s.union({1,5,6})
s1=s.union({1,5,6})
s1=s.intersection({1,5,6})
print(s1,s)
"""
s.add(5)
s.add(4)
s1={9,8} # if both sets have different values then true else false
print(s.isdisjoint(s1))
s.remove(4)
print(s)