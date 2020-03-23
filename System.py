import sqlite3
import pandas as pd
from pandas import DataFrame
from Student import Student

class System:

    def __init__(self):
        conn = sqlite3.connect('StudentDB.sqlite')
        c = conn.cursor()

    #a. Display All Students and all their attributes.
    #i. Create the necessary SELECT statement to produce this result
    def displayAll(self):
        self.c.execute("SELECT * FROM Student")
        studentRows = self.c.fetchall()
        df = DataFrame(studentRows, columns = ["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
        print(df)


    #b. Create Students
    #i. All attributes are required when creating new student.
    #ii. Please make sure to validate user input appropriately.
    def createStudent(self):
        print(" --- Create Student --- ")
        sId = int(input('Student ID: '))
        sFirst = str(input('First Name: '))
        sLast = str(input('Last Name: '))
        sGPA = float(input('GPA: '))
        sMajor = str(input('Major: '))
        sFaculty = str(input('Faculty Advisor: '))
        newStudent = Student(sId, sFirst, sLast, sGPA, sMajor, sFaculty)
        self.c.execute("INSERT INTO Student VALUES('?', '?', '?', '?', '?', '?')", newStudent.getStudent());
        self.conn.commit()
        print(" --- Student Created ---")

    #c. Update Students
    #i. Only the Major and Advisor attributes can be updated.
    #ii. Make sure you construct a proper UPDATE statement so that you don’t update every record in the database.
    def updateStudent(self):
        print(" --- Update Student --- ")
        while (True):

            stud = int(input("Enter Student ID to Update: "))
            print(" Update: a) Major b) Faculty Advisor")
            update = input(' Update Choice: ')

            if update == "a":
                newMajor = input("New Major: ")
                self.c.execute("UPDATE Student SET Major = '?' WHERE StudentId = '?'", (newMajor, stud));
                self.conn.commit()
                print(" --- Major Updated --- ")
            elif update == "b":
                newAdvisor = input("New Advisor: ")
                self.c.execute("UPDATE Student SET FacultyAdvisor = '?' WHERE StudentId = '?'", (newAdvisor, stud));
                self.conn.commit()
                print(" --- Advisor Updated --- ")
            else:
                print("Input Error")
                break

    #d. Delete Students by StudentId
    #i. Perform a “soft” delete on students
    #ii. Set isDeleted to true (1)
    def deleteStudent(self):
        print(" --- Delete Student --- ")
        stud = int(input("Student to be Deleted: "))
        self.c.execute("UPDATE Student SET isDeleted = 1 WHERE StudentId = '?'", (stud))
        self.conn.commit()
        print(" --- Student Deleted --- ")

    #e. Search/Display students by Major, GPA and Advisor.
    #i. User should be able to query by the three aforementioned fields
    def searchStudent(self):
        print(" --- Student Search --- ")
        print("Search by 1) Major, 2) GPA, or 3) Advisor")
        choice = int(input("Search by: "))
        if choice == 1: #search by major
            major = input("Major: ")
            self.c.execute("SELECT * FROM Student WHERE Major = '?'", (major))
            majorRows = self.c.fetchall()
            df = DataFrame(majorRows, columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
            print(df)
        elif choice == 2:
            gpa = float(input("GPA: "))
            self.c.execute("SELECT * FROM Student WHERE GPA = '?'", (gpa))
            gpaRows = self.c.fetchall()
            df = DataFrame(gpaRows, columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
            print(df)
        elif choice == 3:
            advisor = input("GPA: ")
            self.c.execute("SELECT * FROM Student WHERE FacultyAdvisor = '?'", (advisor))
            advisorRows = self.c.fetchall()
            df = DataFrame(advisorRows, columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
            print(df)

        print(" --- Search Completed --- ")

    def menu(self):

        print(" --- Student Database -- ")
        print(" Please select one of the following options: ")
        print(" 1. Display All Students")
        print(" 2. Create Student")
        print(" 3. Update Student")
        print(" 4. Delete Student")
        print(" 5. Search Students")
        print(" 6. Save and Exit")

        while(True):
            choice = int(input(" Choice: "))
            if choice == 1:
                self.displayAll()
            elif choice == 2:
                self.createStudent()
            elif choice == 3:
                self.updateStudent()
            elif choice == 4:
                self.deleteStudent()
            elif choice == 5:
                self.searchStudent()
            elif choice == 6:
                print(" Saving Data ...")
                self.conn.commit()
                self.conn.close()
                print(" --- Done --- ")
                break