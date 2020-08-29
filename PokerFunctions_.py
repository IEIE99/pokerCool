import random

def Fact(x):
    if x ==0:
        return 1
    if x ==1:
        return 1
    else:
        return Fact(x-1)*x


def nCr(n,r):
    return Fact(n)/(Fact(r)*(Fact(n-r)))

def nPr(n,r):
    return Fact(n)/Fact(n-r)


def FreshDeck():
    L=[]
    i=0
    k=1
    while k<14:   
        k=k+1   
        L.append(Card(k,'h'))
        i = i +1
        L.append(Card(k,'d'))
        i = i +1
        L.append(Card(k,'c',))
        i =i +1
        L.append(Card(k,'s'))
    return L

def ShuffleDeck(N):
    M=[]
    while len(N)>0:
        x =  random.randint(0,len(N)-1)    
        M.append(N[x])
        N.remove(N[x])        
    return M

def Deal(deck,remaining_players):
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
