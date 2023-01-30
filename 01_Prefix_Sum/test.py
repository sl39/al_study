class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print('댕댕')

    def __del__(self):
        Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(cls):
        print(cls.num_of_dogs, cls.birth_of_dogs)

a = Doggy("a","b")
print(a.num_of_dogs)
print(a.birth_of_dogs)
del a
print(Doggy.get_status())