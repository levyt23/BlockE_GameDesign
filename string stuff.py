#taylor levy
# february 2 2022
#strings array of charecters
# has many functions

import os, random
os.system ('clear')

myName= "maria suarez"
myStatement= """my name is so nice because
blah blah blah

what ever
ever"""

print ("my last name begins with" + myName [6])
print(myStatement)

if 'blah' in myStatement:
    print ('true')
    #this means the word blah will print as true
print ('expert' not in myStatement)
    #this means that myStatement will print as true

INDEX= myName.find("a")
print(INDEX)
#finding the length of your word
wordLen=len(myName)
print(wordLen) #your last index is length-1
#for loop in range 0 to limit
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i)
print (" ")
print ("done")
myStatement=myStatement.upper()
print(myStatement)


check=True
while check:
    letter=input("Dear user, please give us a nice letter)
    if len(letter)>1 or not letter.isalpha()
        print("Bad")
    else:
        check=False


letter=input("Dear user, please give us a nice letter")
print("Thank you, the letter is" + letter)
if letter in myStatement:
    print ("GREAT")