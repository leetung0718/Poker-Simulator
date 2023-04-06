class Card:
    # define poker card
    static_suites = ["Heart", "Club", "Diamond", "Spade"]
    static_cardvalues = [str(n)
                         for n in range(2, 10)] + ["T", "J", "Q", "K", "A"]

    def __init__(self, value, suite):
        if suite not in Card.static_suites:
            raise ValueError("Invalid suite " + suite)
        if value not in Card.static_cardvalues:
            raise ValueError("Invalid card value " + value)
        # each card perpority
        self.suite = suite
        self.value = value

    # basic function
    def __sub__(self, other):
        """subtract rank / positional value of cards, positive result means left operand higher card than right"""
        if self.value == "A" and other.value == "2":
            return -1
        if self.value == "2" and other.value == "A":
            return 1
        return Card.static_cardvalues.index(self.value) - Card.static_cardvalues.index(other.value)

    def __gt__(self, other):
        """is this (self) card higher than other card"""
        return Card.static_cardvalues.index(self.value) > Card.static_cardvalues.index(other.value)

    def __ge__(self, other):
        """is this (self) card higher or equal to other card"""
        return Card.static_cardvalues.index(self.value) >= Card.static_cardvalues.index(other.value)

    def __lt__(self, other):
        """is this (self) card lower than other card"""
        return Card.static_cardvalues.index(self.value) < Card.static_cardvalues.index(other.value)

    def __le__(self, other):
        """is this (self) card lower or equal to other card"""
        return Card.static_cardvalues.index(self.value) < Card.static_cardvalues.index(other.value)

    def __eq__(self, other):
        """is this (self) card equal to other card"""
        return Card.static_cardvalues.index(self.value) == Card.static_cardvalues.index(other.value)

    # print card
    def __str__(self):
        match self.suite:
            case "Heart": return self.value + '\u2665'
            case "Club": return self.value + '\u2663'
            case "Spade": return self.value + '\u2660'
            case "Diamond": return self.value + '\u2666'
            case _: raise ValueError("Invalid card suite")

    def __repr__(self) -> str:
        return str(self)

    def compare(self, other):
        """
        Param
        ----------------------------
        other: Card object

        Return
        ----------------------------
        0 if same
        1 if greater
        2 if smaller
        """
        if self > other:
            return 1
        elif self < other:
            return 2
        else:
            return 0


if __name__ == "__main__":

    card1 = Card("Q","Spade")
    card2 = Card("A", "Heart")

    print(card1)
    print(card2)
    print(card1 - card2)
    print(card1 > card2)
