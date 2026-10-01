from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def __init__(self, name):
        self.name = name

    def start(self):
        return self.name + " Started"


c = Car("BMW")
print(c.start())


    
            