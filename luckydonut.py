# List of available options
bases = ["regular", "cronut", "chocolate filled", "cream filled"]
toppings = ["chocolate", "strawberry", "glazed", "rainbow", "no topping"]
extras = ["cream", "ice cream", "melted chocolate", "rainbow flakes"]

class Donut:
  def __init__(self):
    self.base = None
    self.topping = None
    self.extra = None
    self.price = None