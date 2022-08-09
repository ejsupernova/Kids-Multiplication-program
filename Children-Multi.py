

import sys
import os
import random
from time import sleep
hard_mode = False
xp = 0
print("______________________________________")
print("             Epic Quiz Game!")
print("                 Rules!")
print("")
print("1.Do not use caps!")
print("2.Have Fun!")
print("______________________________________")

name = input("Please Type Your Name ")
age = input("Please Type your age ")
try:
    print(int(age))
except:
    print("Please Type a valid age")
    sys.exit()
print("Welcome " + name + " you are " + age + " years old")

def loop():
    loop = True
    while loop:
        multi1 = random.randint(2,20)
        multi2 = random.randint(2,20)
        print ("What is " + str(multi1) + " x " + str(multi2) + "?")
        answer = input("Answer: ")
        sum_answer = multi1 * multi2
        print("The answer was " + str(sum_answer))
        print("You answered " + answer)
        if answer == str(sum_answer):
            print("Correct!")
            xp = xp + 50
            print("You have " + str(xp) + " XP")
        else:
            print("Incorrect!")
            print("You have " + str(xp) + " XP")
     


if int(age) > 20:
   print("Welcome To The Parent Control Panel!")
   print("You Can Control Your Child's Multiplication Quiz")
   print("Mode = " + str(hard_mode))
   hard_mode_proxy = input("Hello what would you like to set the mode to " + name + " ")
   bool(hard_mode_proxy)
   hard_mode = hard_mode_proxy
   print("hard mode = " + hard_mode)
#-----------------------------------------

loop()

print("Congrats your total xp is " + str(xp) + " Wow!")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Thank you for using our 3rd party repo! #alpha")
print("Exiting...")
sleep(1)
print("Exiting..")
sleep(1)
print("Exiting.")
sleep(0.2)
exit()