'''#single Inheritance
class A:
    def display1(self):
        print("Class A display method")
class B(A):
    def display2(self):
        print("Class B display method")'''

#2.multilevel inheritance
class A:
    def display1(self):
        print("Class A display method")
class B(A):
    def display2(self):
        print("Class B display method")
class C(B):
    def display3(self):
        print