# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
num=7
maxnum=100
secret_number=0
count = 0

# helper function to start and restart the game
def new_game():
    global maxnum
    global num
    global secret_number
    secret_number = random.randrange(0,maxnum)
    print "NEW GAME! Guess range is 1 to " + str(maxnum)
    print "Number of remaining guesses is " +str(num)
    
    
    
#def new_game1():
    #global secret_number
    #global num
    #secret_number = random.randrange(0,100)
    #num = 7
#def new_game2():
    #global secret_number
    #secret_number = random.randrange(0,1000)
    #num = 10

    
    # initialize global variables used in your code here
    
# define event handlers for control panel
def range100():
    #new_game1()
    global num
    global maxnum
    global secret_number
    secret_number = random.randrange(0,maxnum)
    maxnum=100
    num = 7
    print "NEW GAME! Guess range is 1 to " + str(maxnum)
    print "Number of remaining guesses is " +str(num)
    
def range1000():
    #new_game2()
    global num
    global maxnum
    global secret_number
    secret_number = random.randrange(0,maxnum)
    maxnum=1000
    num = 10
    print secret_number
    print "NEW GAME! Guess range is 1 to " + str(maxnum)
    print "Number of remaining guesses is " +str(num)
 
    
   
   
    # button that changes the range to [0,1000) and starts a new game         
def input_guess(guess):
    # main game logic goes here	
    global value
    global num
    global count
    value = int(guess)
    if num > 0:
        num = num - 1
        count=count+1
    else:
        print "You are out of guesses!"
        num=num+count
        count = 0
        new_game()
        
        
    print "Guess was " + str(value)
    print "Number of remaining guesses is " + str(num)
    if value < secret_number:
        print "Higher!"
    elif value > secret_number:
        print "Lower!"
    else:
        print "Correct!"
        num=num+count
        count = 0
        new_game()
        
        
        
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100]",range100,200)
frame.add_button("Range is [0,1000]",range1000,200)
frame.add_input("Enter value",input_guess,100)

# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
