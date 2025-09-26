import unittest
from problem43 import Rectangle

class TestRectangle(unittest.TestCase):
    """Rectangleクラスのテストクラス"""

    def test_area_case1(self):
        """幅3、高さ4の長方形の面積テスト"""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
    
    def test_area_case2(self):
        """幅5、高さ6の長方形の面積テスト"""
        rect = Rectangle(5, 6)
        self.assertEqual(rect.area(), 30)
        

if __name__ == "__main__":
    unittest.main()