#..............................................................................SME DAY-1..................................................................

# stack = [ ]
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# stack.append('e')
# #stack
# print(stack)

# #stack.pop('a')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)

# stack = ['a','b','c','d','e']
# print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# print(stack)

# l = ["abhay","arya",'a','b','h','a','y','r','s','n']
# print(list[5])






# **Data structures,GUI and CGI**

# **QUEUE** is curculer motion.....FIFO....first in first out
# exaple: apply pop()
# 5 4 3 2 1 0
#   4 3 2 1 0
#     3 2 1 0
#       2 1 0
#         1 0
#           0
# **SCTACK** in linear motion......LIFO....last in first out....close at one end and close at one end
# example: apply pop()
#  5 4 3 2 1
#    4 3 2 1
#      3 2 1
#        2 1
#          1

# push()= insertion
# pop()= deletion

# **LINKED LIST**
# 1: Singly linked list
# 2: duably linked list

# **DATA STRUCTURE TYPE**
# 1: Primitive data structure
# 2: Non-primitive data structure

# stack = []
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# print(stack)
# stack.pop()
# print(stack)

#..........................................................................SME DAY-2.............................................................

# queue = []
# queue.append('a')
# queue.append('b')
# queue.append('c')
# queue.append('d')
# print(queue)
# queue.pop(0)
# print(queue)




#.............................................................................LIST COMPREHENSIONS
#syntex:::::: nuew_list=[expression(elements) for elemets in old_list if condition]
# Parameter: expression,element,itrable,condition,return



# number = [2,4,6,8,10]
# print("Original Number:",number)
# list=[]
# for num in number:
#     list.append(num*num)
# print("new List:",list)



# num = [1,2,3,4,5,6,7,8,9]
# squared = [x**2 for x in num]
# print(squared)


# list = [character for character in [1,2,3]]
# print(list)


# list=[i for i in range(11)if i % 2 == 0]
# print(list)


# list=[i for i in range(11)if i % 3 == 0]
# print(list)


# list = []
# for character in 'tradintioinal approch':
#     list.append(character)
# print(list)    

# list=[character for character in 'comprehension approch']
# print(list)



#...................................................................NESTED COMPREHENSION............................................................
# Nested list comrehension are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.



# matrix =[]
# for i in range(3):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(j)
#print(matrix)        




#........................................................DICTIONARY COMPREHENSION.............................................................

d = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}
# input("Enter a number (0 to 7) to print day:")
# for i in range(0,7):
#     print(d)

print({k:v} for (k,v) in d )
