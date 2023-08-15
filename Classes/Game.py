cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♦", "♣"]
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = [
    {"card": c, "suit": s, "value": v} for [c, v] in zip(cards, values) for s in suits
]


class Game:
    def __init__(self):
        self.dealers_hand = []
        self.users_hand = []
        self.game_deck = deck
