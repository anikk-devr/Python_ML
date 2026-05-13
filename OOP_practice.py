class Student: 
    def __init__(self, name, dept, cgpa):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa

    def show_info(self):
        print("Name: ", self.name)
        print("Dept: ", self.dept)
        print("CGPA: ", self.cgpa)

    def is_good_student(self):
        if self.cgpa > 3.50:
            print("Good Student")
        else: 
            print("Bad Studnet")


s1 = Student("Anik", "CSE", 3.56)
s1.show_info()
s1.is_good_student()

s2 = Student("Rahat", "EEE", 3.26)
s2.show_info()
s2.is_good_student()

s3 = Student("Mahadi", "CSE", 3.16)
s3.show_info()
s3.is_good_student()








