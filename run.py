import random

class BattleshipsGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 0
        self.num_ships = 0
        self.user_board = []
        self.computer_board = []
        self.user_ships = []
        self.computer_ships = []
        self.hidden_user_board = []
        self.hidden_computer_board = []
        
        if self.difficulty == "easy":
            self.board_size = 6
            self.num_ships = 6
        elif self.difficulty == "medium":
            self.board_size = 8
            self.num_ships = 8
        elif self.difficulty == "hard":
            self.board_size = 12
            self.num_ships = 12
        
        self.initialize_user_board()
        self.place_ships_user()
        self.initialize_computer_board()
        self.place_ships_computer()

    def initialize_user_board(self):
        for i in range(self.board_size):
            self.user_board.append([])
            self.hidden_user_board.append([])
            for j in range(self.board_size):
                self.user_board[i].append(".")
                self.hidden_user_board[i].append(".")
    
    def initialize_computer_board(self):
        for i in range(self.board_size):
            self.computer_board.append([])
            self.hidden_computer_board.append([])
            for j in range(self.board_size):
                self.computer_board[i].append(".")
                self.hidden_computer_board[i].append(".")

    def place_ships_user(self):
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.hidden_user_board[row][col] == ".":
                    self.user_ships.append((row, col))
                    self.hidden_user_board[row][col] = "S"
                    placed = True


    def place_ships_computer(self):
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.hidden_computer_board[row][col] == ".":
                    self.computer_ships.append((row, col))
                    self.hidden_computer_board[row][col] = "S"
                    placed = True

    def check_shot(self, row, col):
        if (row, col) in self.ships:
            self.user_board[row][col] = "X"
            self.hidden_user_board[row][col] = "X"
            return True
        else:
            self.board[row][col] = "M"
            self.hidden_user_board[row][col] = "M"
            return False

    def check_win(self):
        for row in self.hidden_user_board:
            if "S" in row:
                return False
        return True

    def print_user_board(self):
        print("Your board:")
        for row in self.user_board:
            print(" ".join(row))

    def print_computer_board(self):
        print("Computer's board:")
        for row in self.computer_board:
            print(" ".join(row))


def main():
    # Modified welcome message
    print("Welcome to Python CLI Battleships!\n---------------------------------------------------\nIn this game, you will try to sink the computer's battleships\n---------------------------------------------------\nEnter the row and column of the grid you want to attack.\n---------------------------------------------------\nThe computer will do the same to your battleships.\n---------------------------------------------------\nThe first player to sink all of the other player's battleships wins. Good luck!")
    # Flag to track whether user has quit the game
    quit = False
    while not quit:
        play = input("Do you want to play? (Y/N) ")
        if play.upper() == "Y":
            # Prompt user to re-enter difficulty level if invalid choice is made
            difficulty = ""
            while difficulty not in ["easy", "medium", "hard"]:
                difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()
            game = BattleshipsGame(difficulty)
            while not game.check_win():
                game.print_user_board()
                game.print_computer_board()
                
                # Check if player wants to quit
                row_input = input("Enter row (0-{}) or Q to quit: ".format(game.board_size - 1))
                if row_input.upper() == "Q":
                    print("Goodbye!")
                    break
                else:
                    row = int(row_input)
                    while row < 0 or row >= game.board_size:
                        print("Invalid row. Please enter a valid row.")
                        row = int(input("Enter row (0-{}): ".format(game.board_size - 1)))
                col_input = input("Enter column (0-{}) or Q to quit: ".format(game.board_size - 1))
                if col_input.upper() == "Q":
                    print("Goodbye!")
                    break
                else:
                    col = int(col_input)
                    while col < 0 or col >= game.board_size:
                        print("Invalid column. Please enter a valid column.")
                        col = int(input("Enter column (0-{}): ".format(game.board_size - 1)))
                    while col < 0 or col >= game.board_size:
                        print("Invalid column. Please enter a valid column.")
                        col = int(input("Enter column (0-{}): ".format(game.board_size - 1)))
                if game.check_shot(row, col):
                    print("Hit!")
                else:
                    print("Miss!")
                # Computer's turn
                placed = False
            while not placed:
                    comp_row = random.randint(0, game.board_size - 1)
                    comp_col = random.randint(0, game.board_size - 1)
                    if game.board[comp_row][comp_col] == "O":
                        if game.check_shot(comp_row, comp_col):
                            print("Computer hit your battleship!")
                        else:
                            print("Computer missed.")
                    placed = True
            # Print computer's board after each turn
                    game.print_computer_board()
                    if game.check_win():
                        game.print_user_board()
                        print("You won!")
                    else:
                        game.print_computer_board()
                        print("Computer won :(")

main()



