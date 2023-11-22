import unittest
from logic import GameBoard, Player, TicTacToeGame  

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()

    def test_initial_board_empty(self):
        for row in self.board.board:
            for cell in row:
                self.assertIsNone(cell)

    def test_is_valid_move(self):
        self.assertTrue(self.board.is_valid_move(1, 1))
        self.board.make_move(1, 1, "X")
        self.assertFalse(self.board.is_valid_move(1, 1))

    def test_make_move(self):
        self.assertTrue(self.board.make_move(0, 0, "X"))
        self.assertEqual(self.board.board[0][0], "X")
        self.assertFalse(self.board.make_move(0, 0, "O"))



class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.player = Player("X")
        self.bot = Player("O", is_bot=True)

    def test_player_symbol(self):
        self.assertEqual(self.player.symbol, "X")

    def test_bot_symbol(self):
        self.assertEqual(self.bot.symbol, "O")

    def test_bot_move(self):
        x, y = self.bot.get_bot_move(self.board)
        self.assertTrue(self.board.is_valid_move(x, y))



class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_game_initialization(self):
        self.assertIsInstance(self.game.board, GameBoard)
        self.assertEqual(len(self.game.players), 2)

    def test_check_winner(self):
        self.game.board.board = [["X", "X", "X"], [None, None, None], [None, None, None]]
        self.assertTrue(self.game.check_winner("X"))

    def test_is_draw(self):
        self.game.board.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.assertTrue(self.game.is_draw())


if __name__ == '__main__':
    unittest.main()
