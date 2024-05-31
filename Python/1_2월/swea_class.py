class Student:
    def __init__(self, name):
        self.name = name
        print(self.name)


class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
        print(self.name, self.major)


student = Student("홍길동")
g_student = GraduateStudent("이순신", "컴퓨터")