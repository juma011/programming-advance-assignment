class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'{self.name} {self.age}')



class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("bark")


d1 = Dog("bill", 20)

d1.speak()



class Cat(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("meow")

    def show(self):
        print(f'{self.name} {self.age}')

pet = Pet("Junior", 7)

d = Dog("jim", 2)
d.show()
c = Cat("dwight", 5)
c.show()


