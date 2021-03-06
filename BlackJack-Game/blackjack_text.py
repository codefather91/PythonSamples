import random

card_deck = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "10" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "A" : 1
}

player_deck=[]
player_score=0
dealer_deck=[]
dealer_score=0
bust_flag=0

def play_again():
    play_choice = input("Wish to play again?")
    if play_choice == 'y' or play_choice == 'Y':
        initialize_game()
    else:
        exit()

def initialize_game():
    global player_deck
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag
    global card_deck
    player_deck=[]
    dealer_deck=[]
    player_score=0
    dealer_score=0
    bust_flag=0
    dealer_card = random.choice(list(card_deck))
    dealer_deck.append(dealer_card)
    dealer_val = card_deck[dealer_card]
    dealer_score+=dealer_val
    play_card1 = random.choice(list(card_deck))
    player_deck.append(play_card1)
    play_cardval1 = card_deck[play_card1]
    player_score+=play_cardval1
    play_card2 = random.choice(list(card_deck))
    player_deck.append(play_card2)
    play_cardval2 = card_deck[play_card2]
    player_score += play_cardval2
    print("DEALER DECK :", " ".join(dealer_deck))
    print("DEALER SCORE :", dealer_score)
    score_show()
    score_check()
    player_turn()

def dealer_move():
    global card_deck
    global dealer_deck
    global dealer_score
    while dealer_score <=17:
        card_name = random.choice(list(card_deck))
        dealer_deck.append(card_name)
        card_val = card_deck[card_name]
        if card_name == 'A':
            if player_score + 11 > 21:
                card_val = 1
            else:
                card_val = 11
        dealer_score += card_val
    print("DEALER DECK :", " ".join(dealer_deck))
    print("DEALER SCORE :", dealer_score)
    result()

def result():
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag
    if dealer_score > 21:
        print("DEALER BUST!")
    elif dealer_score < player_score:
        print("PLAYER WINS!")
    elif dealer_score > player_score:
        print("DEALER WINS!")
    else:
        print("PUSH")
    play_again()

def blackjack():
    score_show()
    print("BLACKJACK!!")
    play_again()

def player_bust():
    global bust_flag
    bust_flag = 1
    print("PLAYER BUST!")
    play_again()

def player_turn():
    global player_score
    dist_to_21 = 21 - player_score
    print(dist_to_21," to go")
    move = input("Hit (h) or Stand (s) ?")
    if move == 'h' or move =='H':
        hit()
    else:
        stand()

def stand():
    global player_score
    global player_deck
    print("FINAL DECK :", " ".join(player_deck))
    print("SCORE :", player_score)
    dealer_move()

def score_check():
    global player_score
    if player_score < 21:
        return 0
    elif player_score == 21:
        return 1
    elif player_score > 21:
        return -1

def hit():
    global card_deck
    global player_deck
    global player_score
    card_name = random.choice(list(card_deck))
    player_deck.append(card_name)
    card_val = card_deck[card_name]
    if card_name == 'A':
        if player_score + 11 > 21:
            card_val = 1
        else:
            card_val = 11
    player_score += card_val
    score_show()
    if score_check() == -1:
        player_bust()
    elif score_check() == 1:
        blackjack()
    else:
        player_turn()

def score_show():
    global player_deck
    global player_score
    print("PLAYER DECK :", " ".join(player_deck))
    print("SCORE :", player_score)

initialize_game()
