import unittest
from datetime import date, datetime


def get_current_date():
    current_date = datetime.now().date()
    return current_date


class TestGetCurrentDate(unittest.TestCase):
    def test_get_current_date(self):
        expected_date = date.today()
        result = get_current_date()
        self.assertEqual(result, expected_date)


if __name__ == '__main__':
    unittest.main()
