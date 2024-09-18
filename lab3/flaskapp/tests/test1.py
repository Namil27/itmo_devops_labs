import unittest
from datetime import date
from ..app import get_current_date


class TestGetCurrentDate(unittest.TestCase):
    def test_get_current_date(self):
        expected_date = date.today()
        result = get_current_date()
        self.assertEqual(result, expected_date)


if __name__ == '__main__':
    unittest.main()
