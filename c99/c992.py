class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6,{"science":4} )
jane = Student("Jane", 12, "female", 6, {"science":2,"math":4})
divij=Student("Divij",14,"male",7,{"math":2})
# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())
print(divij.getGPA())