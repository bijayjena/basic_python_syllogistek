import os
file_obj=open(r"sowpods.txt")
my_word_list=file_obj.readlines()
my_word_list_cln=[word.strip() for word in my_word_list]
file_obj.close()