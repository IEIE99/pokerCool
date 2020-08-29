import pokerfunctions as pf
from table import table
from colours import all_in


class Hand(object):
    
    def __init__(self):

        self.players = table.players.copy()
        hands, flop, turn, river = shuffle()
        self.starting_chips = {}

        for i in range(len(self.players)):
            self.players[i].hand = hands[i]
            self.starting_chips.update({self.players[i].name: self.players[i].chips})
            print(self.players[i].name, ':--- Cards:', self.players[i].hand, 'Chips:', self.players[i].chips)

        self.folded = []
        self.remaining = table.players.copy()
        self.all_in = []
        self.out = []
        
        self.folded_count = 0
        
        self.pre_bets = True
        self.flop_bets = False
        self.turn_bets = False
        self.river_bets = False    
        
        
        self.hands = hands
        self.flop = flop
        self.turn = turn
        self.river = river
        
        self.BB = 50
        self.SB = 25
        self.big_blind = True
        self.small_blind = True

        self.pot = self.BB + self.SB
        self.largest_bet = self.BB
        self.max_bet = 0
        self.pots = []
        
        self.winners = []
        self.players_out = []
        self.max_type_score = 0
        self.max_sum_rank = 0
        self.finished = False
        self.showdown = False

    def increase_pot(self, amount, player):       
##        print('INCREASE AMOUNT', amount)
        if amount >= player.chips:
            player.seat.update_action('ALL IN', 20, color=all_in)
            print(self.starting_chips[player.name])
            player.seat.update_bet(self.starting_chips[player.name])
            self.pot += min(amount, player.chips)            
            player.bet += min(amount, player.chips)
            player.chips -= min(amount, player.chips)
            self.largest_bet = max(self.largest_bet, player.bet)
            player.update_chips()
        else:
##            print('p.bet:', player.bet)
##            print('p.chips:', player.chips)
##            print('min(amt, p.bet):', min(amount, player.chips))
            self.pot += min(amount, player.chips)
            player.bet += min(amount, player.chips)
            player.chips -= min(amount, player.chips)            
            self.largest_bet = max(self.largest_bet, player.bet)
##            print('NEW CHIPS:', player.chips, 'NEW BET:', player.bet)
            player.update_bet()
            player.update_chips()

class Pot():
    
    def __init__(self, chips_committed, contenders):
        
        self.chips_committed = chips_committed
        self.contenders = contenders
        self.pot_total = chips_committed * len(contenders)
        self.max_type_score = 0        
        self.max_sum_rank = 0
        self.players_with_max = []
        self.winners = []

##        current.pots.append(self)

    def __str__(self):
        return ' '.join(('Pot created:', str(self.chips_committed), str(self.contenders)))

    def __lt__(self, other):
        return self.chips_committed < other.chips_committed            

    def max_type(self):
        for p in self.contenders:
            self.max_type_score = max(self.max_type_score, p.type_score)       

    def max_sum(self):
        for p in self.contenders:
            if p.type_score == self.max_type_score:
                self.players_with_max.append(p)
        for p in self.players_with_max:
            self.max_sum_rank = max(self.max_sum_rank, p.sum_rank)
            
    def return_winners(self):
        for p in self.players_with_max:
            if p.sum_rank == self.max_sum_rank:
                self.winners.append(p)

    def chips_total(self):
        self.pot_total = self.chips_committed * len(self.contenders)

    def __call__(self):
        self.max_type()
        self.max_sum()
        self.return_winners()
        self.chips_total()

def shuffle():

    """ SHUFFLE DECK """

    fresh_deck =pf.fresh_deck()
    shuffled_deck = pf.shuffle_deck(fresh_deck)

    """ DEAL HANDS """

    hands, DECK = pf.deal(shuffled_deck, len(table.players))

    """Deal community cards"""

    flop, DECK = pf.Deal_Flop(DECK)
    turn = DECK[0]
    river = DECK[1]

    print("Flop:")
    print(flop)
    print("Turn:")
    print(turn)
    print("River:")
    print(river)

    return hands, flop, turn, river
