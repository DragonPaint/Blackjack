import random
deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
numbers = 0
suits = ["S", "H", "D", "C"]
used = []
player = 0
player_name = []
player_cards = []
used_cards = [""]
player_cards_temp = 0


def blackjack_names():
    player_count = input("How many players?, not including the dealer/computer. ")
    for z in range(int(player_count)):
        player_name.append(input("What is player " + str(z + 1) + "'s name? "))
        print("Player " + str(z + 1) + "'s name is: " + player_name[z])
    blackjack_main(player_count)


def blackjack_main(player_count):
    player_cards = []
    used_cards = [""]
    computer_cards = []
    blackjack_new_card(player_cards_temp)
    computer_cards.append(player_cards_temp)
    blackjack_new_card(player_cards_temp)
    computer_cards.append(player_cards_temp)
    print("Computer card 2 = " + str(player_cards_temp))
    for z in range(int(player_count)):
        blackjack_new_card(player_cards_temp)
        player_cards[z] = str(player_cards_temp) + ", "
        blackjack_new_card(player_cards_temp)
        player_cards[z] += '%s,' % str(player_cards_temp)
        print(player_name[z] + "'s current cards = " + player_cards[z])

    for z in range(int(player_count)):
        draw_more = True
        while draw_more:
            plus_one = input(player_name[z] + "do you want to draw another card? (if no press: n then enter )")
            if plus_one != "n":
                blackjack_new_card(player_cards_temp)
                player_cards[z] += '%s,' % player_cards_temp
                print(player_name[z] + "'s current cards = " + player_cards[z])
            else:
                print("OK")
                draw_more = False

    print("Computers cards = " + str(computer_cards))
    for z in range(int(player_count)):
        print(player_name[z] + "'s cards = " + player_cards[z])


def blackjack_new_card(player_cards_temp):

    suit = random.randint(0, 4)
    number = random.randint(0, 13)
    player_card = [str(suit) + str(number)]
    if used_cards != player_card:
        used_cards.append(str(player_card))
        player_cards_temp = suits[suit]
        player_cards_temp += '%s' % str(deck[number])
    else:
        blackjack_new_card()


def blackjack_new_players(used, player, player_name):
    used = []
    player = 0
    player_name = []
    blackjack_names()


def blackjack_same_players():
    blackjack_main()


def launcher():
    print("Hello and welcome, GAMBLING IS ILEGAL!!!!! \nBut have fun ")
    blackjack_names()


launcher()
#blackjack_new_card(player_cards_temp)

