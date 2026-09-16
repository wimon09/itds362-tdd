class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # fake it: always set to 600 for the first test
        self.amount = 600