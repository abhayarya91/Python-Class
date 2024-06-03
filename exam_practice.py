# # # searching in regex
# # import re

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> re.split  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import re
# text = "You,Need,Meed,Feed,Teed Deed to use the import keyword along with the desired module name" 
# k = text.split(',')
# print(k)


# string = "one,two,three"
# words = string.split(',')
# print(words)



# pattern = r"[A-Z]+eed"s
# text = "You Need Meed Feed Teed Deed to use the import keyword along with the desired module name"
# print(re.split(pattern,text))




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> re.compile  >>>>>>>>>>>>>>>>>>...>>>>>>>>>>>>>>>>>>>> 

# import re
# text = "You Need Meed Feed Teed Deed to use the import keyword along with the desired module name"

# pattern = re.compile(r'\b\w{4}\b')

# for match in pattern.findall(text):
#     print(match)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> re.sub >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import re
# text = "You Need Meed Feed Teed Deed to use the import keyword along with the desired module name" 
# print(re.sub(r'Meed','cool',text))






# import re 

# print(re.subn('ub', '~*', 'Subject has Uber booked already')) 

# t = re.subn('ub', '~*', 'Subject has Uber booked already',flags=re.IGNORECASE) 
# print(t) 
# print(len(t)) 
# print(t[0]) 






#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. matplotLip  >>>>>>>>>>>>>>>>>>>
import matplotlib.pyplot as plt
import numpy as np
x= np.array([0,15])
y= np.array([0,95])

plt.plot(x,y)
plt.show()





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  re.search  and re.findall  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import re
# text = "You Need Meed Feed Teed Deed to use the Meed Meed import keyword along with the desired module name"
# print(re.search(r'Meed',text))

# print(re.findall(r'Meed',text))









#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> import sys  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import sys
# print("kya hal h bhai....?")


# print("ye rha bhai...",sys.path)
# # print(sys.path)
# print(sys.platform)
# print(sys.executable)
# print("ye rha bhai tumhamra module...",sys.modules)
# print(sys.copyright)
# sys.exit()
# print("kam khamtam....")





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> import random  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import random
# print(random.randint(2,9))
# print(random.randrange(3,11))
# l = ["abhay","ayah","afusfgy","gjhrthgi"]
# print(random.choice(l))





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> import datetime >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import datetime
# print("is time ka time.....",datetime.datetime.now())

# # print("date and time of....",datetime.datetime(2002,2,31))
# x = datetime.datetime(2002,9,23)
# print(x)

























# # txt = "We are the the best in the world to tackle with you"
# # x = re.search("the", txt)
# # if x:
# #     print("Yes,you can do this amazing task")
# # else:
# #     print("No, you can't do anything")

# # # """
# # # #matching in regex

# # # import re

# # # txt = "We are the  best in the world to tackle with you our cantacts are 1234567890, 9876543219, 9876543210"
# # # txt1 = "We are the  best in the world to tackle with you our cantacts are ltsu@gmail.com, ltsi@gmail.com, lmsu@gmail.com"

# # # x=re.findall(input("enter the no. you want to search :"),txt)
# # # x2=re.findall(input("enter the email you want to search :"),txt1)

# # # if x:
# # #     print("Yes,mil gye re bhai, ye hai no. :",x)
# # # else:
# # #     print("No, kya re")

# # # if x2:
# # #     print("Yes,mil gye re bhai  , ye hai tera email :",x2)
# # # else:
# # #     print("No, kya re")










