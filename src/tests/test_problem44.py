import unittest
from problem44 import divide

class TestDivide(unittest.TestCase):
    """divide関数のテストクラス"""

    def test_normal_division(self):
        """通常の除算のテスト"""
        self.assertEqual(divide(10, 2), 5.0)

    def test_division_by_zero(self):
        """0で割った場合の例外テスト"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()