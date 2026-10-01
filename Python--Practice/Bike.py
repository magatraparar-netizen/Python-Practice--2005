from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class bike(Vehicle):
    def __init__(self,name):
        self.name = name 


    
    def start(self):
        return self.name + " Start"


b= bike("honda")
print(b.start())

     