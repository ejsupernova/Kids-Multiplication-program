import sys
import os
from time import sleep
import tkinter as tk
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

if int(age) > 20:
   print("Welcome To The Parent Control Panel!")
   print("You Can Control Your Child's Multiplication Quiz")
   print("Mode = " + str(hard_mode))
   hard_mode_proxy = input("Hello what would you like to set the mode to " + name + " ")
   bool(hard_mode_proxy)
   hard_mode = hard_mode_proxy
   print("hard mode = " + hard_mode)
#-----------------------------------------
print("What is 10/2? ")
print("(a)     (b)")
print("9      5 ")
print("")
Test = input()
if Test == "b" or Test == "5":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect You must now go to the tutorial!")
    print("Welcome To The Tutorial!")
    print("")
    print("Disvision is easy all you need to do is Split")
    print("that number the amount of times e.g 2/8=4+4 as")
    print("you can see i di 2, 3 times!This is what makes")
    print("it so easy!")
    print("")
    input("Type anything to proceed: ")
#-------------------------------------------

print("what is 9/3?")
print("(a)     (b)")
print("7      3 ")
print("")

Test = input()
if Test == "b" or "3":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("Your exp is now" + xp)
#----------------------------------------------
print("what is 28/2?")
print("(a)     (b)")
print(" 14       24 ")
print("")

Test = input()
if Test == "a" or "14":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 100exp!")
    xp = xp + 100
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("Keep Going!")
    print("Your exp is now" + xp)
    #-----------------------------------------------
print("!!Bonus!!")
print("what is 10 X 589347542?")
print("    (a)                (b)")
print(" 589347690          5893475420 ")
print("")

Test = input()
if Test == "a" or "14":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 110exp!")
    print("Nice job on the bonus!")
    xp = xp + 110
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("Keep Trying!")
    print("Your exp is now" + xp)
#--------------------------------------
print("what is 100/10")
print("    (a)        (b)")
print("    12          10 ")
print("")

Test = input()
if Test == "b" or "10":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp!")
    print("Wow nice job!")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("....")
    print("Your exp is now" + xp)
#--------------------------------------
print("what is 48/2")
print("    (a)        (b)")
print("    36          24 ")
print("")

Test = input()
if Test == "b" or "24":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 45exp!")
    print("Wow very good job!")
    xp = xp + 45
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("You can do better")
    print("Your exp is now" + xp)
#--------------------------------------
print("what is 64/2")
print("    (a)        (b)")
print("     32         45 ")
print("")

Test = input()
if Test == "a" or "32":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp!")
    print("Wow very good job!")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("Ok")
    print("Your exp is now" + xp)
#--------------------------------------
print("what is 12/4")
print("    (a)        (b)")
print("     2         3 ")
print("")

Test = input()
if Test == "b" or "3":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 65exp!")
    print("Nice")
    xp = xp + 65
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("R.I.P")
    print("Your exp is now" + xp)


if hard_mode == True:
    print("Sorry Hard Mode Is Disabled For Now!")

print("Thank you for using our 3rd party repo! #alpha")
print("Exiting...")
sleep(1)
print("Exiting..")
sleep(1)
print("Exiting.")
sleep(0.2)
exit()