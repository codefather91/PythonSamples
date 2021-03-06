import tkinter as tk
import tkinter.font as font
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import random

# Set DPI awareness for Win10 systems
try:
   from ctypes import windll 
   windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Set up a card deck as a dictionary with all the card faces and their corresponding values
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

# Initialise the global variables
player_deck=[]
player_score=0
dealer_deck=[]
dealer_score=0
bust_flag=0
player_name=''
chance=0
play_card=''
# Define the gameplay logic

def play_again():
    # Function to re-run the game if user wants to play again else close the app
    global chance
    global play_card
    if chance > 0 and chance < 2:
        double_down()
    else:
        hitButton["state"] = 'disabled'
        standButton["state"] = 'disabled'
        playagain = mb.askquestion("Play Again?", "Would you like to play again?")
        if playagain == 'yes':
            hitButton["state"] = 'active'
            standButton["state"] = 'active'
            initialize_game()
        else:
            root.destroy()

def initialize_game():
    # Set up the game for new play. Deal the first two cards to the player and one card to the dealer.
    global player_deck
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag
    global card_deck
    global chance
    global play_card
    player_deck=[]
    dealer_deck=[]
    player_score=0
    dealer_score=0
    bust_flag=0
    chance=0
    dealer_card = random.choice(list(card_deck))
    dealer_deck.append(dealer_card)
    if dealer_card == 'A':
        dealer_val = 11
    else:
        dealer_val = card_deck[dealer_card]
    dealer_score+=dealer_val
    play_card1 = random.choice(list(card_deck))
    play_card2 = random.choice(list(card_deck))
    if play_card1 == play_card2:
        split_ask = mb.askquestion("Split", "You drew two consecutive "+play_card1+"\nWould you like to split?")
        if split_ask == 'yes':
            play_card = play_card1
            double_down()
        else:
            player_deck.append(play_card1)
            if play_card1 == 'A':
                if player_score + 11 <= 21:
                    play_cardval1 = 11
                else:
                    play_cardval1 = 1
            else:
                play_cardval1 = card_deck[play_card1]
            player_score+=play_cardval1
            player_deck.append(play_card2)
            if play_card2 == 'A':
                if player_score + 11 <= 21:
                    play_cardval2 = 11
                else:
                    play_cardval2 = 1
            else:
                play_cardval2 = card_deck[play_card2]
                player_score += play_cardval2
    else:
        player_deck.append(play_card1)
        if play_card1 == 'A':
            if player_score + 11 <= 21:
                play_cardval1 = 11
            else:
                play_cardval1 = 1
        else:
            play_cardval1 = card_deck[play_card1]
        player_score+=play_cardval1
        player_deck.append(play_card2)
        if play_card2 == 'A':
            if player_score + 11 <= 21:
                play_cardval2 = 11
            else:
                play_cardval2 = 1
        else:
            play_cardval2 = card_deck[play_card2]
        player_score += play_cardval2
#    print("DEALER DECK :", " ".join(dealer_deck))
#    print("DEALER SCORE :", dealer_score)
    dealercards.config(text=" ".join(dealer_deck))
    score_show()
    score_check()
#    player_turn()

def double_down():
    global player_deck
    global play_card
    global player_score
    global chance
    global card_deck
    player_deck=[]
    player_score=0
    mb.showinfo(title="Double Down", message="Deck #"+str(chance+1))
    player_deck.append(play_card)
    player_score+=card_deck[play_card]
    chance+=1
    score_show()
    hit()

def dealer_move():
    # Once the user stands his deck, the dealer hits until he hits a 17
    global card_deck
    global dealer_deck
    global dealer_score
    while dealer_score < 17:
        card_name = random.choice(list(card_deck))
        dealer_deck.append(card_name)
        dealercards.config(text=" ".join(dealer_deck))
        card_val = card_deck[card_name]
        if card_name == 'A':
            if player_score + 11 <= 21:
                card_val = 11
            else:
                card_val = 1
        if 'A' in dealer_deck and len(dealer_deck) > 2:
            if dealer_score > 21:
                dealer_score = dealer_score - 10
        dealer_score += card_val
#    print("DEALER DECK :", " ".join(dealer_deck))
#    print("DEALER SCORE :", dealer_score)
    result()

def result():
    # Result calculation on the basis of the hands of the dealer and the player
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag
    global player_name
    if dealer_score > 21:
#        print("DEALER BUST!")
        mb.showinfo(title="Result", message="DEALER BUST!")
    elif dealer_score < player_score:
#        print("PLAYER WINS!")
        mb.showinfo(title="Result", message=player_name+" WINS!")
    elif dealer_score > player_score:
#        print("DEALER WINS!")
        mb.showinfo(title="Result", message="DEALER WINS!")
    else:
#        print("PUSH")
        mb.showinfo(title="Result", message="PUSH\nScores Equal")
    play_again()

def blackjack():
    # Prompt message if user gets a blackjack
    score_show()
    mb.showinfo(title="Result", message="BLACKJACK!")
#    print("BLACKJACK!!")
    play_again()

def player_bust():
    # Prompt message if user total goes over 21, i.e., player bust
    global bust_flag
    global player_name
    bust_flag = 1
    mb.showinfo(title="Result", message=player_name+" BUST!")
#    print("PLAYER BUST!")
    play_again()

'''
def player_turn():
    global player_score
    dist_to_21 = 21 - player_score
#    print(dist_to_21," to go")
#    move = input("Hit (h) or Stand (s) ?")
    if move == 'h' or move =='H':
        hit()
    else:
        stand()
'''
        
def stand():
    # Player no more wishes new cards
    global player_score
    global player_deck
#    print("FINAL DECK :", " ".join(player_deck))
#    print("SCORE :", player_score)
    dealer_move()

def score_check():
    # Check the current total of the player and take actions accordingly
    global player_score
    if player_score < 21:
        return
    elif player_score == 21:
        blackjack()
    elif player_score > 21:
        player_bust()

def hit():
    # Allow the user to add a new card to one's deck
    global card_deck
    global player_deck
    global player_score
    card_name = random.choice(list(card_deck))
    player_deck.append(card_name)
    card_val = card_deck[card_name]
    if card_name == 'A':
        if player_score + 11 <= 21:
            card_val = 11
        else:
            card_val = 1
    if 'A' in player_deck and len(player_deck) > 2:
        if player_score > 21:
            player_score = player_score - 10
    player_score += card_val
    score_show()
    score_check()

def score_show():
    # Display the player's current score in the status bar
    global player_deck
    global player_score
    playercards.config(text=" ".join(player_deck))
#    print("PLAYER DECK :", " ".join(player_deck))
#    print("SCORE :", player_score)
    status.config(text="Player Score: "+str(player_score))

# Game GUI begins here

def newgame():
    # Set up the new game for the user
    global player_name
    player_name = sd.askstring("Player Name", "Input the player name")
    player_name = player_name.upper()
    playerLabel.config(text=player_name)
    hitButton["state"] = 'active'
    standButton["state"] = 'active'
    initialize_game()

def aboutgame():
    # Info about the app
    mb.showinfo(title="About", message="BlackJack!!\nBuilt by Kanav Gulati\nv2 GUI version")

# Set up the GUI for the app
    
root= tk.Tk()
root.geometry('640x480')
root.title('BlackJack!! v2')
root.resizable(False, False)

# Add the menu bar to the app
menubar = tk.Menu(root)
gameMenu = tk.Menu(menubar, tearoff=0)
optionsMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=gameMenu)
menubar.add_cascade(label="Options", menu=optionsMenu)

gameMenu.add_command(label="New Game", command=newgame)
gameMenu.add_command(label="Quit", command=root.destroy)

optionsMenu.add_command(label="About", command=aboutgame)

root.config(menu=menubar)

# Create the main placeholder for the widgets
mainFrame = tk.Frame(root, bg='light gray')
mainFrame.pack(fill="both", expand=True)

# Create a status bar
status = tk.Label(root, text=" ", relief='sunken', anchor=tk.W, bd=1)
status.pack(side="bottom", fill="x")

# Add a placeholder for the player and dealer card deck info widgets
playArea = tk.Frame(mainFrame)
playArea.pack(padx=10, pady=(10,0), fill="both", expand=True)

# Create the Dealer deck related widgets within the playArea frame
dealerFrame = tk.Frame(playArea, bg="green")
dealerFrame.pack(fill="both", expand=True)

dealerLabel = tk.Label(dealerFrame, text="DEALER", fg="black", bg="green", font=font.Font(family='Calibri', size=20, weight='bold'))
dealerLabel.pack(expand=True)
dealercards = tk.Label(dealerFrame, text="NO CARDS DEALT", fg="white", bg="green", font=font.Font(family='Calibri', size=32))
dealercards.pack(fill="both", expand=True)

# Create the Player deck related widgets within the playArea frame
playerFrame = tk.Frame(playArea, bg="green")
playerFrame.pack(fill="both", expand=True)

playerLabel = tk.Label(playerFrame, text="PLAYER", fg="black", bg="green", font=font.Font(family='Calibri', size=20, weight='bold'))
playerLabel.pack(expand=True)
playercards = tk.Label(playerFrame, text="NO CARDS DEALT", fg="white", bg="green", font=font.Font(family='Calibri', size=32))
playercards.pack(fill="both", expand=True)

# Add the frame for the control buttons into the master frame
controlBox = tk.Frame(mainFrame, bg="black")
controlBox.pack(padx=10, pady=(0,10), ipadx=10, ipady=10, fill="both")

hitButton = tk.Button(controlBox, text="HIT", width=20, font=font.Font(family='Calibri', size=16, weight='bold'), command=hit)
hitButton.pack(side="left", padx=10, pady=10, expand=True)

standButton = tk.Button(controlBox, text="STAND", width=20, font=font.Font(family='Calibri', size=16, weight='bold'), command=stand)
standButton.pack(side="right", padx=10, pady=10, expand=True)

# Disable the buttons for the start of the application
hitButton["state"] = 'disabled'
standButton["state"] = 'disabled'

# Start the app
root.mainloop()
