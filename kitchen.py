class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # general multiplication implementation
        self.amount = self.amount * multiplier