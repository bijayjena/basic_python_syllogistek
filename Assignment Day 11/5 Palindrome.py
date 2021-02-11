#Print all palindrome words in the above-mentioned file

import data_prep as d

for word in d.my_word_list_cln:
    if word==word[::-1]:
        print(word)