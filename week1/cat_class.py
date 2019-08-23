class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
         print(self.name +  'meows and is feline good!')

    def feed_cat(self):
        print(self.name + 'purs and thanks for your pawtronage!')

def main():
    cat = Cat(
        'Felix'
    )

main()