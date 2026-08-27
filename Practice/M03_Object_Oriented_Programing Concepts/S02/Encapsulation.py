''''class A:
    a=10
    _b=20
    __c=30
obj=A()
print(obj.a) 
print(obj._b)
print(obj._A__c)'''

'''
class Sample:
    def __init__(self,amount):
        self.__amount=amount
    def credit(self,value):
        self.__amount+=value
    def debit(self,value):
        self.__amount-=value
    def display(self):
        print
obj=Sample(1000)
obj.display()
obj.credit(1500)
obj.display()
obj.debit(500)
obj.display()
'''