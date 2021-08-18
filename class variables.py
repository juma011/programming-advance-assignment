class Person:

    number_of_person = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people = Person.number_of_person + 1
    def add(self):
        print("add method")

    def get_num_of_ppl(cls):
        return cls.number_of_people

p = Person("jim")
p1 = Person("jack")
p2 = Person("dwight")

print(Person.number_of_people)

