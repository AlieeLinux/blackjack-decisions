class IsSurrender:
    def __init__(self, total, dealer) -> None:
        self.total = total
        self.dealer = dealer

    def SurOrNah(self):
        if self.total == 16 and 9 <= self.dealer <= 11:
            print("surrender")
            return None

        if self.total == 15 and self.dealer == 10:
            print("surrender")
        else:
            print("still safe")

