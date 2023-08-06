import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♥', '♦', '♣']
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = [{'card':c,'suit':s,'value':v} for [c,v] in zip(cards, values) for s in suits]

class Game:
	def __init__(self):
		self.dealers_hand = []
		self.users_hand = []
		self.game_deck = deck
	
	def game_start(self):
		dealer1.shuffle_deck()
		
		# ****************************
		# REduce 19-31 and make deal_card dictribute the card, remove from the deck, and append to user/dealers hand
		# have it spit out a printable line describing first card, second card, etc (use class ids!)
		user_card1 = dealer1.deal_card()
		dealer_card1 = dealer1.deal_card()
		user_card2 = dealer1.deal_card()
		dealer_card2 = dealer1.deal_card()

		game1.users_hand.append(user_card1)
		print('Your first card: ' + card_class.format_card(user_card1))
		game1.dealers_hand.append(dealer_card1)
		print('Dealers first card: ' + card_class.format_card(dealer_card1))
		game1.users_hand.append(user_card2)
		print('Your second card: ' + card_class.format_card(user_card2))
		game1.dealers_hand.append(dealer_card2)

		print('---------------------------------------')
		print("Dealer's hand: " + dealer1.format_hand(game1.dealers_hand).split(' ')[0] + ' [hidden]')
		print('Your hand: ' + dealer1.format_hand(game1.users_hand))

class Dealer:	
	def shuffle_deck(self):
		random.shuffle(deck)

	def deal_card(self):
		selected_card = deck[0]
		deck.remove(selected_card)
		return selected_card
	
	def format_hand(self, current_hand):
		user_hand_string = ''
		for card in current_hand:
			if (card == current_hand[-1]):
				user_hand_string += card_class.format_card(card)
			else:
				user_hand_string += card_class.format_card(card) + ', '
		return user_hand_string

class User:
	pass

class Card:
	def format_card(self, card_dict):
		return card_dict['card'] + card_dict['suit']

game1 = Game()
dealer1 = Dealer()
player_class = User()
card_class = Card()

game1.game_start()