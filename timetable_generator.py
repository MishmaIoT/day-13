class Course:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.teacher = None
        self.students = []

class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Timetable:
    def __init__(self):
        self.courses = []

    def assign_teacher(self, course, teacher):
        course.teacher = teacher
        print(f"{teacher.name} assigned to teach {course.name}.")

    def enroll_student(self, course, student):
        course.students.append(student)
        print(f"{student.name} enrolled in {course.name}.")

    def generate_timetable(self):
        print("School Timetable:")
        for course in self.courses:
            print(f"{course.name} - {course.teacher.name} - {course.schedule}")

# Example usage:
math_course = Course("Mathematics", "Mon-Wed-Fri 10:00-11:30")
physics_course = Course("Physics", "Tue-Thu 13:00-14:30")
alice = Student("Alice", "S001")
bob = Student("Bob", "S002")
math_teacher = Teacher("Mr. Smith")
physics_teacher = Teacher("Mrs. Johnson")
school_timetable = Timetable()
school_timetable.courses.extend([math_course, physics_course])
school_timetable.assign_teacher(math_course, math_teacher)
school_timetable.assign_teacher(physics_course, physics_teacher)
school_timetable.enroll_student(math_course, alice)
school_timetable.enroll_student(physics_course, bob)
school_timetable.generate_timetable()
