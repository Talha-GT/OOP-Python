class Student:
    def __init__(self, name, CurrentClass, Id):
        self.name = name
        self.CurrentClass = CurrentClass
        self.Id = Id

    def __repr__(self) -> str:
        return f"Student name: {self.name}, Current Class: {self.CurrentClass}, Id: {self.Id}"

class Teacher:
    def __init__(self, name, subject, Id):
        self.name = name
        self.subject = subject
        self.Id = Id

    def __repr__(self) -> str:
        return f"Teacher Name: {self.name}, Alloted Subject: {self.subject}, Id: {self.Id}"

class School:
    def __init__(self, SchoolName):
        self.SchoolName = SchoolName
        self.Allteacher = []
        self.AllStudent = []

    def Add_teacher(self, name, subject):
        id = len(self.Allteacher) + 1001
        teacherobj = Teacher(name, subject, id)
        self.Allteacher.append(teacherobj)

    def Enrollment(self, StuName, Stuclass, fee):
        if fee < 6500:
            print(f'You need to pay {6500 - fee} more to continue')
        else:
            stuid = len(self.AllStudent) + 1
            enrolledStudent = Student(StuName, Stuclass, stuid)
            self.AllStudent.append(enrolledStudent)

    def __repr__(self) -> str:
        result = f'Welcome to {self.SchoolName}\n'
        result += '---------OUR TEACHERS----------\n'
        for item in self.Allteacher:
            result += f'{item}\n'
        result += '----------OUR STUDENTS----------\n'
        for item in self.AllStudent:
            result += f'{item}\n'
        return result

# Testing the classes
phitron = School('Phitron')
phitron.Enrollment('Alia Vat', 7, 1200)
phitron.Enrollment('Sonam Kapoor', 8, 12000)
phitron.Enrollment('Ranbir Singh', 9, 6500)
phitron.Enrollment('Pushpa Jhukega Nahi', 5, 7000)

phitron.Add_teacher('Abhishek Bachchan', 'DSA')
phitron.Add_teacher('Aishwarya Rai', 'OOP')
phitron.Add_teacher('Amitabh Bachchan', 'CP')

print(phitron)
