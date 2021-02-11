def addstudent(sid,name,grade,m1=0,m2=0,m3=0,m4=0,m5=0):
    f1=open("student1.txt","a")
    f1.write(",".join(map(str,([sid,name,grade,m1,m2,m3,m4,m5]))))
    f1.write("\n")
    f1.close()
def addteacher(tid,tname,tgrade):
    f2=open("teacher1.txt","a")
    f2.write(",".join(map(str,([tid,tname,tgrade]))))
    f2.write("\n")
    f2.close()
def Update_mark(Id,m1,m2,m3,m4,m5):
    f3=open("student.txt","w+")
    li=[i.strip().split(",") for i in f3.readlines()]
    for s in li:
        if s[0]==str(Id):
            s[3]=m1
            s[4]=m2
            s[5]=m3
            s[6]=m4
            s[7]=m5
            print("Student id:",s[0])
            print("Student name:",s[1])
            print("Student grade:",s[2])
            print("Mark sub1:",s[3])
            print("Mark sub2:",s[4])
            print("Mark sub3:",s[5])
            print("Mark sub4:",s[6])
            print("Mark sub5:",s[7])

loginid=input("enter a login id:")
password=input("enter a password:")
p=password
flag="d"

"""file1=open("login.txt","r+")
lis=[i.strip().split(",")for i in file1.readlines()]
for j in lis:
    if j[1]=="password":
        j[1]=input("enter a new password:")
        flag="y"
    else:
        continue"""


        
        
if loginid=="admin" and password=="password":
        print("----Welcome Administrator----")
        print("1.Add Student")
        print("2.Add Teacher")
        print("3.Upate mark")
        print("4.Exit")
        while True:
            ch=int(input("Enter your choice: "))
            if ch==1:
                sid=int(input("Enter id:"))
                name=input("Enter name:")
                grade=input("Enter grade:")
                addstudent(sid,name,grade)
                file1=open("login.txt","a")
                file1.write(",".join(map(str,([sid,p,"d"]))))
                file1.write("\n")
                file1.close()
                
                
            
            elif ch==2:
                tid=int(input("Enter id:"))
                tname=input("Enter name:")
                tgrade=input("Enter grade:")
                addteacher(tid,tname,tgrade)
            
            elif ch==3:
                Id=int(input("Enter the id to update:"))
                m1=int(input("Enter the mark of sub1:"))
                m2=int(input("Enter the mark of sub2:"))
                m3=int(input("Enter the mark of sub3:"))
                m4=int(input("Enter the mark of sub4:"))
                m5=int(input("Enter the mark of sub5:"))
                Update_mark(Id,m1,m2,m3,m4,m5)
            elif ch==4:
                break
else:
    file1=open("login.txt","r+")
    lis=[i.strip().split(",")for i in file1.readlines()]
    for j in lis:
        if j[0]==loginid:
            if j[2]=="d":
                j[1]=input("enter the new password")
                flag="y"
                file1.write(".".join(map(str,[loginid,j[1],flag])))
                file1.write("\n")
                file1.close()
                print("password has successfully changed")
                found=True
            break
        else:
            found=False
    if found:
        print("success")
    else:
        print("user not found")
