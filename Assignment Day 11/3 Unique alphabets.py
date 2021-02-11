#Print all alphabets that never appear double in sequence (back to back) in the words in the above-mentioned file

import data_prep as d
import string
for alpha in string.ascii_uppercase:
    flag=True
    for word in d.my_word_list_cln:
        if alpha*2 in word:
            flag=False
            break
    if flag:
        print(alpha)