from abc import ABC, abstractmethod

class shape (ABC):
    @abstractmethod
    def area (self):
        pass

class retangel(shape):
    def area(self):
        return self.length * self.width

    def __init__(self,length,width):
        self.length = length
        self.width = width


r= retangel(7,3)
print(r.area())








     