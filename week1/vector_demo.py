
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ", ".join((str(self.x), str(self.y)))

    def __add__(self, other):
        if isinstance(other, Vector):
            total_x = self.x + other.x
            total_y = self.x + other.y
        else:
            return NotImplemented

        return Vector(total_x,total_y)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            total_x = self.x * other
            total_y = self.y * other
            return Vector(total_x, total_y)
        else:
            return NotImplemented

    def __len__(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def __iter__(self):
        return iter([self.x, self.y])

