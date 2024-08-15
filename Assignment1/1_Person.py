"""
1. Write a Python program to create a person class. Include attributes  like name, country and date of birth. 
Implement a method to  determine the person’s age. 
"""

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def calculate_age(self):
        today = datetime.today()
        if((today.month, today.day) < (self.dob.month, self.dob.day)):
            age = today.year - self.dob.year -1
        else:
            age = today.year - self.dob.year
        return age

person = Person("Abc", "India", "2004-05-15")
print("Name:", person.name)
print("Age: ",person.calculate_age())
print("Country: ",person.country)