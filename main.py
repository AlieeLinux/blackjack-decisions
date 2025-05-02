import ast
from Decisions.processing import Game


def main():
    game = Game()
    
    first = get_input("first card: ")
    second = get_input("second card: ")
    dealer = get_input("dealer faced card: ")

#    hard.StandoHit()

    game.StartGame(card1=first, card2=second, dealer=dealer)


def get_input(prompt):
    user_input = input(prompt)
    try:
        # Try to evaluate the input safely
        result = ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        # If evaluation fails, fallback to string
        result = user_input
    return result






if __name__ == "__main__":
    while True:
        main()
