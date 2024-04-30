import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.positions = []

    def generate_positions(self, board_size, start_row, start_col, horizontal):
        if horizontal:
            self.positions = [(start_row, start_col + i) for i in range(self.size)]
        else:
            self.positions = [(start_row + i, start_col) for i in range(self.size)]

class Player:
    def __init__(self, name):
        self.name = name
        self.board_size = 8
        self.board = [['~' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = [Ship(5), Ship(4), Ship(3), Ship(3), Ship(2)]

    def place_ships(self):
        print(f"{self.name}, place your ships on the board.")
        for ship in self.ships:
            print(f"Placing ship of size {ship.size}")
            while True:
                try:
                    start_row = int(input("Enter starting row (0 - {}): ".format(self.board_size - 1)))
                    start_col = int(input("Enter starting column (0 - {}): ".format(self.board_size - 1)))
                    horizontal = input("Place horizontally? (y/n): ").lower() == 'y'
                    if not (0 <= start_row < self.board_size and 0 <= start_col < self.board_size):
                        raise ValueError
                    ship.generate_positions(self.board_size, start_row, start_col, horizontal)
                    # Check if ship positions are valid
                    for row, col in ship.positions:
                        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
                            raise ValueError
                        if self.board[row][col] != '~':
                            raise ValueError("Position already occupied.")
                    # Place ship on board
                    for row, col in ship.positions:
                        self.board[row][col] = 'S'
                    break
                except (ValueError, IndexError) as e:
                    print("Invalid input. Please try again.")

    def display_own_board(self):
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))

    def display_opponent_board(self, opponent):
        print("Opponent's Board:")
        for row in opponent.board:
            print(" ".join(row))

    def valid_shot(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '~'

    def fire_shot(self, row, col, opponent):
        if opponent.board[row][col] == 'S':
            opponent.board[row][col] = 'X'
            for ship in opponent.ships:
                if (row, col) in ship.positions:
                    ship.positions.remove((row, col))
                    if len(ship.positions) == 0:
                        print("You sunk a ship!")
                        opponent.ships.remove(ship)
                        if len(opponent.ships) == 0:
                            print("Congratulations, you win!")
                            return True
            print("Hit!")
        else:
            print("Miss!")
            self.board[row][col] = 'O'
        return False

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")

    def fire_shot(self, opponent):
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        while not self.valid_shot(row, col):
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
        print(f"{self.name} fires at row {row}, col {col}:")
        return super().fire_shot(row, col, opponent)

def play_battleship():
    print("Welcome to Battleship!")
    player = Player(input("Enter your name: "))
    player.place_ships()
    computer = ComputerPlayer()

    while True:
        player.display_own_board()
        player.display_opponent_board(computer)
        row = int(input("Enter row to fire at: "))
        col = int(input("Enter col to fire at: "))
        if player.fire_shot(row, col, computer):
            break

        if computer.fire_shot(player):
            break

play_battleship()
