import random, itertools

class BlackjackGame:

    class Hand:
        def __init__(self):
            self.hand = []
            self.hand_value = 0
            self.is_holding = False

    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    # Initial game setup
    def __init__(self):

        # Establish player and dealer hands
        self.dealer = self.Hand()
        self.player = self.Hand()

        # Create deck by combining all ranks and suits
        self.deck = list(' '.join(card) for card in itertools.product(self.RANKS, self.SUITS))

        # Shuffle deck
        random.shuffle(self.deck)

        # Deal initial cards
        self.deal_cards(2, self.dealer.hand)
        self.deal_cards(2, self.player.hand)

    # Deals specified number of cards to the specified hand
    def deal_cards(self, number, hand):
        
        # I don't use the card variable here, it's just to enable the loop to run
        for card in range(number):
            hand.append(self.deck.pop())

    def show_face_up_cards(self):
        pass

    def update_hand_value(self, player):
        player.hand_value = self.get_hand_value(player)

    def get_hand_value(self, player):
        
        total = 0
        ace_count = 0
        
        for card in player.hand:
            # If card is a number, convert to int and add to total
            if card[0] in '23456789':
                total+=int(card[0])

            # If card is Jack/Queen/King, add 10
            elif card[0] in 'jqkJQK':
                total+=10

            # If card is Ace, make note to handle after other cards
            elif card[0] in 'aA':
                ace_count+=1

        # If there's at least a difference of 11 + number of other aces in hand
        # between the players current hand value and 21, ace is worth 11
        # Otherwise, ace is worth 1
        for ace in range(ace_count):
            if total <= 21 - ( 11 + ace_count-1 ):
                total += 11
            else:
                total+=1
            ace_count-=1

        return total

            

    def hit(self):
        pass

    def stay(self):
        pass

game = BlackjackGame()

##        self.deck = []
##        for suit in self.SUITS:
##            for rank in self.RANKS:
##                self.deck.append(rank + ' ' + suit)
