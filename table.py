from player import Player
from poker_rules import best_hand


def winning_player(players: Player):
    """
    given a list of player, return the winners who have the best poker hand

    :param player: list of [Player] objects
    :return: list of players that won
    :rtype: list[Player]
    """
    player_best_hands = [player.get_best_hand() for player in players]
    winning_hand = best_hand(player_best_hands)
    winners = [player for player in players if player.get_best_hand()
               == winning_hand]
    return winners
