import random
import pygame
import itertools
from collections import namedtuple


class Card(object):
    """
    Card represented as a value and a suit, J=11 Q=12 K=13 A=14
    """
    def __init__(self,value,suit,image, text):
        assert type(value) ==int and type(suit)==str,""
        self.value = value
        self.suit = suit
        self.image = image
        self.text = str(self.value) + self.suit
        
    def __str__(self):
        """returns card represented as a string"""
        if self.value == 10:
            return "T"+self.suit
        if self.value == 11:
            return "J"+self.suit
        if self.value == 12:
            return "Q"+self.suit
        if self.value == 13:
            return "K"+self.suit
        if self.value == 14:
            return "A"+self.suit
        return str(self.value)+self.suit

class HoleCards(object):
    """
    Card represented as a value and a suit, J=11 Q=12 K=13 A=1
    """
    def __init__(self,card1,card2):
        assert type(card1) ==Card and type(card2)==Card,""
        self.card1 = card1
        self.card2 = card2
    def __str__(self):
        return str(self.card1)+", "+str(self.card2)

class Flop(object):
    """
    Card represented as a value and a suit, J=11 Q=12 K=13 A=1
    """
    def __init__(self,card1,card2,card3):
        assert type(card1) ==Card and type(card2)==Card and type(card3)==Card,""
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
    def __str__(self):
        return str(self.card1)+", "+str(self.card2)+", "+str(self.card3)

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

def nCr(n,r):
    return fact(n)/(fact(r)*(fact(n-r)))

def nPr(n,r):
    return fact(n)/fact(n-r)

def sum_rank(x):
    ranks = {str(i): i for i in range(2,10)}
    ranks.update({"A":14, "K":13, "Q":12, "J":11, "T":10})
    
    return int(ranks[x[0]]) + int(ranks[x[3]]) + int(ranks[x[6]]) + int(ranks[x[9]]) + int(ranks[x[12]])
        
print(sum_rank(('8c 8s 9d Th Jc')))                   


def fresh_deck():
    
    ranks = {str(i): i for i in range(2,10)}
    ranks.update({"A":14, "K":13, "Q":12, "J":11, "T":10})

    ranks_inverse = [str(k) for k in range(2,10)]
    ranks_inverse.append("T")
    ranks_inverse.append("J")
    ranks_inverse.append("Q")
    ranks_inverse.append("K")
    ranks_inverse.append("A")
    
    L=[]
    i=0
    k=1
    while k<14:
        k=k+1   
        L.append(Card(k,'h',pygame.image.load('Cards_png/'+ranks_inverse[k-2]+'h.png'),str(ranks_inverse[k-2])+'h'))      
        L.append(Card(k,'d',pygame.image.load('Cards_png/'+ranks_inverse[k-2]+'d.png'),str(ranks_inverse[k-2])+'d'))      
        L.append(Card(k,'c',pygame.image.load('Cards_png/'+ranks_inverse[k-2]+'c.png'),str(ranks_inverse[k-2])+'c'))       
        L.append(Card(k,'s',pygame.image.load('Cards_png/'+ranks_inverse[k-2]+'s.png'),str(ranks_inverse[k-2])+'s')) 
               
    return L


def shuffle_deck(N:list):  
    return sorted(N, key=lambda x: random.random())


def deal(deck,remaining_players):
    Hand=[]
    for index in range(remaining_players):
    
        x = deck[0]
        y = deck[1]
        deck.remove(x)
        deck.remove(y)
        Hand.append(HoleCards(x,y))                
    

        deck_remaining = deck

    return Hand, deck_remaining

def Deal_Flop(deck):
        
    x = deck[0]
    y = deck[1]
    z = deck[2]
    deck.remove(x)
    deck.remove(y)
    deck.remove(z)
    Out=Flop(x,y,z)                
    
    deck_remaining = deck

    return Out, deck_remaining


def eval(c):

    def combinations(iterable, r):
        # combinations('ABCD', 2) --> AB AC AD BC BD CD
        # combinations(range(4), 3) --> 012 013 023 123
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)
            
    def all_equal(lst):
        return len(set(lst)) == 1

    def is_consecutive(lst):
        return len(set(lst)) == len(lst) and max(lst) - min(lst) == len(lst) - 1

    def is_lowstraight(lst):
        return sorted(list(lst)) == [2,3,4,5,14]  

    class Card(namedtuple('Card', 'numeric_rank rank suit')):
        def __str__(self):
            return self.rank #+ self.suit
        def rank(self):
            return self.numeric_rank

    def parse_card(card):
        """
        Interpret the card as a namedtuple with a rank and suit.  The rank is
        represented numerically, with 'A' as 14, 'K' as 13, 'Q' as 12, 'J' as
        10.

        >>> parse_card('AS')
        Card(numeric_rank=14, rank='A', suit='♤')
        >>> parse_card('3S')
        Card(numeric_rank=3, rank='3', suit='♤')
        >>> parse_card('JC')
        Card(numeric_rank=11, rank='J', suit='♧')
        """
        FACE_VALUES = {'A': 14,'T':10, 'J': 11, 'Q': 12, 'K': 13}
        PRETTY_SUITS = {'c': '\u2667', 'd': '\u2662', 'h': '\u2661', 's': '\u2664'}
        rank, suit = card[:-1], card[-1:]
        numeric_rank=int(FACE_VALUES.get(rank, rank))
        if not 2 <= numeric_rank <= 14:
            raise ValueError('Invalid card: ' + card)
        return Card(
            numeric_rank=int(FACE_VALUES.get(rank, rank)),
            rank=rank,
            suit=suit
        )

    def parse_cards(cards):
        return [parse_card(card) for card in cards]

    def show_cards(cards):
        return ' '.join(str(card) for card in sorted(cards))

    def numeric_rank(cards):
        total = 0
        for card in cards:
            total += card.rank()
        return total

    def evaluate_hand(cards,cards_2):
        ranks = [card.numeric_rank for card in cards]
        six = 6 in [card2.numeric_rank for card2 in cards_2]
        suits = [card.suit for card in cards]
        if six == False:
            if is_lowstraight(ranks):
                return 'Straight'
            
        if is_consecutive(ranks):
            return (
                'Straight' if not all_equal(suits) else
                'Straight flush' if max(ranks) < 14 else
                'Royal flush'
            )
        if all_equal(suits):
            return 'Flush'
        return {
            4 + 4 + 4 + 4 + 1: 'Four of a kind',
            3 + 3 + 3 + 2 + 2: 'Full house',
            3 + 3 + 3 + 1 + 1: 'Three of a kind',
            2 + 2 + 2 + 2 + 1: 'Two pair',
            2 + 2 + 1 + 1 + 1: 'One pair',
            1 + 1 + 1 + 1 + 1: 'High card',
        }[sum(ranks.count(r) for r in ranks)]


    def best_hand(hand,cards_2):
        def hand_score(cards):
            type_score = [
                'High card',
                'One pair',
                'Two pair',
                'Three of a kind',
                'Straight',
                'Flush',
                'Full house',
                'Four of a kind',
                'Straight flush',
                'Royal flush',
            ].index(evaluate_hand(cards,cards_2))
            return (type_score, sum(card.numeric_rank for card in cards))
        
        if len(set(hand)) != len(hand):
            raise ValueError('Duplicate card in hand', hand)
        return max(itertools.combinations(cards, 5), key=hand_score)





    cards = parse_cards(c)
    cards_2 = parse_cards(c)
    best = best_hand(cards, cards_2)
   
    
    b = numeric_rank(best)
    
    a = evaluate_hand(best, cards_2)
    
    return a, b


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

