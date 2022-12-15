import random

# Welcome to Lucky Donuts!
print("                             Welcome to Lucky Donuts intro font by JK - https://patorjk.com")
print("")
print("                                 _                    _       ")
print("                     __ __ _____| |__ ___ _ __  ___  | |_ ___ ")
print("                     \ V  V / -_) / _/ _ \ '  \/ -_) |  _/ _ \ ")
print("                      \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ ")
print(" ___     __   __ _______ ___   _ __   __   ______  _______ __    _ __   __ _______ _______ ")
print("|   |   |  | |  |       |   | | |  | |  | |      ||       |  |  | |  | |  |       |       |")
print("|   |   |  | |  |       |   |_| |  |_|  | |  _    |   _   |   |_| |  | |  |_     _|  _____|")
print("|   |   |  |_|  |       |      _|       | | | |   |  | |  |       |  |_|  | |   | | |_____ ")
print("|   |___|       |      _|     |_|_     _| | |_|   |  |_|  |  _    |       | |   | |_____  |")
print("|       |       |     |_|    _  | |   |   |       |       | | |   |       | |   |  _____| |")
print("|_______|_______|_______|___| |_| |___|   |______||_______|_|  |__|_______| |___| |_______|")
print("")


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
        print("")
        for i, base in enumerate(bases):
            print(f"{i+1}. {base}")
        print("")
        try:
            choice = input("Enter the number of your choice: ")
# If user enters a 0 - not working. probably def each choice
            if int(choice) == 0:
                print("Cannot select 0. Please enter a valid number.")
            else:
                self.base = bases[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
            self.choose_donut_options()

        print("*** Donut toppings ***")
        print("")
        for i, topping in enumerate(toppings):
            print(f"{i+1}. {topping}")
        print("")
        try:
            choice = input("Enter the number of your choice: ")
            self.topping = toppings[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
            self.choose_donut_options()

        print("*** Donut extras ***")
        print("")
        for i, extra in enumerate(extras):
            print(f"{i+1}. {extra}")
        print("")
        try:
            choice = input("Enter the number of your choice: ")
            self.extra = extras[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
            self.choose_donut_options()

# Write the last lucky donut to a file
    def write_donut(self):
        with open('donuts.txt', 'w') as file:
            file.write(str(self.base) + '\n')
            file.write(str(self.topping) + '\n')
            file.write(str(self.extra) + '\n')
            file.truncate(file.tell() - 1)  # truncate the file to the current position

# Read the last lucky donut from file
    def read_donut(self):
        with open('donuts.txt', 'r') as file:
            self.base = file.readline().strip()
            self.topping = file.readline().strip()
            self.extra = file.readline().strip()

# Beep boop - initialising the donut
my_donut = Donut()

# Asks the user if they are feeling lucky and a) generates lucky donut b) lets them choose between their last donut or a custom donut
feeling_lucky = input("Are you feeling lucky? (y/n)")
if feeling_lucky.lower() == "y":
    print("")
    print("Fortune smiles at the brave. Enjoy the donut.")
    my_donut.generate_random_donut()
else:
    print("")
    print("You donut have to feel lucky all the time!")
    print("")
    wants_previous = input("Do you want your last donut again? (y/n)")
    if wants_previous.lower() == "y":
        my_donut.read_donut()
    else:
        my_donut.choose_donut_options()

# Writes the current donut to a text file
my_donut.write_donut()

# Serves the donut
if my_donut.topping == "no topping":
    print("")
    print(f"Your donut has a {my_donut.base} base, has {my_donut.topping}, and has {my_donut.extra} as an extra.")
elif my_donut.topping == "rainbow" and my_donut.extra == "rainbow flakes":
    print("")
    print("Wow, a Unicorn donut!")
    print("")
    print("                    /")
    print("               ,.. /")
    print("             ,'   ';")
    print("  ,,.__    _,' /';  .")
    print(" :','  ~~~~    '. '~")
    print(":' (   )         )::,")
    print("'. '. .=----=..-~  .;'")
    print(" '  ;'  ::   ':.  '""")
    print("   (:   ':    ;)")
    print("")
    print(f"Your donut has {my_donut.topping} topping and {my_donut.extra} to match... that's pretty. Your base is {my_donut.base}.")
    print("")
    print("Unicorn Ascii art by 'DR J' https://www.asciiart.eu/mythology/unicorns")
elif my_donut.topping == "None":
    print("You have never had a lucky donut.")
else:
    print("")
    print(f"Your donut has a {my_donut.base} base, is topped with {my_donut.topping}, and has {my_donut.extra} as an extra.")