import random
from art import *
from extra.donutart import *
import unittest

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

# Write the donut to a file
    def write_donut(self):
        with open('donuts.txt', 'w') as file:
            file.write(str(self.base) + '\n')
            file.write(str(self.topping) + '\n')
            file.write(str(self.extra) + '\n')
            file.truncate(file.tell() - 1)  # truncate the file to the current position

# Read the last donut from file
    def read_donut(self):
        with open('donuts.txt', 'r') as file:
            self.base = file.readline().strip()
            self.topping = file.readline().strip()
            self.extra = file.readline().strip()
            
# Serve the donut
    def serve_donut(self):
        if my_donut.topping == "no topping":
            donut_image()
            print(f"Your donut has a {my_donut.base} base, has {my_donut.topping}, and has {my_donut.extra} as an extra.")
        elif my_donut.topping == "rainbow" and my_donut.extra == "rainbow flakes":
            print("Wow, a Unicorn donut!")
            unicorn_image()
            print(f"Your donut has {my_donut.topping} topping and {my_donut.extra} to match... that's pretty. Your base is {my_donut.base}.")
        elif my_donut.topping == "None":
            print("You have never had a lucky donut.")
        else:
            donut_image()
            print(f"Your donut has a {my_donut.base} base, is topped with {my_donut.topping}, and has {my_donut.extra} as an extra.")
       
# Navigation menu     

def welcome_message():
    print("--------------------------")
    print("Welcome To...")
    tprint("Lucky Donuts!")
        
# Nav - User selections
def integer_menu():
    while True:
        try:
            my_donut.read_donut()
            print("Welcome to Lucky Donuts. What would you like?")
            if my_donut.base == "":
                print("1. Let me choose my own donut options for base, topping and extras")
                print("2. I'm feeling lucky!")
                menu_option = int(input("Enter your choice:"))
                if menu_option == 1:
                    print("You donut have to feel lucky all the time!")
                    print("Choose your own options for your donut.")
                    my_donut.choose_donut_options()
                    break
                elif menu_option == 2:
                    print("Fortune favors the brave. Enjoy the donut.")
                    my_donut.generate_random_donut()
                    break
            else:
                print("1. Let me choose my own donut options for base, topping and extras")
                print("2. I'm feeling lucky!")
                print(f"3. Repeat the last donut. Base: {my_donut.base.title()}, Topping: {my_donut.topping.title()}, Extra: {my_donut.extra.title()}")
                menu_option = int(input("Enter your choice:"))
                if menu_option == 1:
                    print("You donut have to feel lucky all the time!")
                    print("Choose your own options for your donut.")
                    my_donut.choose_donut_options()
                    break
                elif menu_option == 2:
                    print("Fortune smiles at the brave. Enjoy the donut.")
                    my_donut.generate_random_donut()
                    break
                elif menu_option == 3:
                    my_donut.read_donut()
                    break
            print("Please enter a valid choice as a number corresponding to the selection.")
        except ValueError:
            print("Please enter a valid choice as a number corresponding to the selection.")
    
            
# Testing the donut

class TestDonut(unittest.TestCase):
    def test_generate_random_donut(self):
        # Create a new Donut object
        test_random_donut = Donut()
        
        # Generate a random donut
        test_random_donut.generate_random_donut()
        
        # Check that the base is in the list of available bases
        self.assertIn(test_random_donut.base, bases)
        
        # Check that the topping is in the list of available toppings
        self.assertIn(test_random_donut.topping, toppings)
        
        # Check that the extra is in the list of available extras
        self.assertIn(test_random_donut.extra, extras)
        
    def test_read_donut(self):
        # Create a new Donut object
        test_read_donut = Donut()
        
        # Write some test data to the 'donuts.txt' file
        with open('donuts.txt', 'w') as file:
            file.write('test\n')
            file.write('test\n')
            file.write('test\n')
        
        # Read the donut from the 'donuts.txt' file
        test_read_donut.read_donut()
        
        # Check that the base is correct
        self.assertEqual(test_read_donut.base, 'test')
        
        # Check that the topping is correct
        self.assertEqual(test_read_donut.topping, 'test')
        
        # Check that the extra is correct
        self.assertEqual(test_read_donut.extra, 'test')

#  Uncomment the code below to perform tests

# if __name__ == '__main__':
#     print("Testing: 1. Random donut generator is generating options from selections")
#     print("Testing: 2. Testing read and write to file")
#     unittest.main()

# Beep boop - initialising the donut
my_donut = Donut()

# Welcome message
welcome_message()

# Menu options
integer_menu()

# Serves the donut
my_donut.serve_donut()

# Writes the current donut to a text file
my_donut.write_donut()
