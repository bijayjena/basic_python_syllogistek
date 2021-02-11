#Print words in the file which contain all vowels

import data_prep as d
vowel=['A','E','I','O','U']
for word in d.my_word_list_cln:
    s=set()
    for alpha in word:
        if alpha in vowel:
            s.add(alpha)
    if len(s)==len(vowel):
        print(word)