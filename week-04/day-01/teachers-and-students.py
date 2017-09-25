# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Student(object):
    def learn(self):
        pass
    def question(self):
        Teacher.answer(self)

class Teacher(object):
    def answer(self):
        pass
    def teasch(self):
        Student.learn(self)
