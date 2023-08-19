# f=open("hello.txt")
# content=f.read()
# print(content)
# f.close()

# f=open("hello.txt","rb")
# content=f.read()
# print(content)
# f.close()

# f=open("hello.txt","r")
# content=f.read(5)
# print(content)
# f.close()

"""reading file line by line"""

# f=open("hello.txt","rt")
# content=f.read()
# for line in content:
#
#     print(line,end=" ")
# f.close()

"""read line function"""
# f=open("hello.txt","r")
#
# print(f.readline())
# f.close()

f=open("hello.txt","r")

print(f.readlines())
f.close()



