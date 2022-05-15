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
   hard_mode_proxy = input("Hello what would you like to set the mode to " + name + " ")
   bool(hard_mode_proxy)
   hard_mode = hard_mode_proxy
   print("hard mode = " + hard_mode)
   
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
input("Type anything to procced")
if hard_mode == True:
    print("Sorry Hard Mode Is Disabled For Now!")

print("Thank you for using our repo! #alpha")
print("DO NOT DEL OR ELSE")
input("Press Any Button to exit")
