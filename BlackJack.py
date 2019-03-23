import random

deck = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK",
        "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
        "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
        "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK"]
used = []
player = 0
player_name = ["Computer"]
player_cards = []
used_cards = []
player_cards_temp = 0


def blackjack_names():
    player_count = input("How many players?, not including the dealer/computer. ")
    for z in range(int(player_count)):
        player_name.append(input("What is player " + str(z + 1) + "'s name? "))
        print("Player " + str(z + 1) + "'s name is: " + player_name[z])
    blackjack_main(player_count)


def blackjack_main(player_count):
    player_cards.clear()
    used_cards = []

    for z in range(len(player_name)):
        blackjack_first_new_card(used_cards)
        blackjack_new_card(z, used_cards)
        if player_name[z] == "Computer":
            computer_card = str(player_cards[0])
            print("Computer card 2 = " + computer_card[4:])
        else:
            print(player_name[z] + "'s current cards = " + player_cards[z])

    for z in range(len(player_count)):
        z += 1
        draw_more = True
        while draw_more:
            plus_one = input(player_name[z] + " do you want to draw another card? (if no press: n then enter )")
            if plus_one != "n":
                blackjack_new_card(z, used_cards)
                print(player_name[z] + "'s current cards = " + player_cards[z])
            else:
                print("OK")
                draw_more = False

    for z in range(len(player_count)):
        print(player_name[z] + "'s cards = " + player_cards[z])


def blackjack_first_new_card(used_cards):
    numbers = random.randint(0, 51)
    player_card = [str(numbers)]
    if used_cards != player_card:
        used_cards += player_card
        player_cards.append(str(deck[numbers]) + ", ")
    else:
        blackjack_new_card(used_cards)


def blackjack_new_card(z, used_cards):
    numbers = random.randint(0, 52)
    player_card = [str(numbers)]
    if used_cards != player_card:
        used_cards += player_card
        player_cards[z] += '%s, ' % str(deck[numbers])
    else:
        blackjack_new_card(z, used_cards)


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
