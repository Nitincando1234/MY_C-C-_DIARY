file=open("new.txt","w")
file.write("Hi it is nitin")
file.close()
print(file.closed)
file=open("new.txt","r")
print(file.read())
print(file.mode)