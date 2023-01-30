class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
        print(self.count)
    @classmethod
    def number_of_popilation(cls):
        print(cls.count)

person1 = Person("아이유")
person2 = Person("이찬혁")

Person.number_of_popilation()
person1.number_of_popilation()
person2.number_of_popilation()