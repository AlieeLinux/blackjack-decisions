from Decisions.hard import Hard
from Decisions.Soft import Soft
from Decisions.split import IsSplit
from Decisions.Surrender import IsSurrender
from Decisions.Chance import BlackjackSimulator
import os
import ast


def input_card(prompt):
    try:
        insert = input(prompt)
        result = ast.literal_eval(insert)
    except Exception:
        if insert.lower() == "a":
            result = 11
        elif insert == "":
            result = None
        else:
            result = 10
    return result

class Game:
    @staticmethod
    def StartGame(card1, card2, dealer):
    # Reinitialize


        isplayer1soft = False
        isplayer2soft = False

        if isinstance(card1, str):
            if str(card1).lower() == "a":
                isplayer1soft = True
                card1 = 11
            else:
                card1 = 10

        if isinstance(card2, str):
            if str(card2).lower() == "a":
                isplayer2soft = True
                card2 = 11
            else:
                card2 = 10

        if isinstance(dealer, str):
            if str(dealer).lower() == "a":
                dealer = 11
            else:
                dealer = 10

        totalhand = card1+card2
        os.system("clear")
        soft1 = Soft(totalhand, card1, dealer)
        soft2 = Soft(totalhand, card2, dealer)
        hard = Hard(totalhand, dealer)
        split = IsSplit(card1, dealer)
        surrender = IsSurrender(totalhand, dealer)
        chance = BlackjackSimulator()

        chanceofwinning = chance.chance_to_win(totalhand, dealer)
        chanceoflosing = chance.chance_of_losing_if_hit(totalhand)

        print("first card: ", card1)
        print("second card: ", card2, "\n\n")

        print("Total: ", totalhand, "\n\n")

        print("chance of winning: ", chanceofwinning)
        print("chance of losing If hit: ", chanceoflosing, "\n\n")

        print("surrender? ", end="")
        surrender.SurOrNah()

        if isplayer1soft and card1 != card2:
            print("Soft: ", card2 + 1, "/" , card2 + card1)
            print()
            soft1.DoubleOrStand()
        elif isplayer2soft and card1 != card2:
            print("Soft: ", card1 + 1, "/" , card2 + card1)
            print()
            soft2.DoubleOrStand()
        elif card1 == card2:
            print("Pair: ", card1)
            print()
            split.Decision()
        else:
            print("Hard: ", totalhand)
            print()
            hard.StandoHit()


        ishit = True

        print("dealer: ", dealer, "\n\n")

        while ishit:
            print("what Did you do stand=(click enter) , sp=split, type any number when u hit")
            action = input_card(">>")
            if isinstance(action, int):
                totalhand = totalhand + action
                print("Hard: ", totalhand)
                hard = Hard(totalhand, dealer)
                hard.StandoHit()
                chanceoflosing = chance.chance_of_losing_if_hit(totalhand)
                print("chance of winning: ", chanceofwinning)
                print("chance of losing If hit: ", chanceoflosing, "\n\n")
                if (totalhand) > 21:
                    os.system("clear")
                    print("Busttt\n\n\n")
                    ishit = False
                elif totalhand == 21:
                    os.system("clear")
                    print("lucky!!\n")
                    ishit = False
            elif action == "sp":
                os.system("clear")
                ishit = False
            elif isinstance(action, int):
                pass
            else:
                os.system("clear")
                ishit = False



