string=input("Enter a string(all alphabets):")
if(string<=26)
    i=0
    f=1
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if(string[i]==string[j]):
                f=0
                break
    if(f):
        print("UNIQUE")
    else:
        print("not UNIQUE")
else:
        print("not UNIQUE")
