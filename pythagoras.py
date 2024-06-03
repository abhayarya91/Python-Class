# limite = int(input("Enter the range:"))
# c = 0 
# m = 2 
# for n in range (1, m+1):
#     a = m ** 2 - n ** 2
#     b = 2 * m * n
#     c = m ** 2 + m ** 2 
#     if c > limite:
#         break
#     if a = 0 or b = 0 or c = 0:
#         break
#     print(a, b, classmethod)





limit = int(input("Enter the range: "))
a = 0
b = 0
c = 0
for m in range(1, limit):
    for n in range(m + 1, limit):
        a = n ** 2 - m ** 2
        b = 2 * m * n
        c = n ** 2 + m ** 2
        if c > limit:
            break
        if a == 0 or b == 0 or c == 0:
            break
    if c > limit:
        break
    if a == 0 or b == 0 or c == 0:
        break
print("Pythagorean Triple:", a, b, c)
