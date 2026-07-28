#Singleton Pattern 
class Singleton:
    pass

obj1 = Singleton()
obj2 = obj1

print(obj1 == obj2) 
#True 


#Factory Pattern

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

choice = input("Dog or Cat: ")

if choice == "Dog":
    animal = Dog()
else:
    animal = Cat()

animal.sound()

#Dog or Cat: Dog
#Bark 


#Statergy Pattern

class UPI:
    def pay(self):
        print("Paid using UPI")

class Card:
    def pay(self):
        print("Paid using Card")

choice = input("UPI or Card: ")

if choice == "UPI":
    payment = UPI()
else:
    payment = Card()

payment.pay()

#UPI or Card: Card
#Paid using Card

#Observer Pattern

class Student:
    def update(self):
        print("Holiday Notification Received")

class Teacher:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def announce(self):
        for student in self.students:
            student.update()

# Main Program
s1 = Student()
s2 = Student()

teacher = Teacher()

teacher.add_student(s1)
teacher.add_student(s2)

teacher.announce()

# Holiday Notification Received
# Holiday Notification Received