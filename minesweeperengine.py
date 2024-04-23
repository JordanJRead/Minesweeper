from random import randint

def make_random_ab(x_min, x_max, y_min, y_max):
    b = randint(x_min, x_max)
    a = randint(y_min, y_max)
    return [a, b]


class GameState:

    def __init__(self, width, height, mine_count):
        self.width = width
        self.height = height
        self.width_height_ratio = width / height
        self.mine_count = mine_count
        self.board = []
        for i in range(self.height):
            self.board.append([])
            for y in range(self.width):
                self.board[i].append(
                    "O"
                )  # O == open square3, X == mine (mines are added later)

        self.visible_board = []  # KEY: X = unknown tile
        #O = open tile
        for i in range(height):  # For every row
            self.visible_board.append([])  # make a list for that row
            for y in range(width):
                self.visible_board[i].append("XO")

        self.clean_visible_board = ""
        for i in range(
                height):  # Iterates through list (each row of the board)
            for y in self.visible_board[
                    i]:  # Iterates through the items in that row
                self.clean_visible_board += y
            self.clean_visible_board += "\n"  # Add a linebreak at the end of each row for readability

        self.mine_squares = []

        while len(self.mine_squares) != self.mine_count:
            mine = make_random_ab(0, self.width - 1, 0, self.height - 1)
            a = mine[0]
            b = mine[1]
            if mine not in self.mine_squares:
                self.mine_squares.append(mine)
                self.board[a][b] = "X"

        self.clean_board = ""  # This is a string that represents the board in a readable form
        for i in range(
                height):  # Iterates through list (each row of the board)
            for y in self.board[i]:  # Iterates through the items in that row
                self.clean_board += y
            self.clean_board += "\n"  # Add a linebreak at the end of each row for readability

    def make_clean_visible_board(self):
        self.clean_visible_board = ""
        for i in range(
                self.height):  # Iterates through list (each row of the board)
            for y in self.visible_board[
                    i]:  # Iterates through the items in that row
                self.clean_visible_board += y
            self.clean_visible_board += "\n"  # Add a linebreak at the end of each row for readability

    def number_board(self):  # Assignes numbers to squares
        mines = 0
        for a in range(self.height):
            for b in range(self.width):  # For each square
                if self.visible_board[a][b] == "OO":  # If it's an open tile
                    for i in self.get_surrounding_squares(
                        [a, b]):  # For every touching square
                        if self.board[i[0]][i[
                                1]] == "X":  # If the square next to it is a mine
                            mines += 1
                        self.visible_board[a][b] = str(mines) + "O"
                        
    def number_square(self, square_ab):
      mines = 0
      for i in self.get_surrounding_squares(square_ab):
        if self.board[i[0]][i[1]] == "X":
          mines += 1
      return mines

    def open_board(
            self
    ):  # Marks squares around a 0 as being opened ("OO"), numbers them
        for a in range(self.height):
            for b in range(self.width):  # For every square
                if self.visible_board[a][b][0] == "0":  # If that square is a 0
                    self.visible_board[a][b] = "EO"  # Mark it as being empty
                    for i in self.get_surrounding_squares(
                        [a, b]):  # Get surrounding squares
                        if self.visible_board[i[0]][
                                i[1]][0] == "X":  # If it is unmarked
                            self.visible_board[i[0]][i[
                                1]] = "OO"  # Mark the surrounding squares as being opened
                            self.number_board()  # Number the new open squares
                            self.open_board()

    def get_surrounding_squares(self, square_ab):
        a = square_ab[0]
        b = square_ab[1]
        squares = []
        # Up
        if a > 0:  # If there are squares above this square
            if b > 0:  # If squares on the left
                squares.append([a - 1, b - 1])  # Up left
            squares.append([a - 1, b])  # Up
            if b < self.width - 1:  # If there are square on the right
                squares.append([a - 1, b + 1])  # Up right
        # Sides
        if b > 0:
            squares.append([a, b - 1])  # Left
        if b < self.width - 1:
            squares.append([a, b + 1])  # Right
        # Down
        if a < self.height - 1:  # If there are squares below
            if b > 0:  # If there are squares to the left
                squares.append([a + 1, b - 1])  # Down left
            squares.append([a + 1, b])  # Down
            if b < self.width - 1:  # If there are squares on the right
                squares.append([a + 1, b + 1])
        return squares

    def make_board(self):
      self.board = []
      for i in range(self.height):
            self.board.append([])
            for y in range(self.width):
                self.board[i].append(
                    "O"
                )  # O == open square3, X == mine (mines are added later)
      self.mine_squares = []
      while len(self.mine_squares) != self.mine_count:
            mine = make_random_ab(0, self.width - 1, 0, self.height - 1)
            a = mine[0]
            b = mine[1]
            if mine not in self.mine_squares:
                self.mine_squares.append(mine)
                self.board[a][b] = "X"

    def is_won(self):
        for a in range(self.height):
                for b in range(self.width):
                    if self.visible_board[a][b][0] == "X" and [a, b] not in self.mine_squares: # Hidden tile
                        return False
        return True