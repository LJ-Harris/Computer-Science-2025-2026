# starter program lesson 1
import time

name = input("What's your name?		")
#records users' name
print("We want to know if you like programming!")
print()
#flavour text
time.sleep(0.6)
#wait
answer = input("Do you like programming, " +name+"?	")
# ask question to define variable 'answer'
time.sleep(0.2)
print("Great! You said " + answer + "!")
time.sleep(0.3)
print("Let's learn some Python today")

# Q1: 2 Variables - 'name' and 'answer'
# Q2: 'input' is present, it can record a response from the user typed into the shell
# Q3: '+' in the print statements are used to space/join the variables in the print statement
#       print("Great! You said ", answer, "!")
# &   print("Great! You said " + answer + "!")
#      both show different in the shell
# Q4: it creates and empty line in the shell