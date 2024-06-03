import random 
print("your random number1:",random.randint(2,10))
print("your random number2:",random.randrange(3,9))

l = ["Abhay","Arya","saurya","Moon"]
print("your choice:",random.choice(l))

#.....................................function random
r = random.random()
print(r)

#.....................................function shuffle
l = [10,20,30,40,50,60,70,80,90]
random.shuffle(l)
print(l)

#.....................................function uniform
u = random.uniform(3,9)
print(u)
