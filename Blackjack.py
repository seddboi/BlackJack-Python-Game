import random

from Classes.GameDeck import *
from Classes.Card import *

users_hand = []
dealers_hand = []
game_deck = deck


def play_again_prompt():
    while True:
        play_again_option = input('Play again? ("yes" or "no")').lower()
        if play_again_option == "yes":
            users_hand.clear()
            dealers_hand.clear()
            global game_deck
            game_deck = [
                {"card": c, "suit": s, "value": v}
                for [c, v] in zip(cards, values)
                for s in suits
            ]
            play_game()
            break
        elif play_again_option == "no":
            print("Goodbye :)")
            exit()
        else:
            print("Invalid entry. Please try again.")
            continue


def introduction():
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("*****   *       ***    ***   *   *      *   ***    ***   *   *")
    print("*    *  *      *   *  *   *  *  *       *  *   *  *   *  *  * ")
    print("*   *   *      *****  *      * *        *  *****  *      * *  ")
    print("*    *  *      *   *  *      *  *       *  *   *  *      *  * ")
    print("*    *  *      *   *  *   *  *   *  *   *  *   *  *   *  *   *")
    print("*****    ****  *   *   ***   *   *   ***   *   *   ***   *   *")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("\n")

    while True:
        user_start_choice = input('Ready to play? (enter "yes" or "no)').lower()
        if user_start_choice == "yes":
            play_game()
            break

        elif user_start_choice == "no":
            exit()

        else:
            print("Invalid input. Please try again")
            continue


def play_game():
    random.shuffle(game_deck)

    print("\n")
    deal_card("user")
    print("Your first card: " + Card().format_card(users_hand[-1]))
    deal_card("dealer")
    print("Dealers first card: " + Card().format_card(dealers_hand[-1]))
    deal_card("user")
    print("Your second card: " + Card().format_card(users_hand[-1]))
    deal_card("dealer")

    print("---------------------------------------")
    print("Dealer's hand: " + format_hand(dealers_hand).split(" ")[0] + " [hidden]")
    print("Your hand: " + format_hand(users_hand))

    user_score = sum([x["value"] for x in users_hand])
    dealer_score = sum([x["value"] for x in dealers_hand])

    while True:
        print("\n")

        choice = input(
            'How would you like to continue? [enter "hit" or "stay"]:'
        ).lower()
        if choice == "hit":
            deal_card("user")
            user_score = sum([x["value"] for x in users_hand])
            print("You were dealt a: " + Card().format_card(users_hand[-1]))
            print("Your new hand is: " + format_hand(users_hand))
            print("\n")
        elif choice == "stay":
            print("You ended your turn with a score of " + str(user_score))
            print("\n")
            break
        else:
            print("Invalid entry. Please try again.")
            continue

        if user_score > 21:
            print("You ended with a score of " + str(user_score))
            print("BUST! You lose! :(")
            print("\n")
            play_again_prompt()
            break
        elif user_score == 21:
            print("BLACKJACK! You received a perfect score! You win!")
            print("\n")
            play_again_prompt()
            break

    while dealer_score < 17:
        deal_card("dealer")
        user_score = sum([x["value"] for x in users_hand])
        dealer_score = sum([x["value"] for x in dealers_hand])
        if user_score <= 21:
            print("Dealer collects a: " + Card().format_card(dealers_hand[-1]))
            if dealer_score > 17:
                print("Dealer reveals hand: " + format_hand(dealers_hand))
        else:
            break

    if user_score > 21:
        return
    else:
        if dealer_score > 21:
            print("You ended with a score of " + str(user_score))
            print("Dealer ended with a score of " + str(dealer_score))
            print("\n")
            print("YOU WIN! :)")
            print("\n")
        elif user_score > dealer_score:
            print("You hand scores: " + str(user_score))
            print("The Dealer's hand scores: " + str(dealer_score))
            print("\n")
            print("YOU WIN! :)")
            print("\n")
        elif user_score < dealer_score:
            print("You hand scores: " + str(user_score))
            print("The Dealer's hand scores: " + str(dealer_score))
            print("\n")
            print("You lose :(")
            print("\n")
        else:
            print("You ended with a score of " + str(user_score))
            print("Dealer ended with a score of: " + str(dealer_score))
            print("It's a tie!")
    play_again_prompt()


def deal_card(is_user):
    selected_card = deck[0]
    deck.remove(selected_card)
    if is_user == "user":
        users_hand.append(selected_card)
    else:
        dealers_hand.append(selected_card)
    return selected_card


def format_hand(current_hand):
    user_hand_string = ""
    for card in current_hand:
        if card == current_hand[-1]:
            user_hand_string += Card().format_card(card)
        else:
            user_hand_string += Card().format_card(card) + ", "
    return user_hand_string


introduction()
