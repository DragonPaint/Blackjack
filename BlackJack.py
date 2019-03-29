import random

deck = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK",
        "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
        "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
        "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK"]
pip = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K"]
pip_ten = ["1", "J", "Q", "K"]
used = []
player = 0
player_cards = []


def blackjack_names():
    player_name = ["Computer"]
    player_count = input("How many players?, not including the dealer/computer. ")
    for z in range(int(player_count)):
        player_name.append(input("What is player " + str(z + 1) + "'s name? "))
        print("Player " + str(z + 1) + "'s name is: " + player_name[z])
    blackjack_main(player_count, player_name)


def blackjack_main(player_count, player_name):
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

    blackjack_computer(used_cards)
    blackjack_computer(used_cards)

    for z in range(int(player_count)):
        print(player_name[z + 1] + "'s cards = " + player_cards[+1])
    blackjack_exit(player_count, player_name)


def blackjack_computer(used_cards):
    z = 0
    aces_computer = 0
    computer_score = 0
    for b in player_cards[0]:
        if b in pip:
            if b == "A":
                aces_computer += 1
            elif b in pip_ten:
                computer_score += 10
            else:
                computer_score += int(b)
    if aces_computer != 0:
        computer_score_eleven = computer_score + aces_computer * 11
        computer_score_one = computer_score + aces_computer * 1
        if computer_score_eleven <= 21:
            if computer_score_eleven < 17:
                blackjack_new_card(z, used_cards)
        elif computer_score_one <= 21:
            if computer_score_one < 17:
                blackjack_new_card(z, used_cards)
        else:
            print("Computer went BUST!!! \nYOU WIN!!!")
    else:
        if computer_score < 17:
            blackjack_new_card(z, used_cards)
        elif computer_score > 21:
            print("Computer went BUST!!! \nYOU WIN!!!")
    print("Computers Cards = " + player_cards[0])


def blackjack_exit(player_count, player_name):
    print("Do you want to restart with the same names, restart or exit?")
    restart = input("Names = restart with names, Restart = restart without names, Exit = exit programs. ")
    if restart.lower() == "names":
        blackjack_same_players(player_count, player_name)
    elif restart.lower() == "restart":
        blackjack_names()
    elif restart.lower() == "exit":
        exit()
    else:
        print("Error you shall not pass? I shall give you the options again.")
        blackjack_exit()


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
        player_cards[int(z)] += '%s, ' % str(deck[numbers])
    else:
        blackjack_new_card(z, used_cards)


def blackjack_new_players(used, player, player_name):
    used = []
    player = 0
    player_name = []
    blackjack_names()


def blackjack_same_players(player_count, player_name):
    blackjack_main(player_count, player_name)


def launcher():
    print("Hello and welcome, GAMBLING IS ILEGAL!!!!! \nBut have fun ")
    blackjack_names()


launcher()
