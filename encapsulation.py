class student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def get_name(self):
      return self.name

    def get_age(self):
      return self.age

    def get_roll_number(self):
      return self.roll_number

    def set_name(self, name):
      self.name = name

    def set_age(self, age):
      self.age = age

    def set_roll_number(self, roll_number):
      self.roll_number = roll_number

student1 = student(name="mishma", age=19, roll_number="5981")

print(f"Name: {student1.get_name()}")

print(f"Age: {student1.get_age()}")

print(f"Roll Number: {student1.get_roll_number()}")
