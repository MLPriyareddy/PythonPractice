try:
    a,b=10,0
    print(a/b)
except ZeroDivisionError:
    print("Zerodivisionerror occured")


file=open("File.txt", 'w')
file.write("This is file handling1\n")
file.write("This is file handling2\n")
file.write("This is file handling3\n")
file.close()

file=open("File.txt", 'r')
x=file.read()
print(x)
file.close()

file=open("File.txt", 'a')
file.write("This is file handling4\n")
file.write("This is file handling5\n")
file.close()