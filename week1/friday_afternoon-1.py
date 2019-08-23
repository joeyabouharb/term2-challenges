"""
afternoon activity: vehicle class activity
"""

class Vehicle:
    """
    vehicle class
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 1
        self.capacity = 40

    def refuel(self, litres):
        self.fuel += litres

    def fuel_level(self):
        print(f'Levels: {self.fuel} / {self.capacity}')

    @property
    def is_overflow(self, litres):
        if self.fuel + litres > self.capacity:
            print("too much fuel! ")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.window_open = False

    def wind_up_windows(self):
        self.window_open = True
        print('Wound up windows!')

class Motorbike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def wheelie(self):
        print('Wheelie!')


