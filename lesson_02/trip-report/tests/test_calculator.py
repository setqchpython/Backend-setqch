import unittest

from app.services.calculator import (
    calculate_average,
    calculate_total,
    category_share,
    most_expensive_day,
)

EXPENSES = [
    {"day": 1, "category": "еда", "amount": 540},
    {"day": 1, "category": "транспорт", "amount": 260},
    {"day": 1, "category": "жильё", "amount": 1800},
    {"day": 2, "category": "еда", "amount": 720},
    {"day": 2, "category": "транспорт", "amount": 180},
    {"day": 2, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 430},
    {"day": 3, "category": "транспорт", "amount": 95},
    {"day": 3, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 275},
]


class TestCalculator(unittest.TestCase):
    def test_total(self):
        self.assertEqual(calculate_total(EXPENSES), 7900)

    def test_average(self):
        self.assertAlmostEqual(calculate_average(EXPENSES), 790.0)

    def test_most_expensive_day(self):
        self.assertEqual(most_expensive_day(EXPENSES), (2, 2700))

    def test_food_share(self):
        self.assertAlmostEqual(category_share(EXPENSES, "еда"), 24.87, places=2)

    def test_housing_share(self):
        self.assertAlmostEqual(category_share(EXPENSES, "жильё"), 68.35, places=2)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_most_expensive_day_empty(self):
        with self.assertRaises(ValueError):
            most_expensive_day([])

    def test_category_share_empty(self):
        with self.assertRaises(ValueError):
            category_share([], "еда")

    def test_missing_category(self):
        with self.assertRaises(ValueError):
            category_share(EXPENSES, "сувениры")


if __name__ == "__main__":
    unittest.main()
