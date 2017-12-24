import random, itertools

# TODO could probably handle cards more gracefully by making them objects

class BlackjackGame:

    class Hand:
        def __init__(self, name):
            self.name = name
            self.hand = []
            self.hand_value = 0
            self.is_holding = False
            self.has_busted = False
            self.natural = False

    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    # Initial game setup
    def __init__(self):
        self.game_over = False

        # Establish player and dealer hands
        self.dealer = self.Hand('Dealer')
        self.player = self.Hand('Player')

        # Create deck by combining all ranks and suits
        self.deck = list(' '.join(card) for card in itertools.product(self.RANKS, self.SUITS))
        # self.deck = ['Ace Diamonds', '2 Spades', 'Ace Hearts', 'King Clubs']

        # Shuffle deck
        random.shuffle(self.deck)
        print('Cards shuffled')

        # Deal initial cards
        self.deal_cards(2, self.dealer)
        print('Dealer cards dealt')
        self.deal_cards(2, self.player)
        print('Player cards dealt')

    # Deals specified number of cards to the specified hand
    def deal_cards(self, number, player):
        
        # I don't use the card variable here, it's just to enable the loop to run
        for card in range(number):
            player.hand.append(self.deck.pop())

        self.update_hand_value(player)

    def check_natural_blackjack(self, player):
        if ( player.hand_value == 21 ):
            player.natural == True
            self.game_over == True

    def show_cards(self, player):
        print()
        print( player.name + ' hand: \n' + ', '.join(player.hand))
        print( player.name + ' hand value: ' + str(self.get_hand_value(player)))

    def update_hand_value(self, player):
        player.hand_value = self.get_hand_value(player)
        if (player.hand_value > 21):
            player.has_busted = True

    def get_hand_value(self, player):
        
        total = 0
        ace_count = 0
        
        for card in player.hand:
            # If card is a number, convert to int and add to total
            if card[0] in '0123456789':
                total+=int(card.split()[0])

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

    def hit(self, player):
        print( player.name + ' hit' )
        self.deal_cards(1, player)

    def hold(self, player):
        print( player.name + ' hold' )
        self.player.is_holding = True

    def dealer_ai_hit_logic(self):
        if (self.dealer.hand_value < 17):
            return True
        else:
            self.game_over = True
            return False

    def print_player_interface(self):
        print()
        print( '----------------------------' )
        print( '\nWhat would you like to do?' )
        print( '1. Hit' )
        print( '2. Stay')

    def check_game_results(self):
        self.show_cards(self.player)
        self.show_cards(self.dealer)
        print( '\n###############' )
        if ( self.player.hand_value == self.dealer.hand_value ):
            print( 'Tie game!' )
        elif ( self.dealer.has_busted or self.player.hand_value > self.dealer.hand_value and not self.player.has_busted ):
            print( 'Player wins!' )
        else:
            print( 'Dealer wins.' )
        print( '###############' )

    def start_game(self):
        self.show_cards(self.player)
        self.show_cards(self.dealer)
        self.check_natural_blackjack(self.dealer)
        self.check_natural_blackjack(self.player)
        choice = ''
        option_list = ['1', '2']
        while ( not self.player.has_busted and not self.player.is_holding and choice not in option_list ):
            self.print_player_interface()
            choice = input()
            if ( choice == '1' ):
                self.hit(self.player)
                print('----------------------------')
                self.show_cards(self.player)
                self.show_cards(self.dealer)
            elif ( choice == '2' ):
                self.hold(self.player)
            else:
                print( 'This should not display. Something broke.' )
            choice = ''

        if ( self.player.has_busted ):
            print ( '\n############################' )
            print ( 'You busted!\nHand value: ' + str(self.player.hand_value) )
            print ( '############################' )
            self.game_over = True

        while ( self.dealer_ai_hit_logic() and not self.game_over ):
            self.hit(self.dealer)
            self.show_cards(self.dealer)

        if ( self.dealer.has_busted ):
            print ( '\n############################' )
            print ( 'Dealer busted!\nHand value: ' + str(self.dealer.hand_value) )
            print ( '############################' )
            self.game_over = True

        self.check_game_results()     

while True:
    bj = BlackjackGame()
    bj.start_game()
    choice = ''
    choice_list = ['1', '2']
    while ( choice not in choice_list ):
        print( '\nPlay again?' )
        print( '1. Yes' )
        print( '2. No' )
        choice = input()
    if ( choice == '2' ):
        break

##        self.deck = []
##        for suit in self.SUITS:
##            for rank in self.RANKS:
##                self.deck.append(rank + ' ' + suit)
