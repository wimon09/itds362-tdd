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
        return Sum(self, other)


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
        # delegate to the source's reduce method if it has one
        if hasattr(source, 'reduce'):
            return source.reduce(self, to_unit)
        return source


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, converter, to_unit):
        # not implemented yet — this will make the tests go red until implemented
        raise NotImplementedError