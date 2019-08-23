class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ",".join((str(self.x), str(self.y)))

    def __add__(self, other):
        if isinstance(other, Vector):
            total_x = self.x + other.x
            total_y = self.x + other.y
        else:
            return NotImplemented

        return Vector(total_x,total_y)