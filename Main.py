import pygame
import pokerfunctions as pf
from betting import more_betting
from table import table, Table
from colours import white, yellow, all_in
from hands import Hand, Pot

def prepare_new_hand():
    global current
    print("preparing new hand")

    table.move_dealer()
    
    for p in table.players:
        p.folded = False
        p.all_in = False
        p.bet = 0
        if p.chips == 0:
            current.out.append(p)
       
    for p in current.out:
        table.players.remove(p)

    table.update()
        
    if len(table.players) == 1:
        end_game_loop()
    
    
           
    current = Hand()

    for k, v in current.starting_chips.items():
        print(k,':',v)

    print(current.flop)
    print(current.turn)
    print(current.river)    
    
    table.show_blinds(current.SB, current.BB)
    Table.clear_pot()
        
def hand_loop():
    
    global clock

    tick_count = 0

    hand_finished = False
    
    while not hand_finished:

        

        pygame.time.delay(50)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        while current.pre_bets:
            pre_flop_loop()
## FLOP
        check_chip_total()
        if current.finished:
            break
        if not current.showdown:
            current.flop_bets = True

        Table.show_flop(current)
        pygame.time.delay(1000)
        
        while current.flop_bets:
            flop_loop()
## TURN     
        check_chip_total()
        if current.finished:
            break
        if not current.showdown:
            current.turn_bets = True

        Table.show_turn(current)
        pygame.time.delay(1000)
        
        while current.turn_bets:
            turn_loop()
## RIVER    
        check_chip_total()
        if current.finished:
            break
        if not current.showdown:
            current.river_bets = True

        Table.show_river(current)
        pygame.time.delay(1000)
        
        while current.river_bets:
            river_loop()
        print("river loop finished")
        
## EVAL HAND       
        check_chip_total()
        create_pot()
        winner_loop()
        hand_finished = True
        
    prepare_new_hand()
    check_chip_total() 
    hand_loop()
    return

def pre_flop_loop():
    print("Entered pre_flop_loop")    

    while current.pre_bets:
        
        more_betting(current)
        
    contenders_pre_flop = current.remaining.copy()
    
    for p in current.all_in:
        if p in current.remaining:
            current.pots.append(Pot(current.starting_chips[p.name], contenders_pre_flop))
            current.remaining.remove(p)
      
    print('Remaining:', current.remaining)
    print('Folded:', current.folded)
    print('All_in:', current.all_in)
    
def flop_loop():
    print("Entered flop_loop")

    
    for p in table.players:
        p.cards = str(p.hand.card1), str(p.hand.card2), str(current.flop.card1), str(current.flop.card2), str(current.flop.card3)
        p.eval = pf.eval(p.cards)[0]
        
    while current.flop_bets:
        
        more_betting(current)

    contenders_flop = current.remaining.copy()
    
    for p in current.all_in:
        if p in current.remaining:
            current.pots.append(Pot(current.starting_chips[p.name], contenders_flop))
            current.remaining.remove(p)
           

    print('Remaining:', current.remaining)
    print('Folded:', current.folded)
    print('All_in:', current.all_in)
 
def turn_loop():
    print("Entered turn_loop")
    
    for p in table.players:
        p.cards = p.cards + (str(current.turn),)
        p.eval = pf.eval(p.cards)[0]        
    
    while current.turn_bets:
        
        more_betting(current)

    contenders_turn = current.remaining.copy()
    
    for p in current.all_in:
        if p in current.remaining:
            current.pots.append(Pot(current.starting_chips[p.name], contenders_turn))
            current.remaining.remove(p)

    print('Remaining:', current.remaining)
    print('Folded:', current.folded)
    print('All_in:', current.all_in)

def river_loop():
    print("Entered river_loop")
    
    for p in table.players:
        p.cards = p.cards + (str(current.river),)
        print(p.name, p.cards)
        p.eval, p.sum_rank = pf.eval(p.cards)
        p.type_score = p.hand_value(p.eval)
               
             
    while current.river_bets:
        
        more_betting(current)


    print('Remaining:', current.remaining)
    print('Folded:', current.folded)
    print('All_in:', current.all_in)


def create_pot():
    contenders_river = current.remaining.copy()
    
    for p in current.all_in:
        if p in current.remaining:
            current.pots.append(Pot(current.starting_chips[p.name], contenders_river))
            current.remaining.remove(p)

    current.pots.append(Pot(current.max_bet, contenders_river))            



def winner_loop():
    print("entered winner loop")
    print('===================================')
    print('Number of pots:', len(current.pots))
    print('Pot Total:', current.pot)
    
    for p in table.players:
        p.cards = (str(p.hand.card1), str(p.hand.card2),\
            str(current.flop.card1), str(current.flop.card2),str(current.flop.card3),\
            str(current.turn),str(current.river))
        print(p.name, p.cards)
        p.eval, p.sum_rank = pf.eval(p.cards)
        p.type_score = p.hand_value(p.eval)
    
    current.pots = sorted(current.pots)
    paid = 0
    for pot in current.pots:
        pot.chips_committed -= paid
        paid += pot.chips_committed
        pot()
        print('Pot total:', pot.pot_total, pot.contenders)
        
        
        for winner in pot.winners:
            print(winner, 'received', pot.pot_total / len(pot.winners), 'chips' )
            winner.chips += pot.pot_total / len(pot.winners)
            
            current.pot -= pot.pot_total / len(pot.winners)
            winner.update_chips()

    residual_winners = current.pots[-1].winners
    residual_pot_share = current.pot / len(residual_winners)

    for p in residual_winners:
        p.chips +=residual_pot_share
        current.pot -=residual_pot_share
    
    print('pot:', current.pot)
               
    
def check_chip_total():
    print('pot:', current.pot)
    total = current.pot
    for p in table.players:       
        total += p.chips
        print(p.name, ':', p.chips)

    
        
    if table.total_chips+5 > total > table.total_chips-5:
        print('Chips ok....avg chips:', total / len(table.players))
    else:
        print('avg chips:', total / len(table.players))
        raise ValueError('chips dont add up')
        

    
def end_game_loop():
    table.players[0].seat.update_action('WINNER!!!', 22, yellow)
    pygame.event.clear()
    while True:
        event3 = pygame.event.wait()
        if event3.type == pygame.QUIT:
            pygame.quit()
            quit()


##for p in table.players:
##    p.seat.draw()
##    p()
            
############ START HAND LOOP #########

##start_screen_loop()
current = Hand()

table.update()
table.show_blinds(current.SB, current.BB)
hand_loop()




        


