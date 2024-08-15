""" 
Implement a School Management System

Requirements:
Implement classes for Person, Student, Teacher, Course, and School.
Person should be a base class with attributes like name and age.
Student and Teacher should inherit from Person and add specific attributes/methods.
Course should have attributes like course_id, name, and students.

School should manage students, teachers, and courses, and provide methods to enroll students, 
assign teachers, and generate reports on courses.
"""

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age=age

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id =student_id


class Teacher(Person):
    def __init__(self,name,age,teacher_id):
        super().__init__(name,age)
        self.teacher_id=teacher_id

class Course:

    def __init__(self,course_id,name):
        self.course_id =course_id
        self.name =name
        self.students =[]  

    def enroll_student(self, student):
        self.students.append(student)

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = [] 

    def add_student(self, student):
        self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def add_course(self, course):
        self.courses.append(course)

    
    def generate_course_report(self,course):
        if course in self.courses:
            print("Course:",course.name,"ID:",course.course_id)
            print("Enrolled Students:")
            for student in course.students:
                print("Student:",student.name,"ID: ",student.student_id)
        else:
            print("Course not found")


s = School()

student1 =Student("aaa",18, "101")
student2 =Student("bbb",19, "102")

teacher1 =Teacher("AAA",40, "001")
teacher2 =Teacher("BBB",45, "002")

course1 = Course("M101","Math")
course2 = Course("P201","Phy")


course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student2)

s.add_student(student1)
s.add_student(student2)
s.add_teacher(teacher1)
s.add_teacher(teacher2)
s.add_course(course1)
s.add_course(course2)

s.generate_course_report(course1)
