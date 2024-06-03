class car:
    def __init__(self,make, model):
        self.make = make 
        self.model = model
    def drive (self):
           return f"{self.make} {self.model} is driveng"
my_car = car ("toyota", "camry")
print (my_car.drive()) 
      