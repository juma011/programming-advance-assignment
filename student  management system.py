class Student:
    def __init__(self, name, age, grade, backlog):
        self.name = name
        self.age = age
        self.grade = grade
        self.backlog = backlog

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [s1, s2, s3, s4, s5]

    def add_students(self, student):
        if(len(self.students) < self.max_students):
            self.students.append(student)
            return True
            return False

    def avg_grade(self):
        value = 0
        for s in self.students:
            value = value + s.get_grade()

        return value / len(self.students)

    def add_num(self, string):
        print(string + "hello")



s1 = Student("Ravi", 21, 84, 2)
s2 = Student("Shyam", 21, 89, 0)
s3 = Student("Ram", 21, 59, 1)
s4 = Student("Riddhi", 20, 94, 0)
s5 = Student("Anirudh", 21, 90, 1)
c1 = Course("Aerospace", 5)



print(s1.__dict__)
print(s2.__dict__)
print(c1.__dict__)
print(c1.avg_grade())









