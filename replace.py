#The replace() function will remove all the exclamation in the sentence.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
#Variable new_sentence is used to store the corrected sentence.
new_sentence = sentence.replace("!", " ")
#Print will display the corrected sentence in the output.
print(new_sentence)

#To reprint that sentence in all Capital letters, the upper() function is used.
capitalized_sentence = new_sentence.upper()
#Print will display the sentence in the output in all capital letters.
print(capitalized_sentence)

#To print the sentence in reverse. I used the string index below, leaving the start and end index blank.
print(capitalized_sentence[::-1])
