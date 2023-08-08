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

		dealer1.deal_card('user')
		print('Your first card: ' + card_class.format_card(game1.users_hand[-1]))
		dealer1.deal_card('dealer')
		print('Dealers first card: ' + card_class.format_card(game1.dealers_hand[-1]))
		dealer1.deal_card('user')
		print('Your second card: ' + card_class.format_card(game1.users_hand[-1]))
		dealer1.deal_card('dealer')

		
		print('---------------------------------------')
		print("Dealer's hand: " + dealer1.format_hand(game1.dealers_hand).split(' ')[0] + ' [hidden]')
		print('Your hand: ' + dealer1.format_hand(game1.users_hand))

		user_score = sum([x['value'] for x in game1.users_hand])
		dealer_score = sum([x['value'] for x in game1.dealers_hand])

		while True:
			print('\n')
			
			choice = input('How would you like to continue? [enter "hit" to receive another card, or "stay" to end your turn]: ').lower()
			if choice == 'hit':
				dealer1.deal_card('user')
				user_score = sum([x['value'] for x in game1.users_hand])
				print('You were dealt a: ' + card_class.format_card(game1.users_hand[-1]))
				print('Your new hand is: ' + dealer1.format_hand(game1.users_hand))
				print('\n')
			elif choice == 'stay':
				print('You ended your turn with a score of ' + str(user_score))
				print('\n')
				break
			else:
				print('Invalid entry. Please try again.')
				continue

			if user_score > 21:
				print('You ended with a score of ' + str(user_score))
				print('BUST! You lose! :(')
				break
			elif user_score == 21:
				print('BLACKJACK! You received a perfect score! You win!')
				break
		
		while dealer_score < 17:
			dealer1.deal_card('dealer')
			user_score = sum([x['value'] for x in game1.users_hand])
			dealer_score = sum([x['value'] for x in game1.dealers_hand])
			if (user_score <= 21):
				print('Dealer collects a: ' + card_class.format_card(game1.dealers_hand[-1]))
				if dealer_score > 17:
					print('Dealer reveals hand: ' + dealer1.format_hand(game1.dealers_hand))
			else:
				break
		
		if (user_score > 21):
			return
		else:
			if dealer_score > 21:
				print('You ended with a score of ' + str(user_score))
				print('Dealer ended with a score of ' + str(dealer_score))
				print('\n')
				print('YOU WIN! :)')
				print('\n')
			elif( user_score > dealer_score):
				print('You hand scores: ' + str(user_score))
				print("The Dealer's hand scores: " + str(dealer_score))
				print('\n')
				print('YOU WIN! :)')
				print('\n')
			elif user_score < dealer_score:
				print('You hand scores: ' + str(user_score))
				print("The Dealer's hand scores: " + str(dealer_score))
				print('\n')
				print('You lose :(')
				print('\n')
			else:
				print('You ended with a score of ' + str(user_score))
				print('Dealer ended with a score of: ' + str(dealer_score))
				print("It's a tie!")
		
class Dealer:	
	def shuffle_deck(self):
		random.shuffle(deck)

	def deal_card(self, is_user):
		selected_card = deck[0]
		deck.remove(selected_card)
		if (is_user == 'user'):
			game1.users_hand.append(selected_card)
		else:
			game1.dealers_hand.append(selected_card)
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