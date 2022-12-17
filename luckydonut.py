import random

# Welcome to Lucky Donuts!
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


# Print ASCII donut
def donut_image():
    print("")
    print("⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠄⠀⠒⠂⢀⡤⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⡀⠔⢈⠀⠀⡿⠀⢀⣤⡄⠈⠋⢁⣀⠀⢈⡒⢄⠀⠀⠀⠀")
    print("⠀⠀⣠⠊⣁⡀⠉⠋⠀⣦⠀⠀⠁⢀⠀⠀⠀⠛⠀⠘⠃⣄⠑⢄⠀⠀")
    print("⠀⡔⡁⠀⠉⢁⣄⠄⠀⠈⠀⣶⠀⠈⠛⠀⣠⠄⠶⠦⠀⠑⠀⢬⣧⠀")
    print("⡐⠀⠿⢠⢄⠀⣀⠀⠀⡠⠄⠠⠔⠉⠢⡀⠉⠀⠀⢀⣴⠆⠀⠈⠁⢣")
    print("⠃⣤⠄⠀⢁⣄⠙⠀⠘⠀⡠⠒⠉⠉⠒⢄⠉⢢⠀⠀⢀⡀⠟⠃⢴⡤")
    print("⡀⠀⢔⡀⠈⠋⠠⢄⠰⡜⠀⠀⠀⠀⠀⠀⠱⡜⢠⡤⠈⠛⠁⢀⣄⢀")
    print("⡇⠀⣀⡀⠀⠀⠀⠉⠀⠘⠢⣀⠀⠀⠀⡠⠊⢀⠈⠀⠀⢸⡄⠈⠁⢸")
    print("⠀⠸⡐⠂⠤⢀⠀⢶⠀⠀⣈⡀⠀⢈⡅⠈⠘⡁⠀⠶⠅⡀⠠⠒⡙⠀")
    print("⠀⠀⠐⡄⠀⠀⠱⡀⠀⠀⠉⢁⡠⢏⠁⠀⠚⠁⠀⢠⠊⠀⢀⠜⠀⠀")
    print("⠀⠀⠀⠈⠢⠀⠀⠈⠒⠀⠂⠁⠀⠀⠉⠂⠤⠤⠐⠁⢀⠴⠋⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠈⠑⠠⢄⡀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠂⠁⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")               

# Print ASCII unicorn
def unicorn_image():
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

# List of available options
bases = ["regular", "cronut", "chocolate filled", "custard filled"]
toppings = ["chocolate", "strawberry", "glazed", "rainbow", "no topping"]
extras = ["whipped cream", "ice cream", "melted chocolate", "rainbow flakes"]

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

# choose base option
    def base_options(self):
        print("*** Donut bases ***")
        for i, base in enumerate(bases):
            print(f"{i+1}. {base}")
        try:
            while True:
                choice = input("Enter the number of your choice: ")
                if int(choice) == 0:
                    print("Invalid choice. Please enter a valid number that is not 0.")
                    for i, base in enumerate(bases):
                        print(f"{i+1}. {base}")
                else:
                    self.base = bases[int(choice) - 1]
                    break   
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")  
            self.base_options()
            
# choose topping option            
    def topping_options(self):
        print("*** Donut toppings ***")
        for i, topping in enumerate(toppings):
            print(f"{i+1}. {topping}")
        try:
            while True:
                choice = input("Enter the number of your choice: ")
                if int(choice) == 0:
                    print("Invalid choice. Please enter a valid number that is not 0.")
                    print("*** Donut toppings ***")
                    for i, topping in enumerate(toppings):
                        print(f"{i+1}. {topping}")
                else:
                    self.topping = toppings[int(choice) - 1]
                    break   
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")  
            self.topping_options()
     
# choose extra option        
    def extra_options(self):
        print("*** Donut extra ***")
        for i, extra in enumerate(extras):
            print(f"{i+1}. {extra}")
        try:
            while True:
                choice = input("Enter the number of your choice: ")
                if int(choice) == 0:
                    print("Invalid choice. Please enter a valid number that is not 0.")
                    print("*** Donut extras ***")
                    for i, extra in enumerate(extras):
                        print(f"{i+1}. {extra}")
                else:
                    self.extra = extras[int(choice) - 1]
                    break   
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")  
            self.extra_options()
        
# Choose custom options donut
    def choose_donut_options(self):
        self.base_options()
        self.topping_options()
        self.extra_options()

# Write the lucky donut to a file
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
    print("Fortune smiles at the brave. Enjoy the donut.")
    donut_image()
    my_donut.generate_random_donut()
else:
    print("You donut have to feel lucky all the time!")
    print("What do you want instead?")
    print("1. Let me choose my own options for base, topping and extras")
    print("2. I'll repeat the last donut")
    while True:
        old_nut_or_specific_nut = int(input("Enter your choice:"))
        old_nut_or_specific_nut = int(old_nut_or_specific_nut)
        if old_nut_or_specific_nut == 1:
            my_donut.choose_donut_options()
            break
        elif old_nut_or_specific_nut == 2:
            my_donut.read_donut()
            break
        print("Please enter a valid choice (1 or 2)")

# Writes the current donut to a text file
my_donut.write_donut()

# Serves the donut
if my_donut.topping == "no topping":
    print(f"Your donut has a {my_donut.base} base, has {my_donut.topping}, and has {my_donut.extra} as an extra.")
elif my_donut.topping == "rainbow" and my_donut.extra == "rainbow flakes":
    print("Wow, a Unicorn donut!")
    unicorn_image()
    print(f"Your donut has {my_donut.topping} topping and {my_donut.extra} to match... that's pretty. Your base is {my_donut.base}.")
elif my_donut.topping == "None":
    print("You have never had a lucky donut.")
else:
    print(f"Your donut has a {my_donut.base} base, is topped with {my_donut.topping}, and has {my_donut.extra} as an extra.")