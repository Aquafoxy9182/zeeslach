import random

# Functie om het bord te initialiseren
def initialize_board(size):
    board = []
    for _ in range(size):
        row = ['O'] * size
        board.append(row)
    return board

# Functie om het bord af te drukken
def print_board(board):
    for row in board:
        print(" ".join(row))

# Functie om een willekeurige positie op het bord te genereren
def generate_random_position(size):
    return random.randint(0, size - 1), random.randint(0, size - 1)

# Functie om het spel te spelen
def play_battleship(size, num_ships):
    board = initialize_board(size)

    # Plaats de schepen
    for _ in range(num_ships):
        x, y = generate_random_position(size)
        while board[x][y] == 'S':
            x, y = generate_random_position(size)
        board[x][y] = 'S'

    # Speel het spel
    while True:
        print("Huidige bord:")
        print_board(board)
        guess_x = int(input("Raad een rij (0-" + str(size - 1) + "): "))
        guess_y = int(input("Raad een kolom (0-" + str(size - 1) + "): "))

        if board[guess_x][guess_y] == 'S':
            print("Gefeliciteerd! Je hebt een schip geraakt!")
            board[guess_x][guess_y] = 'X'
        else:
            print("Helaas, geen schip op deze positie.")
            board[guess_x][guess_y] = '-'

        if all(all(cell != 'S' for cell in row) for row in board):
            print("Gefeliciteerd! Je hebt alle schepen gezonken!")
            break

# Start het spel
size = 5  # Grootte van het bord
num_ships = 3  # Aantal schepen
play_battleship(size, num_ships)
