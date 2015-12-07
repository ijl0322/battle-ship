import random

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    """Displays the board    
    board: a list
    """    
    for row in board:
        print " ".join(row)

class ship(object):
    
    """Instantiate a ship instance with three adjacent coordinates
    coordinate_one, coordinate_two, and coordinate_three are list of length 2."""
        
    def __init__(self, coordinate_one, coordinate_two, coordinate_three):
        self.coordinate_one = coordinate_one
        self.coordinate_two = coordinate_two
        self.coordinate_three = coordinate_three
    def get_coord_one(self):
        return self.coordinate_one
    def get_coord_two(self):
        return self.coordinate_two
    def get_coord_three(self):
        return self.coordinate_three

def set_ship_coord():
    """Stochastically decides if the ship will be placed vertically or horizontally.
    """
    vertical_or_horizontal = random.choice([0,1])
    if vertical_or_horizontal == 0:
        #Sets ship vertically
        coordinate_one = [(random.randint(0, len(board) - 3)), (random.randint(0, len(board[0]) - 1))]
        coordinate_two = [(coordinate_one[0] + 1), (coordinate_one[1])]
        coordinate_three = [(coordinate_one[0] + 2), (coordinate_one[1])]
    else: 
        #Sets ship horizontally
        coordinate_one = [(random.randint(0, len(board) - 1)), (random.randint(0, len(board[0]) - 3))]
        coordinate_two = [(coordinate_one[0] ), (coordinate_one[1]) + 1]
        coordinate_three = [(coordinate_one[0] ), (coordinate_one[1]) + 2]
    
    return ship(coordinate_one, coordinate_two, coordinate_three)

def display_ship(ship):
    """
    Shows the ship on the board
    ship: a instance of the ship class
    """
    board[ship.get_coord_one()[0]][ship.get_coord_one()[1]] = "S"
    board[ship.get_coord_two()[0]][ship.get_coord_two()[1]] = "S"
    board[ship.get_coord_three()[0]][ship.get_coord_three()[1]] = "S"
    print_board(board)

print "Hi! Let's play Battleship!"
print "You will have 5 turns to sink my ship!"

ship = set_ship_coord()

for turn in range(5):
    
    """The player has 5 turns to guess the location of the ship. 
    For each turn, the player will have the chance to enter a colum and a row. 
    If the player guesses correctly, the player wins. 
    Otherwise, the guessed location will be marked as "X". 
    The player looses if he/she did not guess the location of the ship correctly when the turns end.
    """
    
    print "--------------------"
    print_board(board)
    print 
    print "Turn", turn + 1 

    guess_col = int(raw_input("Guess Col:"))-1
    guess_row = int(raw_input("Guess Row:"))-1

    if guess_row == ship.get_coord_one()[0] and guess_col == ship.get_coord_one()[1]\
    or guess_row == ship.get_coord_two()[0] and guess_col == ship.get_coord_two()[1]\
    or guess_row == ship.get_coord_three()[0] and guess_col == ship.get_coord_three()[1]:
        print "Congratulations! You sunk my battleship!"
        print "The ship was at: "
        break
    else:
        if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):
            print "Hey! That's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Oops, You missed my battleship!"
            board[guess_row][guess_col] = "X"
    if turn == 4:
        print "Game Over"
        print "The ship was at: "
        
display_ship(ship)