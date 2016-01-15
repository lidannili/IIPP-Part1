# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name =='rock':
        num=0
    elif name=='Spock':
        num=1
    elif name=='paper':
        num=2
    elif name=='lizard':
        num=3
    elif name=='scissors':
        num=4
    else:
        print "wrong input"
    return num


    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        nam = 'rock'
    elif number==1:
        nam ='Spock'
    elif number==2:
        nam ='paper'
    elif number==3:
        nam ='lizard'
    elif number==4:
        nam ='scissors'
    else:
        print "wrong input"
    return nam

    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice):
    print ("Player chooses "+ player_choice)
    player_number=name_to_number(player_choice)
    import random
    comp_number=random.randrange(0,4)
    print ("Computer chooses "+ number_to_name(comp_number))
    a=(player_number-comp_number)%5
    if(a==1 or a==2):
        print "Player wins!"
    elif (a==3 or a==4):
        print "Computer wins!"
    else: 
        print "player and computer tie!"
    print("\n")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric


