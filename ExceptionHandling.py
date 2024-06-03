
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ValueErro
# a = int(input("Enter the value of a: "))
# print("A:",a)
# print(type(a))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> valueError is handle >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# try:
#     a = int(input("Enter the value of a: "))
#     print("A:",a)
#     print(type(a))
#     # print("Code run seccessfully")
# except:
#     print("your logic is incoorect...")
# else:
#     print("No Error...Code is Run..")    




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZeroDivisionError >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = a/b
# print("result",c)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Here ZeroDivisionError is hanlde >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# try:
#     c = a/b
#     print("result:",c)
# except:    
#     print("your logic in incorrect")
# print("thank you")  



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.SyntexError>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

# print("helle)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.Hanlde SyntexError

# try:
#     print(hello)
# except:
#     print("your logic is incorrect....")
# else:
#     print("Error not found..")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TypeError >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# x = "20"
# y = 5
# z = x+y
# print("result=",z)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Hendle TypeError>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# try:
#     a = "45"
#     b = 5
#     c = a + b
#     print("result...",c)
# except:
#     print("incorrect logic")
# else:
#     print("Error not found")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ImportError >>>>>>>>>>>>>>>>>>>>>>>

# import xyz as u

#>>>>>>>>>>>>>>>>>>>>>>>>>>> Hnadle importError >>>>>>>>>>>>>>>>>>>>>

# try:
#     import abcd as o
# except:
#     print("incorrect logic")
# else:
#     print("Error Not found...")















# #..........................................many exception handle
# try:
    
#     print(x)
# except NameError:
#     print("variable not define")
# except:
#     print("exception cought")          


















    




#...................use else part in exception
# try:
#     print("hello")
# except:
#     print("Something went wrong:")
# else:
#     print("Nothing went wrong:")
    
    
    
    
# try:
#     #print("hello")
#     print(x)
# except:
#     print("Something went wrong:")
# else:
#     print("Nothing went wrong:")   


#..................................finally block
# try:
#     print("hello")
# except:
#     print("something went wrong:")
# finally:
#     print("finally run")     
    
    
    
# try:
#     print(h)
# except:
#     print("something went wrong:")
# finally:
#     print("finally run")         




#.................................user define Exception
# class MyException(Exception):
#     pass
# g = 25
# if g > 5:
#     raise MyException("something wrong")
