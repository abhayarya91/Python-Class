class father:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    def sum(self):
        print("addition",self.num1+self.num2)
    def sub(self):
        print("subtraction",self.num1-self.num2)  
class child1(father):
    def mult(self):
        print("multiplication",self.num1*self.num2)
    def dev(self):
        print("division",self.num1/self.num2)
class child2(child1):
    def rem(self):
        print("remender",self.num1%self.num2)
obj = child2()
obj.sum()
obj.sub()
obj.mult()
obj.dev()
obj.rem() 
