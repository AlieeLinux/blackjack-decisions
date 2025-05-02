class Hard:
    def __init__(self, player, dealer):
        self.PlayerTotal = player
        self.DealerTotal = dealer

    def StandoHit(self):
        if self.PlayerTotal <= 8:
            print("Hit!!")
            return None

        # Doubles 

        if self.PlayerTotal == 11:
            print("Double is recommended.")
            return None

        if 2 <= self.DealerTotal <=8 and self.PlayerTotal == 10:
            print("double is recommended.")
            return None

        if self.PlayerTotal == 9 and 3 <= self.DealerTotal <= 6:
            print("double is recommended")
            return None

        # Stands

        if self.PlayerTotal >= 17:
            print("stand!!")
            return None

        if 13 <= self.PlayerTotal <= 16 and 2 <= self.DealerTotal <= 6:
            print("Stand")
            return None

        if self.PlayerTotal == 12 and 4 <= self.DealerTotal <= 6:
            print("Risky Stand")
            return None

        print("hit!")
