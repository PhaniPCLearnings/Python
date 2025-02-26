import random

word_List=["Phani","Cherry","ongole"]

word_Chosen=random.choice(word_List)

placeHolder=''

for pos in range(len(word_Chosen)):
    placeHolder+='_'


print(word_Chosen)
print(placeHolder)
display = ""
i=0
user_Word =input("Guess the Letter : ")
for letter in word_Chosen:
    if letter==user_Word:
        print("Guessed word is available")
    else:
        print("Guessed it wrongly")
