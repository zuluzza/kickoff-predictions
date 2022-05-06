# https://en.wikipedia.org/wiki/Kelly_criterion
class KellyCriterion():
    # calculate amount to be bet on a single bet, considering odds, winning probability and bankroll.
    # if bankroll is not provided, the return value is percentage of bankroll to bet
    def calculate(self, win_probability, odds, bankroll=1.0):
        q = 1 - win_probability
        b = odds - 1
        return bankroll * (win_probability - (q / b))

    # returns true if 
    # note that the real EV depends accuracy of win_probability
    def isPositiveEVBet(self, win_probability, odds):
        return self.calculate(win_probability, odds) > 0.0
