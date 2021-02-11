#Take a sentence and output a dictionary with word as the key and number of characters in the word as value 

sentence=input('Enter a sentence: ').split()
dict={i:len(i) for i in sentence}
print(dict)