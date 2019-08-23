"""
a dog app
"""
import geocoder


def find_location(
        city: str
) -> str:
    """
    find geocode by city
    """
    g = geocoder.arcgis(city)
    return str(g.latlng)


def validate_int(
        user_input: str
) -> int:
    """
    cast str input to int
    """
    if user_input.isdecimal():
        try:
            val = int(user_input)
        except ValueError:
            exit()
    else:
        exit()
    return val

class Dog:
    def __init__(
            self: object,
            name: str,
            age: int,
            breed: str
    ):
        self.name = name.capitalize()
        self.age = validate_int(age)
        self.breed = breed.capitalize()
        self.places_walked = []
        self.status = "Awake"
    def bark(self):
        """
        dog barks back!
        """
        print(
            self.name +
            ' Barks loudly!'
        )

    def toString(self):
        """
        print dog details
        """
        print(
            'Name: ' + self.name +
            '\nAge: ' + str(self.age) +
            '\nBreed: ' + self.breed +
            '\nWalks: ' + str(self.total_walked) +
            '\nDistance Traveled: ' + str(self.distance_travelled)
        ) 

    def places_travelled(self):
        """
        Get all places travelled
        """
        if not self.places_walked:
            return ''
        
        for city, distance in self.places_walked:
            print(" ".join(
                (
                    "City: ",
                    city,
                    "Distance ",
                    str(distance),
                    "meters. Geolocation",
                    find_location(city)
                )
            ))


    @property
    def distance_travelled(self):
        """
        """
        if not self.places_walked:
            return ''
        total = 0
        for _, distance in self.places_walked:
            total += distance

        return total

    @property
    def total_walked(self):
        """
        """
        return len(self.places_walked)

    def walk(self, distance: int, city: str):
        """
        walk with dog
        """
        if self.age > 6 or self.total_walked > 30:
            print(self.name + ' To tired to play. need sleep (Howl! Howl!):')
        else:
            print('Yip Yip! ' + self.name  +  ' loves to walk!')
            self.places_walked.append((city, validate_int(distance)))

    def sleep(self):
        """
        dog sleeps now, exit app
        """
        self.status = "Sleep"

    def ask_for_help(self):
        """
        dog will tell you what it can do
        """
        print('Bark! Bark! Bark!')
        print( '(Walk), (Details), (Bark)')

def main():
    doggo = Dog(
        input('Dog name: '),
        input('Age: '),
        input('Breed: ')
    )
    while doggo.status == 'Awake':
        command = input(doggo.name + ' is waiting for instruction. (Bark!): ').lower()

        if command == 'walk':
            doggo.walk(
                input('How far we walk? (Bark! Bark?): '),
                input('Where? ')    
            )
        elif command == 'details':
            doggo.toString()
        elif command == 'bark':
            doggo.bark()
        elif command == 'sleep':
            doggo.sleep()
        elif command == 'travels':
            doggo.places_travelled()
        else:
            doggo.ask_for_help()
if __name__ == "__main__":
    main()