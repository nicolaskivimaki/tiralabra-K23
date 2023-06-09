import unittest
import pygame
from constants import *
from game import Game
from board import Board
import numpy as np

class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        board = Board()
        self.game = Game(board)

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertIsNotNone(self.game.board)
        self.assertIsNotNone(self.game.screen)
        self.assertIsNotNone(self.game.ai)
        self.assertIsNone(self.game.ai_token)
        self.assertIsNone(self.game.player_token)
        self.assertIsNone(self.game.ai_level)
        self.assertEqual(self.game.winner, "")
        self.assertEqual(self.game.width, COLUMN_COUNT * SQUARESIZE)
        self.assertEqual(self.game.height, (ROW_COUNT + 1) * SQUARESIZE)
        self.assertIsNone(self.game.ai_token)
        self.assertIsNone(self.game.player_token)
        self.assertEqual(self.game.game_state, "START")
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.turn, 0)

    def test_draw_board(self):
        self.game.draw_board()
        # Test if the board is drawn correctly

    def test_board_exists(self):
        empty_board = np.zeros((6, 7))
        self.assertEqual(empty_board.all(), self.game.board.board.all())

    def test_is_valid_location(self):
        self.game.board.drop_piece(1, 1, 1)

        # Test when the column is valid
        self.assertTrue(self.game.is_valid_location(1))

        # Test when the column is full
        for i in range(ROW_COUNT):
            self.game.board.drop_piece(i, 1, 1)
            print(self.game.board.board)

        self.assertFalse(self.game.is_valid_location(1))

        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertTrue(self.game.board.is_valid_location(1))

    def test_get_next_open_row(self):

        self.game.board.reset_board()
        print(self.game.board.board)

        # Test when the column is empty
        self.assertEqual(self.game.get_next_open_row(3), 0)

        # Test when the column has some pieces
        self.game.board.drop_piece(0, 1, 1)
        self.game.board.drop_piece(1, 1, 1)
        self.assertEqual(self.game.get_next_open_row(1), 2)

        # Test when column is full
        self.game.board.board = np.array([
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(self.game.board.get_next_open_row(0), None)

    def test_win(self):

        # Test horizontal win for player 1
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0]
        ])
        self.assertTrue(self.game.board.check_win(1))

        # Test horizontal win for player 2
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 0]
        ])
        self.assertTrue(self.game.board.check_win(2))

        # Test vertical win for player 1
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0]
        ])
        self.assertTrue(self.game.board.check_win(1))

        # Test vertical win for player 2
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0]
        ])
        self.assertTrue(self.game.board.check_win(2))

        # Test diagonal win for player 1
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0]
        ])
        self.assertTrue(self.game.board.check_win(1))

        # Test diagonal win for player 2
        self.game.board.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0]
        ])
        self.assertTrue(self.game.board.check_win(2))



if __name__ == "__main__":
    unittest.main()
