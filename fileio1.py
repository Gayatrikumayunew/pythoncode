"""it delete other content"""
# f=open("hello.txt","w")
# f.write("hello new line")
# f.close()

"""appending"""
# f=open("hello.txt","a")
# f.write("\nhello new second line")
# f.close()
"""read and write both"""
f=open("hello.txt","r+")
print(f.read())
f.write("\nhello new second ..line")
f.close()