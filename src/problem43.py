class Rectangle:
    """長方形クラス"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """面積を計算して返すメソッド"""
        return self.width * self.height