class Soft:
    def __init__(self, Total, Player, Dealer):
        self.total = Total
        self.player = Player
        self.dealer = Dealer

    def DoubleOrStand(self):

        # double or stand 
        if self.player == 8 and self.dealer == 6:
            print("double or stand")
            return None

        if self.player == 7 and 2 <= self.player <= 6:
            print("double or stand")
            return None

        # Double 
        if self.dealer == 6 and 2 <= self.player <=6:
            print("double is recommended.")
            return None

        if self.dealer == 5 and 2 <= self.player <=6:
            print("double is recommended.")
            return None

        if self.dealer == 4 and 4 <= self.player <=6:
            print("double is recommended.")
            return None

        if self.dealer == 3 and self.player == 6:
            print("double is recommended.")
            return None

        # Stands

        if self.player >= 9 and self.player >= 8:
            print("stand")
            return None

        if self.player == 7 and 7 <= self.dealer <= 8:
            print("stand")
            return None






















