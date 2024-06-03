print("Enter the marks obtained in each subject out of 100")
python = int(input("Enetr your marks in Python: "))
DSA = int(input("Enet your marks in DSA: "))
CSF = int(input("Enter your marks in CSF: "))
DT = int(input("Enter your marks in DT: "))
EEE = int(input("Enter your marks in EEE: "))
DM = int(input("Enter your marks in Discrete mathematics: "))
Stats= int(input("Enter your marks in Statistics: "))
total = python+DSA+CSF+DT+EEE+DM+Stats
print("Total Makrs=",total)
percentage = round((total/700)*100)
print("Percentage = ",percentage)
if percentage >=95:
  print("You got grade A1")
elif 95 > percentage >= 85:
  print("You got grade A2")
elif 85 > percentage >= 75:
  print("You got grade B1")
elif 75 > percentage >= 65:
  print("You got grade B2")
elif 65> percentage >= 55:
  print("You got grade C1")
elif 55 > percentage >= 45:
  print("You got grade C2")
else:
  print("You have to do mare efforts....")