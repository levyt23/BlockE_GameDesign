import random, os
os.system ('clear')

#  today wearelearning  to try and excpet, functions,  elif
#  lets  make a menu function key word fef
def menu():
    print('########################################')
    print('#         guess a number menu          #')
    print('#           choice  1: 1-10            #')
    print('#           choice  2: 1-50            #')
    print('#           choice  3: 1-100           #')
    print('########################################')
#checking for correct user input
check=True
while  check:
    try:
        choice=int(input("choice:"))
        if choice>0 or choice<4:
            check = False
        else:
            print ("please enter a number 1-3")
    except ValueError:
            print("sorry, wrong choice, try again")

if choice == 1:
    mynumber= random.randint(1,10)
elif choice == 2:
    mynumber= random.randint(1,50)
elif choice == 3:
    mynumber= random.randint(1,100)

randomNum(gametype) 

gameon = True
#looping with  condition
while(gameon):
    userguess=int(input("guess a number..."))
    if mynumber ==userguess:
        print ("you guessed it")
        gameon=False
    else:
        print ("good luck next time", mynumber)
print("the number  to  guess was " + str(mynumber))

os.system('clear')
menu()