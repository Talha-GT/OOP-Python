class Student:
    def __init__(self,name,CurrentClass,Id):
        self.name=name
        self.CurrentClass=CurrentClass
        self.Id=Id
        
    def __repr__(self)->str:
        return f"Student name : {self.name} Current Class :{self.CurrentClass}  Id: {self.Id}"
class Teacher:
    def __init__(self,name,subject,Id):
        self.name=name
        self.subject=subject
        self.Id=Id
    def __repr__(self)->str:
        return f"Teacher Name:{self.name} Alloted Subject : {self.subject} Id: {self.Id}"

class School:
    def __init__(self,SchoolName):
        self.SchoolName=SchoolName
        self.Allteacher=[]
        self.AllStudent=[]

    def Add_teacher(self,name,subject):
        id=len(self.Allteacher)+1001
        teacherobj=(name,subject,id)
        self.Allteacher.append(teacherobj)

    def Enrollment(self,StuName,Stuclass,fee):
        if fee <6500:
            print(f'{StuName}  need to more:{6500-fee}$ to continue')
        else:
            stuid=len(self.AllStudent)+1
            enrolledStudent=Student(StuName,Stuclass,stuid)
            self.AllStudent.append(enrolledStudent)
    def __repr__(self)->str:
        print(f'Welcome to {self.SchoolName}')
        print('---------OUT TEACHER----------')
        for item in self.Allteacher:
            print(item)
        print('----------OUR STUDENT----------')
        for item in self.AllStudent:
            print(item)
        return 'All done here for'

My_school=School('MBSTU')
My_school.Enrollment('Alia vat',7,1200)
My_school.Enrollment('pori moni',7,6000)
My_school.Enrollment('sonam kapoor',8,12000)
My_school.Enrollment('Ranbeer sing',9,6500)
My_school.Enrollment('pushpa jhukega nehi',5,7000)


My_school.Add_teacher('Avishik bachhan','DSA')
My_school.Add_teacher('Oisharia rai','OOP')
My_school.Add_teacher('Amitav bachan','CP')

print(My_school)