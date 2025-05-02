from Decisions.hard import Hard

class IsSplit:

    def __init__(self, card, dealer) -> None:
        self.card = card
        self.dealer = dealer
        self.cardtotal = self.card + self.card

    def Decision(self):

        if isinstance(self.card, str) or self.card == 11:
            print("Stand")
            return None
        if self.card == 8 or self.card != 11:
            print("Split is extremely recommended")
            return None

        self.card = int(self.card)
        if isinstance(self.dealer, str):
            if str(self.dealer).lower() == "a":
                self.dealer = 11
            elif str(self.dealer) != "a":
                self.dealer = 10
        self.dealer = int(self.dealer)

        # Split only das ############################################

        if self.dealer <=3 and self.card <= 3:
            print("split only if Double After Split is offered")
            return None

        if 5 <= self.dealer <= 6 and 4 <= self.card <=6:
            print("split only if Double After Split is offered")
            return None

        if self.card == 6 and self.dealer == 2:
            print("Split if Double After Split is offered")
            return None

        ##############################################################

        # Normal Split ###############################################

        if 4 <= self.dealer <= 7 and self.card <= 3:
            print("Split Is recomended")
            return None

        if 6 <= self.card <= 9 and self.dealer <= 6:
            print("Split is recommended")
            return None

        if 7 <= self.card <= 8 and self.dealer == 7:
            print("Split is recommended")
            return None

        if 8 <= self.dealer <= 9 and self.card == 9:
            print("Split is recommended")
            return None

        ##############################################################

        x = Hard(self.cardtotal, self.dealer)
        x.StandoHit()

        return False











