class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # return a new Quantity instead of mutating
        return Quantity(self.amount * multiplier)