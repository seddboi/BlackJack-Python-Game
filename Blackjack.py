from Classes.Game import *
from Classes.Dealer import *
from Classes.Card import *


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
    d1.shuffle_deck()

    d1.deal_card("user")
    print("Your first card: " + c1.format_card(g1.users_hand[-1]))
    d1.deal_card("dealer")
    print("Dealers first card: " + c1.format_card(g1.dealers_hand[-1]))
    d1.deal_card("user")
    print("Your second card: " + c1.format_card(g1.users_hand[-1]))
    d1.deal_card("dealer")

    print("---------------------------------------")
    print(
        "Dealer's hand: " + d1.format_hand(g1.dealers_hand).split(" ")[0] + " [hidden]"
    )
    print("Your hand: " + d1.format_hand(g1.users_hand))

    user_score = sum([x["value"] for x in g1.users_hand])
    dealer_score = sum([x["value"] for x in g1.dealers_hand])

    while True:
        print("\n")

        choice = input(
            'How would you like to continue? [enter "hit" or "stay"]:'
        ).lower()
        if choice == "hit":
            d1.deal_card("user")
            user_score = sum([x["value"] for x in g1.users_hand])
            print("You were dealt a: " + c1.format_card(g1.users_hand[-1]))
            print("Your new hand is: " + d1.format_hand(g1.users_hand))
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
            break
        elif user_score == 21:
            print("BLACKJACK! You received a perfect score! You win!")
            break

    while dealer_score < 17:
        d1.deal_card("dealer")
        user_score = sum([x["value"] for x in g1.users_hand])
        dealer_score = sum([x["value"] for x in g1.dealers_hand])
        if user_score <= 21:
            print("Dealer collects a: " + c1.format_card(g1.dealers_hand[-1]))
            if dealer_score > 17:
                print("Dealer reveals hand: " + d1.format_hand(g1.dealers_hand))
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


g1 = Game()
d1 = Dealer()
c1 = Card()

introduction()
