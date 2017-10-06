class Car():
    gas_level = 0
    def __init__(self,gas_level):
        self.gas_level = gas_level
        
    
    
    def add_gas(self,gas_level):
        return 13 - self.gas_level
    def fill_up(self):
        if(self.add_gas(self.gas_level)<= 0):
            return 0
        else:
            return self.add_gas(self.gas_level)
       