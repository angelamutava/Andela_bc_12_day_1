class Person:

    """This class declares the basic attributes every person has"""
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    """The student class inherits from  person and gives the student te ability to enroll to certain courses"""
    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    """This class inherits from person and checks employment type"""

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):

    """"This class inherits from  StaffMember and identiies the lectures with the courses they  teach""""
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


john = Student("John", "Doe", "xyzthf")
john.enrol("Introduction to computer programming")

angie = Lecturer("Angela", "Mutava", "29695896")
angie.assign_teaching("Mathematics for dummies")