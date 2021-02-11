#Print the words that are in sonnet_words.txt but not in sowpods.txt

import sowpods as s
import os
file_obj=open(r"sonnet_words.txt")
list_sonnet=file_obj.readlines()
list_sonnet_cln=[word.strip() for word in list_sonnet]
file_obj.close()

# count=0
for i in list_sonnet_cln:
    if i not in s.cln_list_sowpods:
        print(i)
        # count+=1
# print(count)