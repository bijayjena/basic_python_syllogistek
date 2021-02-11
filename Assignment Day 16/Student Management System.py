# student management system

# STUDENT FUNCTIONS
def addStudent(uid, name, grade, m1='0', m2='0', m3='0', m4='0', m5='0'):  # To add student details in the file
    try:
        obj = open("student.db", 'a')
        obj.write(",".join(map(str,[uid,name,grade,m1,m2,m3,m4,m5])))
        obj.write("\n")
    finally:
        obj.close()
    return 1


def searchStudent(uid):  # To search student in the file
    obj = open("student.db", 'r')
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