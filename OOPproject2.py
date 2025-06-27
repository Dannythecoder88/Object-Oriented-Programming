class Menuitem:

    def __init__(self, name, category, price):
        self.name= name
        self.category = category
        self.price= price

    def apply_discount(self):
        self.pay = int(self.price * self.discount_amt)

class Order:

    def __init__(self, order_number, status):
        self.order_number= order_number
        self.items= []
        self.status= status

    def add_item(self, menu_item):
            self.items.append(menu_item)


    def remove_items(self, menu_item):
        if menu_item in self.items:
            self.items.remove(menu_item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
    def print_receipt(self):
        #Allows me to make an order numver
        print("Order number", self.order_number)
        print("Items:")
        for item in self.items:
            print(item.name, ":", item.price)
        print("Total:", self.get_total())
        
    
class DiscountedMenuItem(Menuitem):
    def __init__(self, name, category, price):
        super().__init__(name, category, price)
        self.discount_rate = 0.1

    def get_discounted_price(self):
        return self.price * (1 - self.discount_rate)
    
burger = Menuitem("Burger", "Beef", 5.0)
fries = Menuitem("Fries", "Side", 2.0)
soda = DiscountedMenuItem("Soda", "Drink", 2.0)
print("Discounted Soda Price:", soda.get_discounted_price())
order1 = Order(1, "In Progress")
order1.add_item(burger)
order1.add_item(fries)
order1.add_item(soda)
order1.print_receipt()
order1.remove_items(fries)
order1.print_receipt()
