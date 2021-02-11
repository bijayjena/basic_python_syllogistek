import getpass                                                                                  

def delete_login(uid):
    try:
        obj=open('login.txt','r')
        new_file=[]
        for lst in obj.readlines():
            s=lst.strip().split(',')
            if s[0]!=uid:
                new_file.append(s)
        obj.close()
        obj=open('login.txt','w')
        for lst in new_file:
            obj.write(','.join(lst))
            obj.write("\n")
    except FileNotFoundError:
        print("Ask admin to add required files")
    finally:
        obj.close()

def addStudent(uid,name,grade,m1='0',m2='0',m3='0',m4='0',m5='0'):
    obj=open("student.txt",'a')
    obj.write(",".join(map(str,[uid,name,grade,m1,m2,m3,m4,m5])))
    obj.write("\n")
    obj.close()
    obj=open("login.txt",'a')
    obj.write(",".join(map(str,[uid,name,'password','Default','s'])))
    obj.write("\n")
    obj.close()

def searchStudent(uid):
    try:
        obj = open("student.txt", 'r')
        flag = 1
        for lst in obj.readlines():
            if lst[:len(uid)] == uid:
                flag = 0
                s = lst.strip().split(',')
                key = ['ID', 'Name', 'Grade', 'Mark1', 'Mark2', 'Mark3', 'Mark4', 'Mark5']
                for i, value in enumerate(s):
                    print("{}: {}".format(key[i], s[i]))
                break
        obj.close()
        if flag:
            print("Not found")
    except FileNotFoundError:
        print("Ask user to create file")

def updateStudentMarks(uid,m1,m2,m3,m4,m5):
    try:
        obj = open("student.txt", 'r')
        new_file = []
        flag=1
        for lst in obj.readlines():
            s = lst.strip().split(',')
            if s[0] == uid:
                flag = 0
                s[3], s[4], s[5], s[6], s[7] = m1, m2, m3, m4, m5
                new_file.append(s)
            else:
                new_file.append(s)
        if flag:
            print("Student data not found")
            return
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()
    try:
        obj = open("student.txt", 'w')
        for lst in new_file:
            obj.write(",".join(lst))
            obj.write("\n")
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()

def deleteStudent(uid):
    try:
        obj = open("student.txt", 'r')
        new_file = []
        flag = 0
        for lst in obj.readlines():
            s = lst.strip().split(',')
            if s[0] != uid:
                new_file.append(s)
            elif s[0] == uid:
                flag = 1
        if flag:
            print("Student's data not found")
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()
    try:
        obj = open("student.txt", 'w')
        for lst in new_file:
            obj.write(','.join(lst))
            obj.write("\n")
        obj.close()
        delete_login(uid)
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()
    
def displayStudent():
    try:
        obj = open("student.txt", 'r')
        print("ID\tName\tGrade\tMark1\tMark2\tMark3\tMark4\tMark5")
        print("__\t____\t_____\t_____\t_____\t_____\t_____\t_____")
        for lst in obj.readlines():
            s = lst.strip().split(',')
            print(
                s[0] + "\t" + s[1] + "\t" + s[2] + "\t" + s[3] + "\t" + s[4] + "\t" + s[5] + "\t" + s[6] + "\t" + s[7])
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()

def addTeacher(uid,name,grade,subject):
    try:
        obj = open("teacher.txt", 'a')
        obj.write(",".join(map(str, [uid, name, grade, subject])))
        obj.write("\n")
        obj.close()
        obj = open("login.txt", 'a')
        obj.write(",".join(map(str, [uid, name, 'password', 'Default', 't'])))
        obj.write("\n")
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()

def searchTeacher(uid):
    try:
        obj = open("teacher.txt", 'r')
        flag = 1
        for lst in obj.readlines():
            if lst[:len(uid)] == uid:
                flag = 0
                s = lst.strip().split(',')
                key = ['ID', 'Name', 'Grade', 'subject']
                for i, value in enumerate(s):
                    print("{}: {}".format(key[i], s[i]))
                break
        if flag:
            print("Not found")
    except FileNotFoundError:
        print("Ask user to create file")
    finally:
        obj.close()

def displayTeacher():
    try:                                                                        
        obj = open("teacher.txt",'r')
        print("ID\tName\tGrade\tSubject")
        print("__\t____\t_____\t_______")
        for lst in obj.readlines():
            s=lst.strip().split(',')
            print(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3])
    except FileNotFoundError:
        print("Ask admin to create file")
    finally:
        obj.close()

def updateTeacher(uid,sub):
    try:
        obj = open("teacher.txt", 'r')
        new_file = []
        flag = 1
        for lst in obj.readlines():
            s = lst.strip().split(',')
            if s[0] == uid:
                flag = 0
                s[3] = sub
                new_file.append(s)
            else:
                new_file.append(s)
        if flag:
            print("Teacher's data not found")
            return
    except FileNotFoundError:
        print("Ask admin to create file")
    finally:
        obj.close()
    try:
        obj=open("teacher.txt",'w')
        for lst in new_file:
            obj.write(",".join(lst))
            obj.write("\n")
    finally:
        obj.close()

def deleteTeacher(uid):
    try:
        obj = open("teacher.txt", 'r')
        new_file = []
        flag = 0
        for lst in obj.readlines():
            s = lst.strip().split(',')
            if s[0] != uid:
                new_file.append(s)
            elif s[0] == uid:
                flag = 1
        if flag:
            print("Teacher's data not found")
    except FileNotFoundError:
        print("Ask admin to create one")
    finally:
        obj.close()
    try:
        obj = open("teacher.txt", 'w')
        for lst in new_file:
            obj.write(','.join(lst))
            obj.write("\n")
        delete_login(uid)
    finally:
        obj.close()

def admin():
    print("ADMIN MENU")
    print("__________")
    print("1:Add student\n2:Add teacher\n3:Display teacher\n4:Display student\n5:Search student")
    print("6:Search teacher\n7:Update student\n8:Update teacher\n9:Delete student\n10:Delete teacher")
    print("11:Update Password\nPRESS E TO EXIT")
    while True:
        ch=input("Enter your choice: ")
        if ch=='e' or ch=='E':
            print("Logout!!")
            break
        elif ch=='1':
            addStudent(input("ID: "),input("Name: "),input("Grade: "))
            print("Student data added")
        elif ch=='2':
            addTeacher(input("ID: "),input("Name: "),input("Grade: "),input("Subject: "))
        elif ch=='3':
            displayTeacher()
        elif ch=='4':
            displayStudent()
        elif ch=='5':
            searchStudent(input("ID: "))
        elif ch=='6':
            searchTeacher(input("ID: "))
        elif ch=='7':
            updateStudentMarks(input("ID: "),input("Mark 1: "),input("Mark 2: "),input("Mark 3: "),input("Mark 4: "),input("Mark 5: "))
        elif ch=='8':
            updateTeacher(input("ID: "),input("Subject: "))
        elif ch=='9':
            deleteStudent(input("ID: "))
        elif ch=='10':
            deleteTeacher(input("ID: "))
        elif ch=='11':
            change_pass("admin")
        else:
            print("Invalid Choice!!")
        
def teacher():
    print("TEACHER MENU")
    print("____________")
    print("\n1:Add marks\n2:Search Student\n3:Display Student:\nPRESS E TO EXIT")                                                                                 #Teacher portal
    while True:
        ch=input("Enter your choice: ")
        if ch=='e' or ch=='E':
            print("Logout")
            break
        elif ch=='1':
            updateStudentMarks(input("ID: "),input("Mark 1: "),input("Mark 2: "),input("Mark 3: "),input("Mark 4: "),input("Mark 5: "))
        elif ch=='2':
            searchStudent(input("ID: "))
        elif ch=='3':
            displayStudent()
        else:
            print("Invalid choice")

def student(uid):
    
    print("WELCOME STUDENT")
    print("_______________")
    searchStudent(uid)
    print("\n1:Change Password\nPRESS E TO EXIT")
    while True:
        ch=input("Enter your choice: ")
        if ch=='E' or ch=='e':
            break
        elif ch=='1':
            change_pass(uid)
        else:
            print("Invalid Choice")

def set_password():
    while True:
        pw=input("Enter new password: ")
        s=n=b=c=0
        if 6<=len(pw)<=12:
            print("Password Updated.")
            for ch in pw:
                if ch.islower() and s!=1:
                    s+=1
                elif ch.isupper() and b!=1:
                    b+=1
                elif ch.isnumeric() and n!=1:
                    n+=1
                elif ch in ['!','@','#','$','%','&'] and c!=1:
                    c+=1
            if s+b+n+c==4:
                break
        print("Invalid Password")
    print("Valid Password")
    return pw
        
def change_pass(uid):
    obj=open('login.txt','r')
    new_file=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]==uid:
            s[2]=set_password()
            s[3]='change'
            new_file.append(s)
        else:
            new_file.append(s)
    obj.close()
    obj=open("login.txt",'w')
    for lst in new_file:
        obj.write(",".join(lst))
        obj.write("\n")
    obj.close()
    print("Password Changed.")

def admin_pass():
    file=open("login.txt",'a')
    file.write(",".join(map(str,["admin","Administrator",'admin','Default','a'])))
    file.write("\n")
    file.close()


def main():
    # admin_pass()
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("____________________________________")
    while True:
        print("Login")
        print("_____")
        user = input("User ID: ")
        password = getpass.getpass(prompt="Password: ")
        obj = open('login.txt', 'r')
        flag = 0
        for lst in obj.readlines():
            s = lst.strip().split(',')
            if s[0] == user:
                flag = 1
                break
        obj.close()
        if flag:
            if s[3] == 'Default' and s[2] == password:
                change_pass(s[0])
            else:
                if s[4] == 's' and s[2] == password:
                    student(s[0])
                elif s[4] == 't' and s[2] == password:
                    teacher()
                elif s[4] == 'a' and s[2] == password:
                    admin()
                else:
                    print("Invalid id and password")
        ch = input("Press any key to login or press E to exit: ")
        if ch == 'e' or ch == 'E':
            break
main()