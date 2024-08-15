"""
3. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price. 
"""

class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add(self,n,p):
        self.items.append({'name': n, 'price': p})

    def remove(self,n):
        for x in self.items:
            if x['name' ]==n:
                self.items.remove(x)
                return
        
        print("Not found ")

    def calculate_total(self):
        tot = 0
        
        for item in self.items:
            tot += item['price']
            
        return tot



cart = ShoppingCart()
cart.add( 'a', 100)
cart.add( 'b',20)
cart.add('c',  500)

print("Total: ",cart.calculate_total( ))

cart.remove('c')
print("Total after removing item: ",cart.calculate_total())
