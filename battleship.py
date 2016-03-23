from random import randint

sea = []
sea_size = 0
turns = 0

def print_game(sea):
    print "_____________"
    for row in sea:
        print "| "+" ".join(row)+" |"
    print "============="

def random_row(sea):
    return randint(0, len(sea) - 1)

def random_col(sea):
    return randint(0, len(sea[0]) - 1)

ship_row = random_row(sea)
ship_col = random_col(sea)

print "Hello, and welcome to my Battleship game!"
print_game(sea)

while sea_size not in range(5,11):
	sea_size = int(raw_input("Size of your board game (from 5 to 10): "))

for x in range(sea_size):
    board.append(["~"] * sea_size)

while turns not in range(1,10):
	turns = int(raw_input("Number of turns (from 1 to 10): "))

for turn in range(0,turns):
    print "Turns left: ",turns-turn
    guess_row = int(raw_input("Guess row (from 0 to "+sea_size+": "))
    guess_col = int(raw_input("Guess column (from 0 to "+sea_size+": "))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Damn'! You sunk my battleship..."
        break
    else:
        if guess_row not in range(0,sea_size) or \
        guess_col not in range(0,sea_size) :
            print "Wow dude, you're so high, that's not even in the sea..."
        elif(board[guess_row][guess_col] == "X"):
            print "You tried here already, too bad!"
        else:
            print "Missed! Eh eh!"
            board[guess_row][guess_col] = "O"
        print_board(board)
print "Game's over! ;)"
