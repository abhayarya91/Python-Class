
#create file
s = "this is my file handling program"

file = open("demo.txt","w")
file.write(s)
file.close()
print("file created")

#reade file
# file = open("demo.txt","r")
# filecontent = file.read()
# print(filecontent)
fileconect = file.read()
print(fileconect)

#list store into file
list = ["python","java","CSS","Advance"]
file = open("demo2.txt","w")
file.writelines(list)
file.close()
print("list writen in file")

#read file
file = open("demo2.txt","r")
filelist = file.readlines()
print(filelist)

#append the file
s = " python file handling."
file = open("demo.txt","a")
file.write(s)
file.close()
print("file update")
