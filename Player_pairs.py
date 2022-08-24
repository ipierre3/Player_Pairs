import random
from collections import Counter

"""
Main Stories
 
(5 points): As a developer, I want to make at least five commits on GitHub with descriptive  messages.

(10 points): As a developer, I want every function to be a pure function that does not modify or  access global variables. 
(Receives data through parameters and returns data through the  “return” keyword).

(5 points): As a pair player, I want a fifty-two (52) deck of cards to be created and stored in a List  (number/type only, no suits). 
        
        Four of each: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,  Jack, Queen, King
        
         HINT: Create a list called “deck”. This list should contain simple string values. For example, the list would contain four 
        (4) “7” string values to represent the four sevens (7) present in the deck.
            
            deck = [“Ace”, “Ace”, “Ace”, “Ace”, “2”, “2”, “2”, “2”, “3” ..... ]

                How could you add them using a loop rather than having to type out every value?
 
(2.5 points): As a pair player, I want to ensure that only four (4) of each number/type exist within the shuffled deck.
 
(5 points): As a pair player, I want to be able to shuffle the deck of cards so that they are in random order.
 
(5 points): As a pair player, I want five (5) cards dealt to four (4) players. 
 
(5 points): As a pair player, I want to determine the number of pairs within each player’s hand and display the player number, 
their hand, and the number of pairs to the terminal. 

(5 points): As a pair player, I want to determine the game’s winner or tied players and display them to the terminal.

"""


def greet():
    print('Welcome to Player Pairs!')
    print('In this game each player will receive 5 cards.')
    print('Once each hand has been dealt, we will compare to see who has the most pairs!')

greet()

def run_player_pairs():
    deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
    'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
    'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 
    'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Initial shuffling of the deck

    random.shuffle(deck)

# Key function elements to ensure variable 'deck' passes through each 'player' follow-up function

    player_1(deck)
    player_2(deck)
    player_3(deck)
    player_4(deck)

# Function for Player 1

def player_1(deck):
    player_hand = []
    print('Player 1')

    for draw in range(5):
        player_hand.append(deck[draw])

    print('Hand: ' + str(player_hand))

# Key function element that allows 'amount of pairs' function to pass through each player function

    amount_of_pairs(player_hand)

def player_2(deck):
    random.shuffle(deck)
    player_hand = []
    print('Player 2')

    for draw in range(5):
        player_hand.append(deck[draw])

    print('Hand: ' + str(player_hand))

    amount_of_pairs(player_hand)


def player_3(deck):
    random.shuffle(deck)
    player_hand = []
    print('Player 3')

    for draw in range(5):
        player_hand.append(deck[draw])

    print('Hand: ' + str(player_hand))

    amount_of_pairs(player_hand)


def player_4(deck):
    random.shuffle(deck)
    player_hand = []
    print('Player 4')

    for draw in range(5):
        player_hand.append(deck[draw])

    print('Hand: ' + str(player_hand))

    amount_of_pairs(player_hand)

# Checking for pairs 

def amount_of_pairs(player_hand):
    while True:
        cards = player_hand

        counted_cards = Counter(cards)
        find_pairs, count = zip(*counted_cards.most_common(2))

        located_pairs = {
            (1, 1): "Number of Pairs: 0",
            (2, 1): "Number of Pairs: 1",
            (4, 1): "Number of Pairs: 2",
        }
        msg = located_pairs[count]
        print(msg)
        break

# def who_won():

run_player_pairs()