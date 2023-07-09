import random

# Define the deck of cards
suits = ['♠', '♣', '♥', '♦']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for suit in suits for rank in ranks]

# Define the initial pot and player details
pot = 0
players = [{'name': 'Player 1', 'chips': 100, 'hand': [], 'folded': False},
           {'name': 'Player 2', 'chips': 100, 'hand': [], 'folded': False}]

# Function to deal cards
def deal_cards():
    random.shuffle(deck)
    for player in players:
        player['hand'] = [deck.pop(), deck.pop()]

# Function to display player cards
def display_player_info(current_player):
    for player in players:
        
        output = ""
        if player == current_player:
            output = f"{player['name']}: {player['hand'][0]} {player['hand'][1]} ({player['chips']})"
        else:
            output = f"{player['name']}: [XX] [XX] ({player['chips']})"        
        print(output)

# Function to display the community cards
def display_community_cards(community_cards):
    print("Community cards: ", end="")
    for card in community_cards:
        print(card, end=" ")
    print()

# Function to display the pot
def display_pot():
    print(f"Pot: {pot}")

# Function to place bets
def place_bets(player):
    while True: 

        action = input(f"{player['name']}, choose an action (check/bet/fold): ")
        if action == 'check':
            print(f"{player['name']} checks.")
            break
        elif action == 'bet':
            bet = int(input(f"{player['name']}, place your bet: "))
            if bet <= player['chips']:
                player['chips'] -= bet
                global pot
                pot += bet
                print(f"{player['name']} bets {bet}.")
                break
            else:
                print("Invalid bet. You don't have enough chips.")
        elif action == 'fold':
            player['folded'] = True
            print(f"{player['name']} folds.")
            break
        else:
            print("Invalid action. Please choose again.")

# Function to play the game
def play_game():
    while True:
        deal_cards()
        current_player = players[0]
        display_player_info(current_player)

        # Place initial bets
        for player in players:
            place_bets(player)

        # Flop - Deal 3 community cards
        display_player_info(current_player)
        display_pot()
        community_cards = [deck.pop(), deck.pop(), deck.pop()]
        display_community_cards(community_cards)

        # Place bets after flop
        # Place initial bets
        for player in players:
            if not player['folded']:
                place_bets(player)        

        # Turn - Deal 1 more community card
        display_player_info(current_player)
        display_pot()
        community_cards.append(deck.pop())
        display_community_cards(community_cards)

        # Place bets after turn
        for player in players:
            place_bets(player)

        # River - Deal the final community card
        display_player_info(current_player)
        display_pot()
        community_cards.append(deck.pop())
        display_community_cards(community_cards)

        # Place bets after river
        for player in players:
            place_bets(player)

        # Showdown
        display_player_info(current_player)
        display_pot()
        print("Showdown time!")

        # Calculate and display the winner(s) and distribute the pot
        # You'll need to implement this part based on the rules of Texas Hold'em

        # Check if players want to continue playing
        choice = input("Do you want to play again? (y/n): ")
        if choice.lower() != 'y':
            break

# Start the game
play_game()
