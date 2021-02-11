while(1):
    P=int(input("Enter the Principle : "))
    R=float(input("Enter the Rate : "))
    T=int(input("Enter the Time : "))
    if (P>0 and R>0 and T>0):
        print("The Simple Interest is : ",(P*R*T)/100)
    else :
        print("Input Error!! Try again")
    x=int(input("Try again? Press 1 else anything else..."))
    if (x==1):
        print("Once again :")
    else:
        exit()