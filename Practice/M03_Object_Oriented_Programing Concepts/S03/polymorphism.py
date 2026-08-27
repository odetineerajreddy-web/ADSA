'''Types of polymorphism
1.compile-time 
    1.Function overloading
    2.Operator overloading
2.Runtime 
    1.method overloading'''

'''def add(x,y):
    return x+y 
def add(x,y,z):
    return x + y + z 
def add(x,y,z,a):
    return x+y+z+a 
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))'''

'''
Python does not support Function overloading directly we can achieve this variable length arguments
'''

'''def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))'''

#Operator Overloading
class Add:
    def __init__(self,x):
        self.x=x
    def __add__(self,val):
        return self.x + val.x

a = Add(10)
b = Add(20)
print(a+b)
print(a-b)