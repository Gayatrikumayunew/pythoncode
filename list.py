list1=["hello",1,45,"gayu"]
print(list1[::-1])
print(len(list1))
list1.append(7)
list1.insert(2,"hi")
print(list1)
list1.remove("hello")
print(list1)

tuple1=(1,)
print(tuple1)
tuple1=(1,2,3)
print(tuple1)
#tuple1[2]=7 // error
#print(tuple1)

#swaping of two numbers
a=5
b=8
a,b=b,a
print(a,b)
