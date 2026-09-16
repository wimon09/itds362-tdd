"""
Test list
☐ 200 g × 3 = 600 g
☐ multiplying a quantity does not modify the original
☐ two quantities with the same amount and unit are equal
☐ 1 oz is not the same as 1 g
☐ 200 g + 300 g = 500 g
☐ 200 g + 1 oz, reduced to grams, using a conversion rate
☐ (200 g + 1 oz) × 2
"""

from kitchen import Quantity, grams, ounces, Converter


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_addition_with_conversion():
    total = grams(200).plus(ounces(1))
    converter = Converter()
    converter.add_rate("oz", "g", 28.349523125)
    assert converter.reduce(total, "g") == grams(200 + 28.349523125)
