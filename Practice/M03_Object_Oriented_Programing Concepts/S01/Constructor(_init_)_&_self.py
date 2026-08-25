'''from math import pi
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r
c=Circle(7)
c1=Circle(10)
c2=Circle(15)
print(c.area())
print(c.perimeter())
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())
'''

#1603. Design Parking System
'''class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small
        
    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>=1:
                self.big-=1
                return True
        if carType==2:
            if self.medium>=1:
                self.medium-=1
                return True
        if carType==3:
            if self.small>=1:
                self.small-=1
                return True
        return False'''

#another approach
'''class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots =[0,big, medium, small]
    def addCar(self, carType: int) -> bool:
        if self.slots[carType]>=1:
            self.slots[carType]-=1
            return True
        return False'''
