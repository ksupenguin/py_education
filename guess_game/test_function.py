from guess_game import function_guess as f
from guess_game.validation_for_guessgame import validation

low, high = validation()
f.game(low, high)
