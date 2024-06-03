import re
while (True):

    gmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    num = r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'

    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    if re.match(gmail, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

    if re.match(num, phone_number):
        print("Valid phone number.")
    else:
        print("Invalid phone number.")
