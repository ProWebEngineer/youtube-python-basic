class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



def main():
    rectangle = Rectangle(5, 10)
    rectangle_area = rectangle.area()
    print(rectangle_area)

if __name__ == "__main__":
    main()