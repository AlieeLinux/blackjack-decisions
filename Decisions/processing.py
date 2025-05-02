from Decisions.hard import Hard
from Decisions.Soft import Soft
from Decisions.split import IsSplit

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

        soft1 = Soft(totalhand, card1, dealer)
        soft2 = Soft(totalhand, card2, dealer)
        hard = Hard(totalhand, dealer)
        split = IsSplit(card1, dealer)

        if isplayer1soft and card1 != card2:
            soft1.DoubleOrStand()
        elif isplayer2soft and card1 != card2:
            soft2.DoubleOrStand()
        elif card1 == card2:
            split.Decision()
        else:
            hard.StandoHit()

#        print("what Did you do?")
#        action = input("(s, h, none/n \n>>")

















