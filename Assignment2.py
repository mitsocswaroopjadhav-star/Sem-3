def report_header(func):
    def wrapper(*awrgs,**kwargs):
        print("=" *40)
        print("Student report")
        func(*awrgs,**kwargs)

        print("=" * 40)
    return wrapper


class Report:
    college = "XYZ COLLEGE"
    def __init__(self,name,rollno,grade):
        self.name = name 
        self.rollno = rollno
        self.grade = grade

    @classmethod
    def changecollege(cls,new_name):
        cls.new_name = new_name



    @report_header
    def display_reports(self):
        print(f"College : {Report.college}")
        print("Name :" , self.name)
        print("Roll no : " , self.rollno)
        print("Grade : ",self.grade)

        if self.grade>=35:
            print("PASS")
    
        else:
            print("Fail")

student1 = Report("Rahul", 101, 85)
student1.display_reports()