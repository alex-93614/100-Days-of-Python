import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Todo calculate scrore
def calculate_score(cards):
    score = sum(cards)
    ace_count = cards.count(11)

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score

#ToDo　Start game

#遊ぶか確認
play = input("Do you want to play a game of Blackjack? Type'y' or 'n': ")

# if play yes
if play == 'y':
    #art表示
    print(art.logo)

while play == 'y':
    #ToDo draw cards　初期カード配布

    #1.player draw2 card
    player_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    #2.print player score
    print(f"Your cards: {player_cards},current score: {calculate_score(player_cards)}")

    #3Computer draw 2card
    computer_cards = []
    computer_cards.append(random.choice(cards))

    #print computer card and score
    print (f"Computer's 1st card: {computer_cards}")

    #ToDo player turn
    #4.another card Type yes or no
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    #5.yes
    while another_card == 'y':
        #5-1.player draw1 card, computer draw1 card
        player_cards.append(random.choice(cards))

        #5-2.print player score,computer score(only1card)
        print(f"Your cards: {player_cards},current score: {calculate_score(player_cards)}")
        print (f"Computer's 1st card: {computer_cards}")

        if calculate_score(player_cards) > 21:

            print (f"Your final hand: {player_cards},final score: {calculate_score(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
            print("You went over.You lose!")
            break

        # 5-3. another card?
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    #ToDo if another_card == no Computer turn
    if calculate_score(player_cards) <= 21:
        while calculate_score(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

        print (f"Your final hand: {player_cards},final score: {calculate_score(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

        #ToDo Caluculate scores
        if calculate_score(computer_cards) > 21:
            print("You lose!")

        elif calculate_score(player_cards) == calculate_score(computer_cards):
            print ("draw!")

        elif calculate_score(player_cards) < calculate_score(computer_cards):
            print ("You lose!")

        else:
            print ("You win!")
#    else:

    #ToDo Continue?
    play = input("Do you want to play a game of Blackjack? Type'y' or 'n': ")
#if play no
#else:
    #finish