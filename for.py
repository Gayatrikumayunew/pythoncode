"""list1=("harry","larry","marry")
for item in list1:
    print(item)

list1=(['harry','codd'],["larry","danve"],["marry","dono"])
for item in list1:
    print(item)

dict1=dict(list1)
print(dict1)
'
"""
list1=["j",58,"jid",85,6]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)
