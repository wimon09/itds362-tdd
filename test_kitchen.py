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

from kitchen import Quantity


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
