#taylor levy
#01/21/2022

#we are going to leanr the input () function, random numbers
#typecasting, branching, looping
import os, random
os.system ('clear')
#declare variable for user input
# print("enter a number 1 - 10: ", end = "#")
# useless=input() #input returns a string we must typecast if we want an integer
# print("the number is %.2f " % (useless*3))
# guess=int(input("please give me a nunmber"))

#guess a number
# mynumber = 9  instead of a fixed number we use random
mynumber=random.randint(1,10)
gameon=true
while(gameon)
    userguess=int(input("guess a number from 1-10"))
    if mynumber == serguess:
        print("you guessed it")
        gameon=false
    else:
        print("good luck next time")
    print ("the number was "+ str(mynumber))