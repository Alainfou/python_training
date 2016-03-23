from random import randint

# Variables (board, board size, number of turns):
sea = []
sea_size = 0
turns = 0

# Function to print the current board game:
def print_game(sea):
    print "_"+"__"*(sea_size+1)
    for row in sea:
        print "| "+" ".join(row)+" |"
    print "="+"=="*(sea_size+1)

# Functions to choose a random column or row index:
def random_row(sea):
    return randint(0, len(sea) - 1)

def random_col(sea):
    return randint(0, len(sea[0]) - 1)

# Welcome message :
print "Hello, and welcome to my Battleship game!"

# Get input (size of the square sea):
while sea_size not in range(5,11):
	sea_size = int(raw_input("Size of your board game (from 5 to 10): "))

# Create a square sea:
for x in range(sea_size):
    sea.append(["~"] * sea_size)

# Create a single ship, hidden in the sea:
ship_row = random_row(sea)
ship_col = random_col(sea)

# Get input (number of turns):
while turns not in range(1,10):
	turns = int(raw_input("Number of turns (from 1 to 10): "))

# Repeat for each turn:
for turn in range(0,turns):
    # Print the number of turns left (but counts from 0):
    print "Turns left: ",turns-turn
    # Print the game at every turn:
    print_game(sea)

    # Get the input (row and column):
    guess_row = int(raw_input('Guess row (from 0 to '+str(sea_size-1)+'): '))
    guess_col = int(raw_input('Guess column (from 0 to '+str(sea_size-1)+'): '))
    
    # Check the input:
    if guess_row not in range(0,sea_size) or \
    guess_col not in range(0,sea_size) :
        print "Wow dude, you're so high, that's not even in the sea..."

    # If the selected index matches, you won!
    elif guess_row == ship_row and guess_col == ship_col:
        print "Damn'! You sunk my battleship..."
        break
    # If the index is in the board game but not the ship,
    # check if it has been tried already or mark it as tried:
    else:
        if(sea[guess_row][guess_col] == "O"):
            print "You tried here already, too bad!"
        else:
            print "Missed! Eh eh!"
            sea[guess_row][guess_col] = "O"

# Will print in every cases:
sea[ship_row][ship_col] = "X"
print_game(sea)
print " ~ Thanks for playing Battleship! ~ "
