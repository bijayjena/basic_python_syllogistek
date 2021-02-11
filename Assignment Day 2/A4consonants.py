str=input("Enter a string : ")
#list=['a','e','i','o','u','A','E','I','O','U']
i=0
while i!=len(str):
    if(str[i]!='a' and str[i]!='e' and str[i]!='i' and str[i]!='o' and str[i]!='u' and str[i]!='A' and str[i]!='E' and str[i]!='I' and str[i]!='O' and str[i]!='U'):
        print(str[i],end=" ")
    i=i+1
