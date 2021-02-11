#Print the longest palindrome in sowpods.txt

import sowpods as s

max=0
for word in s.cln_list_sowpods:
    if word==word[::-1]:
        if(len(word)>max):
            max=len(word)
            l_p=word
print("Longest Pallindromic word is :",l_p)