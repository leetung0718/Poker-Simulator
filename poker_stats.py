from card import Card
from itertools import combinations


def create_stats_dict(starting_hands_stats, stats_dict):
    """
    updated input dictionary with 169 keys representing the unique starting hands in poker
    each key maps to a nested statistics dictionary

    :param starting_hands_stats: empty dict
    :param stats_dict: {'won': 0, 'played': 0}
    :return: None
    """
    pocket_pairs = [card*2 for card in Card.static_cardvalues]
    # 13C2 = 78 two card combinations
    combos = list(combinations(Card.static_cardvalues, 2))
    # 78 suited two card combinations
    suited_hands = [b+a+'s' for a, b in combos]
    offsuite_hands = [b+a+'o' for a, b in combos]  # any two offsuite cards
    starting_hands_stats.update(
        {k: stats_dict.copy() for k in pocket_pairs + suited_hands + offsuite_hands})
