class Dog:
    def __init__(self, name) -> None:
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
my_dog.speak()

another_dog = Dog('chitti')
another_dog.speak()