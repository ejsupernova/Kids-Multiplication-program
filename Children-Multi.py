import sys
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
   hard_mode_proxy = input("Hello what would you like to set the mode to " + name)
   bool(hard_mode_proxy)
   hard_mode = hard_mode_proxy
   print("hard mode = " + hard_mode)
   
print("What is 4 x 5? ")
print("(a)     (b)")
print("32      20 ")
print("")
Test = input()
if Test == "b" or Test == "20":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect You must now go to the tutorial!")
    print("Welcome To The Tutorial!")
    print("")
    print("Multiplication is easy all you need to do is add")
    print("that number the amount of times e.g 2x3/2+2+2 as")
    print("you can see i added 2, 3 times!This is what makes")
    print("it so easy!")
    print("")
    input("Type anything to proceed: ")


print("what is 3x6?")
print("(a)     (b)")
print("18      13 ")
print("")

Test = input()
if Test == "a" or Test == "18":
    print("Congratulations You Are Correct!")
    print("You Will Be Awarded 50exp")
    xp = xp + 50
    print("Your EXP is  " + str(xp))
else:
    print("Incorrect!")
    print("Your exp is now" + str(xp))
input("Type anything to procced")
if hard_mode == True:
    print("Welcome To The hard mode bonus quistion!")
    print("")
    print("What is 287 x 9?")
    print("2583    2467")
    print(" a       b")
    print("")
    print(" c       d ")
    print("2896    2479")
    hard_quiz1 = input()


print("Thank you for using our repo! #alpha")
print("DO NOT DEL OR ELSE")
input("Press Any Button to exit")
