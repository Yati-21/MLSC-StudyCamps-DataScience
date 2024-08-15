"""
4. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
"""
class Calculator:
    def __init__(self):
        pass
    
    def add(self, a,b):
        return a +b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a, b):
        if b ==0:
            print("division by zero")
        else:
            return a / b


a =Calculator()
print(a.add(10,20))
print(a.subtract(1,4))
print(a.multiply(7,10))
print(a.divide(8,2))
