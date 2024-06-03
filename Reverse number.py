#Write a python program to reverse number.
def reverse_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_number = int(reversed_str)
    return reversed_number

number_to_reverse = int(input("Enter a number to reverse: "))
reversed_result = reverse_number(number_to_reverse)
print(f"The reversed number of {number_to_reverse} is {reversed_result}.")


# # Take input from the user
# num = input("Enter a number: ")
# print("Reversed number:", num[::-1])
