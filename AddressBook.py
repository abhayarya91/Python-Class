#WAP to create address book.
import os
print(os.getcwd)

while True:
    file=open(r'C:\Users\abhay\OneDrive\Documentos\Python\AbhayArya\address.txt',"a")
    Name = input("Enter your Name:")
    Address = input("Enter your Address:")
    Phone_No = input("Enter your Phone No:")
    file.write("\nName:"+Name)
    file.write("\nAddress:"+Address)
    file.write("\nPhone_No:"+Phone_No)
    file.close()

