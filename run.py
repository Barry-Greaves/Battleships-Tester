import random

class BattleshipsGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 0
        self.num_ships = 0
        self.board = []
        self.ships = []
        self.hidden_board = []
        
        if self.difficulty == "easy":
            self.board_size = 4
            self.num_ships = 4
        elif self.difficulty == "medium":
            self.board_size = 6
            self.num_ships = 6
        elif self.difficulty == "hard":
            self.board_size = 8
            self.num_ships = 8
        
        self.initialize_board()
        self.place_ships()

    def initialize_board(self):
        for i in range(self.board_size):
            self.board.append([])
            self.hidden_board.append([])
            for j in range(self.board_size):
                self.board[i].append(".")
                self.hidden_board[i].append(".")

    def place_ships(self):
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.hidden_board[row][col] == ".":
                    self.ships.append((row, col))
                    self.hidden_board[row][col] = "S"
                    placed = True

    def check_shot(self, row, col):
        if (row, col) in self.ships:
            self.board[row][col] = "X"
            self.hidden_board[row][col] = "X"
            return True
        else:
            self.board[row][col] = "M"
            self.hidden_board[row][col] = "M"
            return False

    def check_win(self):
        for row in self.hidden_board:
            if "S" in row:
                return False
        return True

    def print_user_board(self):
        print("Your board:")
        for row in self.board:
            print(" ".join(row))

    def print_computer_board(self):
        print("Computer's board:")
        for row in self.hidden_board:
            print(" ".join(row))


def main():
    # Modified welcome message
    print("Welcome to Battleships! In this game, you will try to sink the computer's battleships by entering the row and column of the grid you want to attack. The computer will do the same to your battleships. The first player to sink all of the other player's battleships wins. Good luck! Enter Q at any time to quit.")
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
                # Check if player wants to quit
                row_input = input("Enter row (0-{}) or Q to quit: ".format(game.board_size - 1))
                if row_input.upper() == "Q":
                    print("Goodbye! Quitter.")
                    break
                else:
                    row = int(row_input)
                    while row < 0 or row >= game.board_size:
                        print("Invalid row. Please enter a valid row.")
                        row = int(input("Enter row (0-{}): ".format(game.board_size - 1)))
                col_input = input("Enter column (0-{}) or Q to quit: ".format(game.board_size - 1))
                if col_input.upper() == "Q":
                    print("Goodbye! Quitter.")
                    break
                else:
                    col = int(col_input)
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
    else:
        print("Goodbye!")

main()



