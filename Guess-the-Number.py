# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# Global Variables
high = 100
counter = 7


# helper function to start and restart the game
def new_game():
    # Global Variables
    global high, counter, secret_number
    secret_number = random.randrange(0, high)
    print("")
    print("A new game has been started with a range [0," + str(high) + ")") 
    print("Number of remaining guesses: " + str(counter)) 
    
def restart() :
    global high, counter
    if high == 100 :
        counter = 7
    elif high == 1000 :
        counter = 10   
    print("")
    print("The game has been restarted ") 
    new_game()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high, counter
    high = 100
    counter = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high, counter
    high = 1000
    counter = 10
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global high,counter
    guess = int(guess)
    counter += -1  
    print("")
    print("Guess was " + str(guess))
    print("Number of remaining guesses: " + str(counter))
    
    if counter > 0 :        
        if guess < secret_number :
            print("Try a Higher guess!!")                 
        elif guess > secret_number :
            print("Try a Lower guess!!") 
         
    if counter == 0 :
        if guess == secret_number :
            print("You selected the correct number")
        else :
            print("You lost, the secret number was " + str(secret_number) + ". Try again")
        high = 100
        counter = 7
        new_game()
    
        
# create frame
frame = simplegui.create_frame("Guess the number", 400, 150)

# register event handlers for control elements and start frame
button0 = frame.add_button('Restart', restart,130 )
button1 = frame.add_button('Range is [0,100) ', range100,130 )
button2 = frame.add_button('Range is [0,1000)', range1000,130 )
button3 = frame.add_input('Input Guess', input_guess,100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
