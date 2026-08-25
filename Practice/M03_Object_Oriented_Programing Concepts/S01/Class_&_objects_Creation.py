'''class Example:
    x=100
    def display(self):
        print("This is an example class")
    def dispaly1(self):
        name="xyz" 
        print("Good morning",name)
        
obj=Example()
print(obj.x)
obj.display()
obj.dispaly1()'''
from math import pi
class Circle:
    r=7
    def area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r
c1=Circle()
print(c1.area())
print(c1.perimeter())

    



