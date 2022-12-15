import random

# List of available options
bases = ["regular", "cronut", "chocolate filled", "cream filled"]
toppings = ["chocolate", "strawberry", "glazed", "rainbow", "no topping"]
extras = ["cream", "ice cream", "melted chocolate", "rainbow flakes"]

# Donut class
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
        
# Choose custom options donut
    def choose_donut_options(self):
        print("*** Donut bases ***")
        for i, base in enumerate(bases):
            print(f"{i+1}. {base}")
        choice = input("Enter the number of your choice: ")
        self.base = bases[int(choice) - 1]

        print("*** Donut toppings ***")
        for i, topping in enumerate(toppings):
            print(f"{i+1}. {topping}")
        choice = input("Enter the number of your choice: ")
        self.topping = toppings[int(choice) - 1]

        print("*** Donut extras ***")
        for i, extra in enumerate(extras):
            print(f"{i+1}. {extra}")
        choice = input("Enter the number of your choice: ")
        self.extra = extras[int(choice) - 1]
    
my_donut = Donut()

feeling_lucky = input("Are you feeling lucky? (y/n)")
if feeling_lucky.lower() == "y":
    print("Fortune smiles at the brave. Enjoy the donut.")
    my_donut.generate_random_donut()
else:
    my_donut.choose_donut_options()

# Print donut
if my_donut.topping == "no topping":
    print(f"Your donut has a {my_donut.base} base, has {my_donut.topping}, and has {my_donut.extra} as an extra.")
elif my_donut.topping == "rainbow" and my_donut.extra == "rainbow flakes":
    print("Wow, a Unicorn donut!")
    print(f"Your donut has {my_donut.topping} topping and {my_donut.extra} to match... that's pretty. Your base is {my_donut.base}.")
    print("                    /")
    print("               ,.. /")
    print("             ,'   ';")
    print("  ,,.__    _,' /';  .")
    print(" :','  ~~~~    '. '~")
    print(":' (   )         )::,")
    print("'. '. .=----=..-~  .;'")
    print(" '  ;'  ::   ':.  '""")
    print("   (:   ':    ;)")
    print("Unicorn Ascii art by 'DR J' https://www.asciiart.eu/mythology/unicorns")
else:
    print(f"Your donut has a {my_donut.base} base, is topped with {my_donut.topping}, and has {my_donut.extra} as an extra.")