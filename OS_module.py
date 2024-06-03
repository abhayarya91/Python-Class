# import os
# print("current working directory:",os.getcwd())
# os.mkdir("python.txt")
# print("directory created")
# print("directories in current location",os.listdir())
# os.rmdir("python.txt")
# print("directory deleted")
# print("OS name:",os.name)

# fd = "python.txt"

# file = open(fd, 'w')
# file.write("hello,this OS module")
# file.close()
# file = open(fd, 'r')
# text = file.read()
# print("Here text:",text)

# try:
#     filename = 'python2.txt'
#     f = open(filename, 'r')
#     text = f.read()
#     f.close()
# except IOError:
#   print('Problem reading: ' + filename)

import os

file_name = "karan.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is a file handling written by Abhay_Arya.\n")
    file.write("Written using Python.\n")
print(f"File '{file_name}' created and written.")

with open(file_name, "r") as file:
    content = file.read()
print(f"Content of the file '{file_name}':")
print(content)

os.remove(file_name)
print(f"File '{file_name}' deleted.")
