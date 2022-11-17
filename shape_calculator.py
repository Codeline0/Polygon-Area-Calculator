class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for h in range(self.height):
            for w in range(self.width):
                picture += '*'
            picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        amount_inside = (self.width/shape.width) * (self.height/shape.height)
        if amount_inside < 1: 
            return 0
        return int(amount_inside)


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side 