import sqlite3

class Student:

    def __init__(self, StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor):
        self.StudentId = int(StudentId)
        self.FirstName = str(FirstName)
        self.LastName = str(LastName)
        self.GPA = float(GPA)
        self.Major = str(Major)
        self.FacultyAdvisor = str(FacultyAdvisor)

    def getStudentId(self):
        return self.StudentId

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getGPA(self):
        return self.GPA

    def getMajor(self):
        return self.Major

    def getFacultyAdvisor(self):
        return self.FacultyAdvisor

    def getStudent(self):
        return(self.getStudentId(), self.getFirstName(), self.getLastName(),
               self.getGPA(), self.getMajor(), self.getFacultyAdvisor())

