import random

deck = ["null"
        "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK",
        "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
        "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
        "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK"]
numbers = None
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
    computer_cards = []

    blackjack_new_card(numbers)
    computer_cards = [deck[numbers]]
    blackjack_new_card(numbers)
    computer_cards += [deck[numbers]]
    print("Computer card 2 = " + str(computer_cards[1]))
    for z in range(int(player_count)):
        blackjack_new_card(numbers)
        player_cards.append(str(deck[numbers]) + ", ")
        blackjack_new_card(numbers)
        player_cards[z] += '%s, ' % str(deck[numbers])
        print(player_name[z] + "'s current cards = " + player_cards[z])

    for z in range(int(player_count)):
        draw_more = True
        while draw_more:
            plus_one = input(player_name[z] + " do you want to draw another card? (if no press: n then enter )")
            if plus_one != "n":
                blackjack_new_card(numbers)
                player_cards[z] += '%s, ' % str(deck[numbers])
                print(player_name[z] + "'s current cards = " + player_cards[z])
            else:
                print("OK")
                draw_more = False

    print("Computers cards = " + str(computer_cards))
    for z in range(int(player_count)):
        print(player_name[z] + "'s cards = " + player_cards[z])


def blackjack_new_card(numbers):
    numbers = random.randint(0, 52)
    print(str(numbers) + ", " + str(deck[numbers]))
    player_card = [str(numbers)]
    if used_cards != player_card:
        used_cards.append(str(player_card))
    else:
        blackjack_new_card(numbers)


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
