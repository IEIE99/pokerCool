from collections import namedtuple
import itertools

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
            return self.rank + self.suit

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
    'ts, sr = hand_score(cards_2)'
    
    b = show_cards(best)
    
    a = evaluate_hand(best, cards_2)
    
    return a, b




