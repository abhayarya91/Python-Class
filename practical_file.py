#WAP to List Generation, operations (Repetition, concatenation, membership) and built in methods.

# num = [1, 2, 3, 4, 5]
# list2 = ['apple', 'banana', 'orange']

# repeate = num * 3
# print("Repeated numbers:", repeate)

# combined_list = num + list2
# print("Combined list:", combined_list)

# if 'apple' in list2:
#     print("Yes, 'apple' is in the member of list2.")
# else:
#     print("No, 'apple' is not in the member of list2.")




#WAP to generate Pythagorean Triplets

# def generate_pythagorean_triplets(limit):
#     triplets = []
#     for m in range(1, limit):
#         for n in range(1, m):
#             a = m**2 - n**2
#             b = 2 * m * n
#             c = m**2 + n**2
#             if c > limit:
#                 break
#             triplets.append((a, b, c))
#     return triplets

# # Example usage
# limit = 20
# triplets = generate_pythagorean_triplets(limit)
# for triplet in triplets:
#     print(triplet)




#WAP to generate star and number pattern.
# rows = 5
# rows = int(input("Enter the number of row:"))
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()


# # rows = 5
# rows = int(input("Enter the number of row:"))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()







#WAP to Reverse a Given Number.

# number = int(input("Enter a number: "))

# reversed_number = 0

# while number > 0:
#     remainder = number % 10
#     reversed_number = reversed_number * 10 + remainder
#     number = number // 10

# print("Reversed Number:", reversed_number)



# string = input("Enter string:")
# print("number of string:",len(string))



#WAP to Calculate student Grades.




#WAP to Expression Evaluation.

# def evaluate_expression(expression):
#     try:
#         result = eval(expression)
#         return result
#     except Exception as e:
#         return "Error: {}".format(e)

# expression = input("Enter the expression to evaluate: ")
# result = evaluate_expression(expression)
# print("Result:", result)




# list = [1, 2, 3, 4, 5]
# print("First element:", list[0])

# print("Slice of the list:", list[1:4])

# list.append(6)
# print("List after appending 6:", list)

# list.insert(2, 7)
# print("List after inserting 7 at index 2:", list)

# list.remove(4)
# print("List after removing element with value 4:", list)

# popped_element = list.pop(2)
# print("Popped element:", popped_element)
# print("List after popping element at index 2:", list)

# print("Length of the list:", len(list))

# list.sort()
# print("Sorted list:", list)

# list.reverse()
# print("Reversed list:", list)

# new_list = list + [7, 8, 9]
# print("Concatenated list using + operator:", new_list)

# list.extend([7, 8, 9])
# print("Extended list using extend() method:", list)



# string1 = input("Enter first String: ")
# string2 = input("Enter second String: ")

# repeated_string = string1 * 2
# print("Repeated string:", repeated_string)

# concatenated_string = string1 + " " + string2
# print("Concatenated string:", concatenated_string)

# test_string = input("Enter String to test: ")
# if test_string in string1:
#     print("'{0}' is present in '{1}'".format(test_string, string1))
# else:
#     print("'{0}' is not present in '{1}'".format(test_string, string1))





# list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# list.append(8)
# print("After appending 8:", list)

# list.extend([7, 9])
# print("After extending with [7, 9]:", list)

# list.insert(3, 0)
# print("After inserting 0 at index 3:", list)

# list.remove(1)
# print("After removing the first occurrence of 1:", list)

# popped_element = list.pop()
# print("Popped element:", popped_element)
# print("List after popping:", list)

# list.clear()
# print("After clearing the list:", list)

# new_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# index = new_list.index(5)
# print("Index of first occurrence of 5:", index)

# count = new_list.count(1)
# print("Number of occurrences of 1:", count)

# new_list.sort()
# print("Sorted list:", new_list)

# new_list.reverse()
# print("Reversed list:", new_list)

# copied_list = new_list.copy()
# print("Copied list:", copied_list)

# length = len(new_list)
# print("Length of the list:", length)








# while True:
#     def add(x, y):
#         return x + y

#     def subtract(x, y):
#         return x - y

#     def multiply(x, y):
#         return x * y

#     def divide(x, y):
#         if y == 0:
#             return "Error: Division by zero!"
#         else:
#             return x / y

#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#     else:
#         print("Invalid input")




# dict1 = {'Name':'Abhy','Class':'Cyber Security'}
# dict2 = {'age':25,'address':'Roper'}
# print("1st dctionary:",dict1)
# print("2nd dictionary:",dict2)
# marge_dict= dict1,dict2
# print("marge Dictionery:",marge_dict)
# print("type marge Dict.....",type(marge_dict))





