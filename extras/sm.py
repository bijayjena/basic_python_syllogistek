#student management system

import getpass                                                                                  
                                                                                                #STUDENT FUNCTIONS
def addStudent(uid,name,grade,m1='0',m2='0',m3='0',m4='0',m5='0'):                              #To add student details in the file
    obj=open("student.txt",'a')
    obj.write(",".join(map(str,[uid,name,grade,m1,m2,m3,m4,m5])))
    obj.write("\n")
    obj.close()
    obj=open("login.txt",'a')
    obj.write(",".join(map(str,[uid,name,'password','Default','s'])))
    obj.write("\n")
    obj.close()

def searchStudent(uid):                                                                         #To search student in the file
    obj=open("student.txt",'r')
    flag=1
    for lst in obj.readlines():
        if lst[:len(uid)]==uid:
            flag=0
            s=lst.strip().split(',')
            key=['ID','Name','Grade','Mark1','Mark2','Mark3','Mark4','Mark5']
            for i,value in enumerate(s):
                print("{}: {}".format(key[i],s[i]))
            obj.close()
            break
    obj.close()
    if flag:
        print("Not found")

def updateStudentMarks(uid,m1,m2,m3,m4,m5):                                                     #To update students marks
    obj=open("student.txt",'r')
    newfile=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]==uid:
            s[3],s[4],s[5],s[6],s[7]=m1,m2,m3,m4,m5
            newfile.append(s)
        else:
            newfile.append(s)
    obj.close()
    obj=open("student.txt",'w')
    for lst in newfile:
        obj.write(",".join(lst))
        obj.write("\n")
    obj.close()

def deleteStudent(uid):                                                                         #To delete students record
    obj=open("student.txt",'r')
    newfile=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]!=uid:
            newfile.append(s)
    obj.close()
    obj=open("student.txt",'w')
    for lst in newfile:
        obj.write(','.join(lst))
        obj.write("\n")
    obj.close()
    
def displayStudent():                                                                           #To display student datas
    obj=open("student.txt",'r')
    print("ID\tName\tGrade\tMark1\tMark2\tMark3\tMark4\tMark5")
    print("--\t----\t-----\t-----\t-----\t-----\t-----\t-----")
    for lst in obj.readlines():
        s=lst.strip().split(',')
        print(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+s[6]+"\t"+s[7])
    obj.close()
                                                                                                #TEACHER FUNCTIONS
def addTeacher(uid,name,grade,subject):                                                         #To add teacher details in the file
    obj=open("teacher.txt",'a')
    obj.write(",".join(map(str,[uid,name,grade,subject])))
    obj.write("\n")  
    obj.close()
    obj=open("login.txt",'a')
    obj.write(",".join(map(str,[uid,name,'password','Default','t'])))
    obj.write("\n")
    obj.close()

def searchTeacher(uid):                                                                         #To search teacher in the file
    obj=open("teacher.txt",'r')
    flag=1
    for lst in obj.readlines():
        if lst[:len(uid)]==uid:
            flag=0
            s=lst.strip().split(',')
            key=['ID','Name','Grade','subject']
            for i,value in enumerate(s):
                print("{}: {}".format(key[i],s[i]))
            obj.close()
            break
    obj.close()
    if flag:
        print("Not found")

def displayTeacher():                                                                           #To display teacher details
    obj=open("teacher.txt",'r')
    print("ID\tName\tGrade\tSubject")
    print("--\t----\t-----\t-------")
    for lst in obj.readlines():
        s=lst.strip().split(',')
        print(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3])
    obj.close()

def updateTeacher(uid,sub):                                                                     #To update teacher subjects
    obj=open("teacher.txt",'r')
    newfile=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]==uid:
            s[3]=sub
            newfile.append(s)
        else:
            newfile.append(s)
    obj.close()
    obj=open("teacher.txt",'w')
    for lst in newfile:
        obj.write(",".join(lst))
        obj.write("\n")
    obj.close()

def deleteTeacher(uid):                                                                         #To delete teacher datas
    obj=open("teacher.txt",'r')
    newfile=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]!=uid:
            newfile.append(s)
    obj.close()
    obj=open("teacher.txt",'w')
    for lst in newfile:
        obj.write(','.join(lst))
        obj.write("\n")
    obj.close()

def admin():                                                                                    #Admin portal    
    print("ADMIN MENU")
    print("----------")
    print("1:Add student\n2:Add teacher\n3:Display teacher\n4:Display student\n5:Search student\n6:Search teacher\n7:Update student\n8:Update teacher\n9:Delete student\n10:Delete teacher\nPRESS E TO EXIT")
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
        else:
            print("Invalid Choice!!")
        
def teacher():                                                                                  #Teacher portal
    print("TEACHER MENU")
    print("------------")
    print("\n1:Add marks\n2:Search Student\n3:Display Student:")
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

def student():                                                                                  #Student portal
    print("STUDENT MENU")
    print("------------")
    print("\n1:Search Student:")
    while(True):
        ch=input("Enter your choice: ")
        if ch=='e' or ch=='E':
            print("Logout")
            break
        elif ch=='1':
            searchStudent(input("ID: "))
        else:
            print("Invalid choice")

def default(uid):                                                                               #Default to Change password func.
    obj=open('login.txt','r')
    newfile=[]
    for lst in obj.readlines():
        s=lst.strip().split(',')
        if s[0]==uid:
            s[2]=input("Enter new password: ")
            s[3]='change'
            newfile.append(s)
        else:
            newfile.append(s)
    obj.close()
    obj=open("login.txt",'w')
    for lst in newfile:
        obj.write(",".join(lst))
        obj.write("\n")
    obj.close()
    print("Password Changed.")

def verification():                                                                             #Authentication
    while(True):
        print("Login")
        print("-----")
        user=input("User ID: ")
        password=input("Password: ")
        if user=='admin' and password=='admin':
            admin()
        else:
            obj=open('login.txt','r')
            flag=0
            for lst in obj.readlines():
                s=lst.strip().split(',')
                if s[0]==user:
                    flag=1
                    break
            obj.close()
            if flag:
                if s[3]=='Default':
                    default(s[0])
                else:
                    if s[4]=='s':
                        student()
                    elif s[4]=='t':
                        teacher()
            else:
                print("Invalid id and password")
        ch=input("Press any key to login or press E to exit: ")
        if ch=='e' or ch=='E':
            break
def main():                                                                                 #Main function
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
    verification()
main()                                                                                      #Beginning
