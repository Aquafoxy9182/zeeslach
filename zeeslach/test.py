# Import
import re

# Function to initialize the board
def initialize_board():
    return [[" "]*10 for _ in range(10)]

# Function to display the board
def display_board(board):
    letters = "ABCDEFGHIJ"
    print("   1  2  3  4  5  6  7  8  9 10")
    for i in range(10):
        print(letters[i], end=" ")
        for j in range(10):
            print("|", board[i][j], end=" ")
        print("|")

# Function to get input from the user for boat placement
def get_boat_location(size):
    letters = "ABCDEFGHIJ"
    while True:
        location = input(f"Enter location for boat (size {size}): ").upper()
        if not re.match("^[A-J][1-9]|10$", location):
            print("Invalid location. Please enter a location like 'A1' or 'J10'.")
            continue
        row, col = letters.index(location[0]), int(location[1:]) - 1
        return row, col

# Function to place a boat on the board
def place_boat(board, row, col, size):
    for i in range(size):
        if board[row][col+i] != " ":
            print("Boat placement overlaps with another boat. Please try again.")
            return False
    for i in range(size):
        board[row][col+i] = "O"
    return True

# Main function to start the game
def start_game():
    board = initialize_board()
    display_board(board)
    for size in range(1, 5):
        print(f"Placing boat of size {size}")
        while True:
            row, col = get_boat_location(size)
            if place_boat(board, row, col, size):
                break
        display_board(board)

# Main program
def main():
    # Player selection
    while True:
        num_players = input("Enter the number of players (1 or 2): ")
        if num_players == "1":
            start_game()
            break
        elif num_players == "2":
            print("Two player mode is not yet implemented.")
            continue
        else:
            print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

