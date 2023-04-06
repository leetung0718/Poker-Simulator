from card import Card
import random


class Deck:
    def __init__(self):
        self._deck = []
        for suite in Card.static_suites:
            for value in Card.static_cardvalues:
                self._deck.append(Card(value, suite))

    def shuffle(self):
        """random shuffle 1~5 times"""
        for _ in range(random.randint(1, 5)):
            random.shuffle(self._deck)

    def get_cards(self):
        """return list of cards in deck"""
        return self._deck

    def dealcard(self):
        """give a card from deck"""
        return self._deck.pop()

    def remove(self, *args):
        for card in args:
            self._deck.remove(card)
        return self._deck

    def __len__(self):
        return len(self._deck)

    def __str__(self) -> str:
        return " ".join([str(card) for card in self._deck])


if __name__ == "__main__":

    deck = Deck()

    print(deck.get_cards)
    print("-"*10 + ' shuffle ' + "-"*10)
    deck.shuffle()
    print(str(deck))
    print("-"*10 + ' deal a card ' + "-"*10)
    print(deck.dealcard())
    print("-"*10 + ' left card in deck ' + "-"*10)
    print(len(deck))
