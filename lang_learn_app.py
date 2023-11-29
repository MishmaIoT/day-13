class LanguageCourse:
    def __init__(self, language, level, lessons):
        self.language = language
        self.level = level
        self.lessons = lessons
        self.completed_lessons = {}

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

class LanguageApp:
    def __init__(self):
        self.language_courses = []

    def enroll_student(self, student, course):
        student.enrolled_courses.append(course)
        print(f"{student.name} enrolled in {course.language} - {course.level} course.")

    def complete_lesson(self, student, course, lesson):
        if lesson in course.lessons:
            course.completed_lessons.setdefault(student, []).append(lesson)
            print(f"{student.name} completed lesson {lesson} in {course.language} - {course.level} course.")
        else:
            print(f"Lesson {lesson} not found in the course.")

    def track_progress(self, student, course):
        if student in course.completed_lessons:
            print(f"Progress for {student.name} in {course.language} - {course.level} course:")
            for lesson in course.completed_lessons[student]:
                print(f"- Lesson {lesson}")
        else:
            print(f"No progress found for {student.name} in {course.language} - {course.level} course.")

# Example usage:
english_course = LanguageCourse("English", "Intermediate", ["Grammar", "Vocabulary", "Listening"])
french_course = LanguageCourse("French", "Beginner", ["Greetings", "Numbers", "Basic Phrases"])
john = Student("John", "S001")
jane = Student("Jane", "S002")
language_app = LanguageApp()
language_app.language_courses.extend([english_course, french_course])
language_app.enroll_student(john, english_course)
language_app.enroll_student(jane, french_course)
language_app.complete_lesson(john, english_course, "Grammar")
language_app.complete_lesson(jane, french_course, "Greetings")
language_app.complete_lesson(jane, french_course, "Numbers")
language_app.track_progress(john, english_course)
language_app.track_progress(jane, french_course)

