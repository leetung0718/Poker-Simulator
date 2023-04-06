from card import Card
from deck import Deck
from table import *
from tqdm import tqdm

# simulate
num_simulations = 1000

# p1
player1 = Player(name="player1")
card1 = Card("A", "Heart")
card2 = Card("A", "Diamond")
player1.add_card(card=card1)
player1.add_card(card=card2)

# p2
player2 = Player(name="player2")
card3 = Card("6", "Spade")
card4 = Card("2", "Spade")
player2.add_card(card=card3)
player2.add_card(card=card4)

players = [player1, player2]

# dict to track win/loss stats
hand_stats = {}
for p in players:
    c1, c2 = p._holeCards
    hand_stats[str(c1) + str(c2)] = 0

print(f"simulate {num_simulations} times")
for i in tqdm(range(num_simulations)):
    # define a deck of cards
    play_deck = Deck()
    play_deck.remove(card1, card2, card3, card4)
    play_deck.shuffle()
    assert len(play_deck) == 48

    play_deck.dealcard()  # burn before deal
    flop_cards = [play_deck.dealcard() for _ in range(3)]

    play_deck.dealcard()
    turn_card = [play_deck.dealcard()]

    play_deck.dealcard()
    river_card = [play_deck.dealcard()]

    table = flop_cards + turn_card + river_card

    for p in players:
        bh = p.update_best_hand(table)

    for p in winning_player(players):
        p_hand = p.get_holecards_pokernotation()
        c1, c2 = p._holeCards
        hand_stats[str(c1) + str(c2)] += 1

# update win_rate
for p in players:
    # p_hand = p.get_holecards_pokernotation()
    c1, c2 = p._holeCards
    win_times = hand_stats[str(c1) + str(c2)]
    hand_stats[str(c1) + str(c2)] = str(win_times) + \
        "(" + str(win_times/num_simulations) + "%)"

print(hand_stats)
print()
