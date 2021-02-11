#Find all the words which contains 'uu' in the above-mentioned file

import data_prep as d
for i in d.my_word_list_cln:
    if "UU" in i:
        print(i)