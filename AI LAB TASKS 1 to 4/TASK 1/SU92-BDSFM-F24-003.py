import random
import pandas as pd

class Tile:
    def __init__(self, value=0):
        self.value = value

    def is_empty(self):
        return self.value == 0

    def double(self):
        self.value *= 2
        return self.value

    def __str__(self):
        return f"{self.value}" if self.value != 0 else " "


class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[Tile() for _ in range(size)] for _ in range(size)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_tiles = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c].is_empty()]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.grid[r][c] = Tile(2 if random.random() < 0.9 else 4)

    def compress(self):
        changed = False
        new_grid = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
        for r in range(self.size):
            col = 0
            for c in range(self.size):
                if not self.grid[r][c].is_empty():
                    new_grid[r][col] = self.grid[r][c]
                    if col != c:
                        changed = True
                    col += 1
        self.grid = new_grid
        return changed

    def merge(self):
        changed = False
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.grid[r][c].value == self.grid[r][c + 1].value and not self.grid[r][c].is_empty():
                    self.grid[r][c].double()
                    self.grid[r][c + 1] = Tile()
                    changed = True
        return changed

    def reverse(self):
        for r in range(self.size):
            self.grid[r] = self.grid[r][::-1]

    def transpose(self):
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_left(self):
        changed = self.compress()
        merged = self.merge()
        self.compress()
        return changed or merged

    def move_right(self):
        self.reverse()
        moved = self.move_left()
        self.reverse()
        return moved

    def move_up(self):
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        self.transpose()
        moved = self.move_right()
        self.transpose()
        return moved

    def can_move(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c].is_empty():
                    return True
                if r < self.size - 1 and self.grid[r][c].value == self.grid[r + 1][c].value:
                    return True
                if c < self.size - 1 and self.grid[r][c].value == self.grid[r][c + 1].value:
                    return True
        return False

    def has_2048_tile(self):
        for row in self.grid:
            if any(tile.value == 2048 for tile in row):
                return True
        return False

    def display_board(self):
        for row in self.grid:
            print("+----" * self.size + "+")
            print("".join(f"| {tile} " for tile in row) + "|")
        print("+----" * self.size + "+")


class Game:
    def __init__(self):
        self.board = Board()
        self.is_game_over = False
        self.is_game_won = False

    def play(self):
        while not self.is_game_over:
            self.board.display_board()
            move = input("Enter move (w: up, s: down, a: left, d: right, q: quit): ").strip().lower()
            if move == "q":
                print("Thanks for playing!")
                break
            elif move in "wasd":
                moved = False
                if move == "w":
                    moved = self.board.move_up()
                elif move == "s":
                    moved = self.board.move_down()
                elif move == "a":
                    moved = self.board.move_left()
                elif move == "d":
                    moved = self.board.move_right()

                if moved:
                    self.board.add_new_tile()

                if self.board.has_2048_tile():
                    print("Congratulations! You've reached 2048!")
                    self.is_game_won = True
                    break

                if not self.board.can_move():
                    print("Game over! No more moves available.")
                    self.is_game_over = True
                    break
            else:
                print("Invalid move! Please try again.")


class GameDisplay:
    @staticmethod
    def welcome_message():
        print("Welcome to 2048!")
        print("Combine tiles with the same number to reach 2048.")
        print("Controls: 'w' = up, 's' = down, 'a' = left, 'd' = right, 'q' = quit\n")

    @staticmethod
    def show_board(board):
        for row in board.grid:
            print("+----" * len(row) + "+")
            for tile in row:
                print(f"| {str(tile.value).center(4)}", end=" ")
            print("|")
        print("+----" * len(board.grid[0]) + "+")


# Main Game Execution
def main():
    GameDisplay.welcome_message()
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
