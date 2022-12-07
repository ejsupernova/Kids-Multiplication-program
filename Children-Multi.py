import sys
import os
import random
from time import sleep

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

    def disable(self):
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.ENDC = ''
        

hard_mode = False
xp = 0
print("______________________________________")
print(f"             {bcolors.WARNING}Epic Quiz Game!{bcolors.ENDC}")
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
print("to exit at anytime, please type Q as an answer")

def loop():
    xp = 0
    hits = 0
    loop = True
    while loop:
        multi1 = random.randint(2,12)
        multi2 = random.randint(2,12)
        print (f"{bcolors.OKBLUE}What is " + str(multi1) + " x " + str(multi2) + f"?{bcolors.ENDC}")
        answer = input("Answer: ")
        sum_answer = multi1 * multi2
        
        # check if answer is Q, then print final results and exit the loop.
        if answer.lower().strip() != 'q':                
            if answer == str(sum_answer):
                print(f"{bcolors.OKGREEN}Correct!{bcolors.ENDC}")
                print(f"The answer was {bcolors.OKGREEN}{str(sum_answer)}{bcolors.ENDC}")
                print(f"You answered {bcolors.OKGREEN}{str(answer)}{bcolors.ENDC}")            
                xp = xp + 50
                print(f"You have {bcolors.OKGREEN}{str(xp)}{bcolors.ENDC} XP")
            else:            
                print(f"{bcolors.WARNING}Incorrect!{bcolors.ENDC}")
                print(f"The answer was {bcolors.OKGREEN}{str(sum_answer)}{bcolors.ENDC}")
                print(f"You answered {bcolors.WARNING}{str(answer)}{bcolors.ENDC}")            
                print(f"You have {bcolors.OKGREEN}{str(xp)}{bcolors.ENDC} XP")            
                
                hits = hits + 1            
                # you may uncomment the below line if you want to show the number of wrong answers to your child after each wrong answer.
                # print(f"You had {bcolors.WARNING}{str(hits)}{bcolors.ENDC} wrong answers")
        else:
            # exit
            print("")
            print(f"You have {bcolors.OKGREEN}{str(xp)}{bcolors.ENDC} XP")            
            print(f"You had {bcolors.WARNING}{str(hits)}{bcolors.ENDC} wrong answers")
            loop = False
     


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