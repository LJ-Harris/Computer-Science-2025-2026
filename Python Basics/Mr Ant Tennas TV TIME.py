import time

# Homework 15/9/2025
# Quiz time !!

def quizExtra():
    print("Welcome everyone!")
    time.sleep(0.2)
    print("It's time for....")
    time.sleep(0.5)
    print("GEO-NIUS GEOGRAPHY!!")
    time.sleep(0.75)
    print("...")
    time.sleep(0.75)
    print("Tough crowd..")
    time.sleep(0.1)
    print("ANYWAY!! On to the questions!")
    time.sleep(0.5)
    print("We will ask a series of 5 multiple choice")
    print("questions, and you must answer correctly")
    print("for at least THREE to win!")
    time.sleep(1.5)
    # Just some simple fun stuff to make the program feel more alive/energetic
    
def quizBasic():
    score = 0
    print("Our first question to start of the night will be a simple one.")
    print(" ")
    print("What is the world's LARGEST rainforest?")
    print("Is it A: The Amazon Rainforest?")
    print("B: The Southeast Asian Rainforest?")
    print("Or C: The Congolian Rainforest?")
    print("(Enter either 'a' 'b' or 'c' on your keyboard to submit your answer)")
    answer1 = "a"
    user = input(" ")
    if user.lower() == "a":
        print("Correct!")
        score = score + 1
        # records what questions you get right
    else:
        print("Incorrect :(")
    print(" ")
    print("The Amazon rainforest is the largest rainforest in the world at a staggering 7 MILLION square kilometers!")
    print("[[ according to https://en.wikipedia.org/wiki/Amazon_rainforest ]] !!")
    print("Now, onto question 2")
    print(" ")
    # checks if you answered with the correct letter in the shell, line 34 'answer1 = "a" ' is junk code now as I don't actually need a variable to check for the right answer
   
   #question 2
    print("What is the country that is also known as Holland?")
    print(" ")
    print("Is it A: Amsterdam?")
    print("B: Denmark?")
    print("Or C: The Netherlands?")
    print("(Enter either 'a' 'b' or 'c' on your keyboard to submit your answer)")
    answer1 = "c"
    user = input(" ")
    if user.lower() == "c":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect :(")
    print("It is in fact The Netherlands!")
    print("Now, onto question 3")
    print(" ")
    
    #question 3
    print("Moving onto a tricker one now, where can you find the landmark Machu Picchu?")
    print(" ")
    print("Is it A: Mexico?")
    print("B: Peru?")
    print("Or C: Brazil?")
    print("(Enter either 'a' 'b' or 'c' on your keyboard to submit your answer)")
    answer1 = "a"
    user = input(" ")
    if user.lower() == "b":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect :(")
    print("Machu Picchu is found in Peru!")
    print("They also apparently created a rudimentary form of basketball using human heads, how interesting!")
    print("Now, onto question 4")
    print(" ")

    #question 4
    print("What is the deepest point of the ocean?")
    print(" ")
    print("Is it A: The Mariana Trench?")
    print("B: The The Lough?")
    print("Or C: Goo Lagoon?")
    print("(Enter either 'a' 'b' or 'c' on your keyboard to submit your answer)")
    answer1 = "a"
    user = input(" ")
    if user.lower() == "a":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect :(")
    print("The Mariana Trench is the deepest oceanic trench on Earth at roughly 11 THOUSAND Meters!")
    print("Now, onto the FINAL question!")
    print(" ")
    
    #question 5
    print("This one is for our patriotic, constitution loving Americans in the audience..")
    print("Arizona, New Mexico, Colorado and which other state all intersect at the 'Four Corners Monument'?")
    print(" ")
    print("Is it A: New Jersey?")
    print("B: Nevada?")
    print("Or C: Utah?")
    print("(Enter either 'a' 'b' or 'c' on your keyboard to submit your answer)")
    answer1 = "a"
    user = input(" ")
    if user.lower() == "c":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect :(")
    print("The monument consists of Arizona, New Mexico, Colorado and Utah!")
    print("Now, let's see how our dear contestant did!")
    print(" ")
    
    if score >= 3:
        print("Congratulations! You won with a score of:", score, "out of 5, WOW!!")
        print("Would you like to try again to better that score? Or just to show off your geographical prowess?")
        # this will happen if you win/pass
    else:
        print("Uh oh.. not quite a victory for this daring contestant!! Dont fret however, we're here ALL night! Would you like to try again?")
    print("(type yes if you would like to play again, or no if you dont. It's fine I'm not going to me upset if you say no I promise...)")
    retry = input(" ")
    # this will happen if you dont
    if retry.lower() == "yes":
              quizBasic()
    else:
        print("Goodbye!")
    # a simple check if the player wants to take the quiz again

# To remove the bells&whistles at the start, delete line 134 'quizExtra()'
quizExtra()
quizBasic()
