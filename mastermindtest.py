import unittest
import mastermind


class TestMastermind(unittest.TestCase):
    def test_not_a_number(self):
        game1 = mastermind.mastermind()
        game2 = mastermind.oszustMastermind()
        self.assertEqual(game1.userInputGuess("g"), -1)
        self.assertEqual(game2.userInputGuess("g"), -1)

    def test_too_short_or_too_long(self):
        game1 = mastermind.mastermind()
        game2 = mastermind.oszustMastermind()
        self.assertEqual(game1.userInputGuess("11"), -1)
        self.assertEqual(game2.userInputGuess("11"), -1)
        self.assertEqual(game1.userInputGuess("111111"), -1)
        self.assertEqual(game2.userInputGuess("111111"), -1)

    def test_not_a_num_1111_to_6666(self):
        game1 = mastermind.mastermind()
        game2 = mastermind.oszustMastermind()
        self.assertEqual(game1.userInputGuess("7777"), -1)
        self.assertEqual(game2.userInputGuess("7777"), -1)

    def test_bad_guess(self):
        game1 = mastermind.mastermind()
        game1._mastermind__solution = [1, 1, 1, 1]
        self.assertEqual(game1.userInputGuess("2222")[0], 0)
        self.assertEqual(game1.userInputGuess("2222")[1], 0)

    def test_almost_good_guess_wrong_place(self):
        game1 = mastermind.mastermind()
        game1._mastermind__solution = [1, 1, 3, 3]
        self.assertEqual(game1.userInputGuess("2211")[1], 2)

    def test_good_guess_wrong_place(self):
        game1 = mastermind.mastermind()
        game1._mastermind__solution = [1, 2, 3, 4]
        self.assertEqual(game1.userInputGuess("1243")[0], 2)
        self.assertEqual(game1.userInputGuess("1243")[1], 2)

    def test_good_guess_(self):
        game1 = mastermind.mastermind()
        game1._mastermind__solution = [1, 2, 3, 4]
        self.assertEqual(game1.userInputGuess("1234"), "wygrana")

    def test_defeat(self):
        game1 = mastermind.mastermind()
        game1._mastermind__solution = [1, 2, 3, 4]
        for i in range(11):
            game1.userInputGuess("1111")

        self.assertEqual(game1.userInputGuess("1111")[2], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
