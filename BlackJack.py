import random

deck = ["null"
        "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK",
        "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
        "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
        "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK"]
numbers = 0
suits = ["S", "H", "D", "C"]
used = []
player = 0
player_name = []
player_cards = []
used_cards = [""]
computer_cards = []
player_cards_temp = 0


def blackjack_names():
    player_count = input("How many players?, not including the dealer/computer. ")
    for z in range(int(player_count)):
        player_name.append(input("What is player " + str(z + 1) + "'s name? "))
        print("Player " + str(z + 1) + "'s name is: " + player_name[z])
    blackjack_main(player_count)


def blackjack_main(player_count):
    player_cards.clear()
    used_cards = [""]
    computer_cards.clear()

    blackjack_new_card(player_cards_temp)
    computer_cards.append(player_cards_temp)
    blackjack_new_card(player_cards_temp)
    computer_cards.append(player_cards_temp)
    print("Computer card 2 = " + str(player_cards_temp))
    for z in range(int(player_count)):
        blackjack_new_card(player_cards_temp)
        player_cards.append(str(player_cards_temp) + ", ")
        blackjack_new_card(player_cards_temp)
        player_cards[z] += '%s,' % str(player_cards_temp)
        print(player_name[z] + "'s current cards = " + player_cards[z])

    for z in range(int(player_count)):
        draw_more = True
        while draw_more:
            plus_one = input(player_name[z] + " do you want to draw another card? (if no press: n then enter )")
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
    number = random.randint(0, 52)
    if number == 0:
        blackjack_new_card(player_cards_temp)

    player_card = [str(number)]
    if used_cards != player_card:
        used_cards.append(str(player_card))
        player_cards_temp = deck[number]
    else:
        blackjack_new_card(player_cards_temp)


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
# blackjack_new_card(player_cards_temp)
