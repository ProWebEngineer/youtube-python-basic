import unittest
from problem41 import add

class TestAdd(unittest.TestCase):
    """add関数のテストクラス"""

    def test_add_positive_numbers(self):
        """正の数の和をテスト"""
        self.assertEqual(add(2, 3), 5)
    

if __name__ == "__main__":
    unittest.main()