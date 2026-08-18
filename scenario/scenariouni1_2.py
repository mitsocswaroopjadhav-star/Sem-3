class Employee:
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display(self):
        for e in self.employees:
            print(e.eid, e.name, e.salary, e.category())


c = Company()

e1 = Employee(1, "Rahul", 80000)
e2 = Employee(2, "Amit", 55000)
e3 = Employee(3, "Priya", 30000)

c.add_employee(e1)
c.add_employee(e2)
c.add_employee(e3)

c.display()