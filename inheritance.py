class father:
    #properties 
    def lands(self):
        print("Having 40 ekar lands")
    
class son(father):
    #properties
    def money(self):
        print("having 10 lakhs money")
  
s = son()
s.lands()
s.money()        
