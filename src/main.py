from board import Board
from game import Game

def main():
    board = Board()
    game = Game(board)
    game.start_screen()

if __name__ == "__main__":
    main()
