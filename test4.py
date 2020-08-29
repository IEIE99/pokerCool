import sys
import pokerfunctions as pf
from table import table
from players import Player

class Hand(object):
    def __init__(self):

        self.players = table.players.copy()
        hands, flop, turn, river = shuffle()

        for i in range(len(self.players)):
            self.players[i].hand = hands[i]

        self.folded = []
        self.remaining = table.players.copy()
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
        self.pots = []
       
        self.winners = []
        self.players_out = []
        self.max_type_score = 0
        self.max_sum_rank = 0
        self.finished = False
        self.showdown = False

    def increase_pot(self, amount, player):
        if amount > player.chips:
            player.seat.update_action('ALL IN', 20, yellow)
        self.pot += min(amount, player.chips)
        player.chips -= min(amount, player.chips)
        player.bet += min(amount, player.chips)
        self.largest_bet = player.bet      
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

        current.pots.append(self)

    def __str__(self):
        return ' '.join((str(self.chips_committed), str(self.contenders), 'Max type_score:', str(self.max_type_score)))

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

    for hand in hands:
        print('Hole cards:', hand)

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

current = Hand()

for p in table.players:
    p.cards = str(p.hand.card1), str(p.hand.card2), str(current.flop.card1), str(current.flop.card2), str(current.flop.card3)
    p.cards = p.cards + (str(current.turn),)
    p.cards = p.cards + (str(current.river),)
    print(p.name, p.cards)
    p.eval, p.sum_rank = pf.eval(p.cards)
    p.type_score = p.hand_value(p.eval)
        

current.pot = 10300
contenders1 = current.players.copy()

p1 = current.players[0]
p2 = current.players[1]
p3 = current.players[2]
p4 = current.players[3]

contenders2 = contenders1.copy()
contenders2.remove(p1)
contenders2.remove(p4)

contenders3 = contenders2.copy()
contenders3.remove(p2)
contenders4 = contenders3.copy()
contenders4.remove(p3)


pot2 = Pot(800,contenders2)
pot4 = Pot(2000,contenders4)
pot1 = Pot(500,contenders1)
pot3 = Pot(1000,contenders3)



print(pot1<pot3)
current.pots = sorted(current.pots)


paid = 0
for pot in current.pots:
    pot.chips_committed -= paid
    paid += pot.chips_committed
    pot()
    print('Pot total:', pot.pot_total, pot.contenders)
    
    
    for winner in pot.winners:
        print(winner)
        winner.chips += pot.pot_total / len(pot.winners)
        current.pot -= pot.pot_total / len(pot.winners)
        winner.update_chips()

print('pot:', current.pot)






for p in table.players:
    print(p, 'Hand:', p.eval, 'score:', p.type_score, 'rank:', p.sum_rank, 'Chips:', p.chips)

print(sys.prefix)
print(sys.exec_prefix)
print(sys.path)
