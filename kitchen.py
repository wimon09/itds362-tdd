class Quantity:
    def __init__(self, amount, unit="g"):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Quantity):
            return NotImplemented
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"

    def plus(self, other):
        # fake it for initial green: assume same unit and return concrete Quantity
        return Quantity(self.amount + other.amount, self.unit)


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


class Converter:
    def __init__(self):
        self._rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        self._rates.setdefault(from_unit, {})[to_unit] = rate

    def reduce(self, source, to_unit):
        # fake: assume source already in desired unit or is a Quantity
        return source