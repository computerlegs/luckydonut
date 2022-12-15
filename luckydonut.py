import random

# List of available options
bases = ["regular", "cronut", "chocolate filled", "cream filled"]
toppings = ["chocolate", "strawberry", "glazed", "rainbow", "no topping"]
extras = ["cream", "ice cream", "melted chocolate", "rainbow flakes"]

class Donut:
    def __init__(self):
        self.base = None
        self.topping = None
        self.extra = None
        
# Random donut
    def generate_random_donut(self):
        self.base = random.choice(bases)
        self.topping = random.choice(toppings)
        self.extra = random.choice(extras)

    
my_donut = Donut()
my_donut.generate_random_donut()

# Print donut
print(f"Your donut has a {my_donut.base} base, is topped with {my_donut.topping}, and has {my_donut.extra} as an extra.")