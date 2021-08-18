class Dog:
    pass
class Dog:
    def speak(self):
        print("bark")
    def walk(self):
        print("walk")

d = Dog()
print(d.walk())

d2 = Dog()
print(d2.walk())

d.name = "jim"
d2.name = "dwight"
print(d2.name)
d.age = 30
d2.age = 35

print(type(d))

def speak():
    print('speak')

d1 = 20
d2 = 60
print(d2/10)

class Dog:
    def bark(self):
        print("bark")
    def set_breed(self, breed):
        self.breed = breed
    def get_breed(self):
        return self.breed

d = Dog()
print(d.bark())

d.set_breed("german shepherd")
print(d.get_breed())

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

d = Dog("Micheal", 20, "brown" )
print(d.color)
print(d.age)
print(d.name)











