import random
from Classes.Game import *
from Classes.Card import *


class Dealer:
    def shuffle_deck(self):
        random.shuffle(deck)

    def deal_card(self, is_user):
        selected_card = deck[0]
        deck.remove(selected_card)
        if is_user == "user":
            Game().users_hand.append(selected_card)
        else:
            Game().dealers_hand.append(selected_card)
        return selected_card

    def format_hand(self, current_hand):
        user_hand_string = ""
        for card in current_hand:
            if card == current_hand[-1]:
                user_hand_string += Card().format_card(card)
            else:
                user_hand_string += Card().format_card(card) + ", "
        return user_hand_string
