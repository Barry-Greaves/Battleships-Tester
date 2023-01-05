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
            self.board_size = 2
            self.num_ships = 2
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
                    self.user_board[row][col] = "S"
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

    def check_shot_user(self, row, col):
        if (row, col) in self.user_ships:
            self.computer_board[row][col] = "X"
            self.hidden_computer_board[row][col] = "X"
            return True
        else:
            self.computer_board[row][col] = "M"
            self.hidden_computer_board[row][col] = "M"
            return False

    def check_win_user(self):
        for row in self.hidden_computer_board:
            if "S" in row:
                return False
        return True

    def check_shot_computer(self, row, col):
        if (row, col) in self.user_ships:
            self.user_board[row][col] = "X"
            self.hidden_user_board[row][col] = "X"
            return True
        else:
            self.user_board[row][col] = "M"
            self.hidden_user_board[row][col] = "M"
            return False

    def check_win_computer(self):
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

    def computer_turn(self, row, col):
        placed = False
        while not placed:
            comp_row = random.randint(0, board_size - 1)
            comp_col = random.randint(0, board_size - 1)
        if user_board[comp_row][comp_col] == ".":
            user_board[comp_row][comp_col] = "X"
        else:
            user_board[comp_row][comp_col] = "M"
            placed = True
        return user_board


def main():
    # Modified welcome message
    print("Welcome to Python CLI Battleships!)
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

            while not game.check_win_user() and not game.check_win_computer():
                game.print_user_board()
                game.print_computer_board()

                # Check if player wants to quit
                row_input = input("Enter row (0-{}) ".format(game.board_size - 1))
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
                if game.check_shot_user(row, col):
                    print("Hit!")
                else:
                    print("Miss!")
            
            game.computer_turn(row, col)
            if game.check_shot_computer(row, col):
                print("Hit!")
            else:
                print("Miss!")

            # Print computer's board after each turn
   
            if game.check_win_user():
                game.print_user_board()
                print("You won!")
                break
            else:
                if game.check_win_computer():
                    print("Computer wins!")
                    break


main()


