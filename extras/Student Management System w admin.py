# Student Management System with admin settings
from abc import abstractmethod, ABC


def display_s(s):  # To display student data
    lst = s.strip().split(',')
    key = ['ID', 'Name', 'Grade', 'Mark1', 'Mark2', 'Mark3', 'Mark4', 'Mark5']
    for i, value in enumerate(lst):
        print("{}: {}".format(key[i], lst[i]))


class student:
    def __init__(self,uid,name,grade,m1,m2,m3,m4,m5):
        self.uid = uid
        self.name = name
        self.grade = grade
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    @abstractmethod
    def addStudent(self):
        pass

    def searchStudent(self):
        obj = open("student.db", 'r')
        flag = 1
        for lst in obj.readlines():
            if lst[:len(self.uid)] == self.uid:
                flag = 0
                display_s(lst)
                obj.close()
                break
        obj.close()
        if flag:
            print("Not found")

class teacher:
    def __init__(self,uid,name,subject):
        self.uid = uid
        self.name = name
        self.subject = subject

    @abstractmethod
    def addTeacher(self):
        pass

    def searchTeacher(self):
        obj = open("student.db",'r')
        flag = 1
        for lst in obj.readlines():
            if lst[:len(self.uid)] == self.uid:
                flag = 0
                display_s(lst)
                obj.close()
                break
        obj.close()
        if flag:
            print("Not found")

class admin(student, teacher):
    def __init__(self,admin,pwd):
        self.admin=admin
        self.pwd=pwd

    def login(self,log,pwd):
        if self.log == "admin" and self.pwd == "password":
            print("----Welcome Administrator----")
            print("1.Add Student")
            print("2.Add Teacher")
            print("3.Update mark")
            print("4.Exit")
            while True:
                ch = int(input("Enter your choice: "))


    def __addStudent(self):
        try:
            obj = open("student.db", 'a')
            obj.write(",".join(map(str, [self.uid, self.name, self.grade, self.m1, self.m2, self.m3, self.m4, self.m5])))
            obj.write("\n")
        finally:
            obj.close()
        return 1

    def __addTeacher(self):
        try:
            obj = open("teacher.db", 'a')
            obj.write(",".join(map(str, [self.uid, self.name, self.subject])))
            obj.write("\n")
        finally:
            obj.close()
        return 1

def main():

    print("1:Add student\n2:Search student\n3:Add teacher\n4:Search teacher\nPRESS E TO EXIT")
    while (True):
        ch = input("Enter your choice: ")
        if ch == 'e' or ch == 'E':
            print("Exit")
            break;
        elif ch == '1':
            addStudent(input("ID: "), input("Name: "), input("Grade: "), input("Mark 1: "), input("Mark 2: "),
                       input("Mark 3: "), input("Mark 4: "), input("Mark 5: "))
            print("Student data added")
        elif ch == '2':
            searchStudent(input("ID: "))
        elif ch == '3':
            addTeacher(input("ID: "), input("Name: "), input("Grade: "), input("Subject: "))
        elif ch == '4':
            searchTeacher(input("ID: "))
        else:
            print("Invalid Choice!!")
main()