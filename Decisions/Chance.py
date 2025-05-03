import random

class BlackjackSimulator:
    def __init__(self, simulations=10000):
        self.simulations = simulations

    def draw_card(self):
        card = random.randint(1, 13)
        return min(card, 10)

    def simulate_dealer(self, dealer_card):
        total = dealer_card
        ace = 1 if dealer_card == 1 else 0

        while total < 17 or (total == 17 and ace and total + 10 <= 21):
            card = self.draw_card()
            if card == 1:
                ace += 1
            total += card
            while total > 21 and ace:
                total -= 10
                ace -= 1
        return total

    def chance_to_win(self, player_total, dealer_card):
        wins = 0
        for _ in range(self.simulations):
            if player_total > 21:
                continue
            dealer_total = self.simulate_dealer(dealer_card)

            if dealer_total > 21 or player_total > dealer_total:
                wins += 1
            elif player_total == dealer_total:
                wins += 0.5
        return round(wins / self.simulations, 2)

    def chance_of_losing_if_hit(self, player_total):
        losses = 0
        for _ in range(self.simulations):
            new_card = self.draw_card()
            new_total = player_total + new_card

            # Assume single ace logic only for simplicity
            if new_card == 1 and new_total + 10 <= 21:
                new_total += 10

            if new_total > 21:
                losses += 1

        return round(losses / self.simulations, 2)

