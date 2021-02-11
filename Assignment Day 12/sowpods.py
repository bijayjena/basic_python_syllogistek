import os
file_obj=open(r"sowpods.txt")
list_sowpods=file_obj.readlines()
cln_list_sowpods=[word.strip() for word in list_sowpods]
file_obj.close()