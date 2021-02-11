# student management system

# STUDENT FUNCTIONS
from os.path import exists


def addStudent(uid, name, grade, m1='0', m2='0', m3='0', m4='0', m5='0'):  # To add student details in the file
    try:
        obj = open("student.txt", 'a')
        obj.write(",".join(map(str,[uid,name,grade,m1,m2,m3,m4,m5])))
        obj.write("\n")
        log = open("login_details.txt", 'a')
        log.write("\n")
        log.write(",".join(map(str, [uid, "password"])))
    finally:
        obj.close()
        log.close()
    return 1


def searchStudent(uid):  # To search student in the file
    if exists("student.txt")==1:
        obj = open("student.txt", 'r')
        flag = 1
        for lst in obj.readlines():
            if lst[:len(uid)] == uid:
                flag = 0
                display_s(lst)
                obj.close()
                break
        obj.close()
        if flag:
            print("Not found")
    else:
        print("File not Found")


def display_s(s):  # To display student data
    lst = s.strip().split(',')
    key = ['ID', 'Name', 'Grade', 'Mark1', 'Mark2', 'Mark3', 'Mark4', 'Mark5']
    for i, value in enumerate(lst):
        print("{}: {}".format(key[i], lst[i]))


# TEACHER FUNCTIONS
def addTeacher(uid, name, grade, subject):  # To add teacher details in the file
    try:
        obj = open("teacher.txt", 'a')
        obj.write(",".join(map(str, [uid, name, grade, subject])))
        obj.write("\n")
        log = open("login_details.txt", 'a')
        log.write("\n")
        log.write(",".join(map(str, [uid, "password"])))
    finally:
        obj.close()
    return 1


def searchTeacher(uid):  # To search teacher in the file
    obj = open("teacher.txt", 'r')
    flag = 1
    for lst in obj.readlines():
        if lst[:len(uid)] == uid:
            flag = 0
            display_t(lst)
            obj.close()
            break
    obj.close()
    if flag:
        print("Not found")


def display_t(s):  # To display teacher details
    lst = s.strip().split(',')
    key = ['ID', 'Name', 'Grade', 'subject']
    for i, value in enumerate(lst):
        print("{}: {}".format(key[i], lst[i]))

def updateMark(uid,m1,m2,m3,m4,m5):
    obj=open("student.txt",'r')
    li=[i.strip().split(",") for i in obj.readlines()]
    for s in li:
        if s[0]==str(uid):
            s[3]=m1
            s[4]=m2
            s[5]=m3
            s[6]=m4
            s[7]=m5
            obj.write(",".join(map(str, [s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]])))
    obj.close()

def main():
    obj = open("login_details.txt", 'r')
    lst = [i.strip().split(",") for i in obj.readlines()]
    log_ad = lst[0][0]
    pwd_ad = lst[0][1]
    obj.close()
    login = input("Login id: ")
    password = input("Password: ")

    if login == log_ad and password == pwd_ad:
        print("1:Add student\n2:Search student\n3:Add teacher\n4:Search teacher\n5:Update marks\n6:Update Password\nPRESS E TO EXIT")
        while True:
            ch = input("Enter your choice: ")
            if ch == 'e' or ch == 'E':
                print("Exit")
                break
            elif ch == '1':
                addStudent(input("ID: "), input("Name: "), input("Grade: "), input("Mark 1: "), input("Mark 2: "), input("Mark 3: "), input("Mark 4: "), input("Mark 5: "))
                print("Student data added")
            elif ch == '2':
                searchStudent(input("ID: "))
            elif ch == '3':
                addTeacher(input("ID: "), input("Name: "), input("Grade: "), input("Subject: "))
            elif ch == '4':
                searchTeacher(input("ID: "))
            elif ch == '5':
                updateMark(input("ID: "), input("Mark 1: "), input("Mark 2: "), input("Mark 3: "), input("Mark 4: "), input("Mark 5: "))
                print("Marks updated")
            elif ch == '6':
                new_pwd=input("Enter new password: ")
                cnf=input("Confirm password: ")
                if new_pwd==cnf:
                    obj = open("admin.txt",'w+')
                    obj.write(",".join(map(str, [login,new_pwd])))
                    obj.close()
                else:
                    print("Try again")
            else:
                print("Invalid Choice!!")
    elif login == log_stud and password == pwd_stud:
        print("1:Search student\n2:Search teacher\nPRESS E TO EXIT")
        while True:
            ch = input("Enter your choice: ")
            if ch == 'e' or ch == 'E':
                print("Exit")
                break
            elif ch == '1':
                searchStudent(input("ID: "))
            elif ch == '2':
                searchTeacher(input("ID: "))
            else:
                print("Invalid Choice!!")
    elif login == log_teach and password == pwd_teach:
        print("1:Search student\n2:Search teacher\n3:Update marks\nPRESS E TO EXIT")
        while True:
            ch = input("Enter your choice: ")
            if ch == 'e' or ch == 'E':
                print("Exit")
                break
            elif ch == '1':
                searchStudent(input("ID: "))
            elif ch == '2':
                searchTeacher(input("ID: "))
            elif ch == '3':
                updateMark(input("ID: "), input("Mark 1: "), input("Mark 2: "), input("Mark 3: "), input("Mark 4: "), input("Mark 5: "))
                print("Marks updated")
            # elif ch == '4':
            #     new_pwd = input("Enter new password: ")
            #     cnf = input("Confirm password: ")
            #     if new_pwd == cnf:
            #         obj = open("admin.txt", 'w+')
            #         obj.write(",".join(map(str, [login, new_pwd])))
            #         obj.close()
            #     else:
            #         print("Try again")
            else:
                print("Invalid Choice!!")
    else:
        print("ID and Password mismatch!!")
main()