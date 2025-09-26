import unittest
from problem42 import is_even

class TestIsEven(unittest.TestCase):
    """is_even関数のテストクラス"""

    def test_is_even_with_even_number(self):
        """偶数のテスト"""
        self.assertTrue(is_even(2))

    def test_is_even_with_odd_number(self):
        """奇数のテスト"""
        self.assertFalse(is_even(3))


if __name__ == "__main__":
    unittest.main()