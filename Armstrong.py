#WAP to check a number is armgstrong input from usesr
while True:
    number = int(input("Enter a number: "))
    num_digits = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    if number == sum:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")
