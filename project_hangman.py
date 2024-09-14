print()
print("                        HANGMAN GAME : ")
print()
import random
import picture_hangman
words=["apple","mango","beautiful","afnitha","aslam","books","potato","hangman","python","coding"]
final_words=random.choice(words)
count=0
words_list=[]
for i in final_words:
    count+=1
    words_list+=('-')
print(f"* You have only {count} lives so try to guess the word within {count} attempts , Good luck ! ")
#print(final_words)
print(f"* You want to enter a {count} letter word : ")
print(words_list)
print()
for i in range(count):
    count-=1
    letter=input("Enter a letter : ")
    print()
    if(letter in final_words):
        words_list[i]=letter
        print(words_list)
        print(f"You have only {count} life ")
        print()
    else:
        print(picture_hangman.pict[i])
        print(f"You have only {count} life ")
        print()
