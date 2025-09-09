import time

name = input("What's your name?		")
age = int(input("Hello, " +name+ " how old are you?		"))
favFood = input("What's your favourite food, " +name+ "?	")
favColor = input("And finally, what's your favourite colour?	")
newAge = age + 1
time.sleep(0.7)
print("Amazing,  you will be" , newAge , "next year, happy early birthday!")
time.sleep(0.3)
print("I think you should have " + favColor + " balloons at your" ,newAge, "th birthday")
time.sleep(0.4)
print("I had something else to say")
time.sleep(0.5)
print("Oh yes!")
time.sleep(0.1)
print("I hope you have a wonderful " +favFood+ "on your birthday. Goodbye!")