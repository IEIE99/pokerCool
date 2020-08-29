
import pygame
from colours import white, fold_color, yellow



def wait_for_action():
    
    pygame.display.update()
    pygame.event.clear()
    while True:
        event3 = pygame.event.wait()
        if event3.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event3.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()            
            if 250 < mouse[0] < 350 and 510 < mouse[1] < 570:
                return check_fold
            if 400 < mouse[0] < 500 and 510 < mouse[1] < 570:             
                return call_check
            if 550 < mouse[0] < 650 and 510 < mouse[1] < 570:                  
                return raise_bet           
    
def more_betting(current):
    
    for p in current.players:

        if len(current.all_in) >= len(current.remaining):
            current.showdown = True
            showdown(current)
            return

        if len(current.players) - current.folded_count == 1:
            no_showdown(current)       
            return
       
        if current.small_blind:
            current.small_blind = False
            continue
        
        if current.big_blind or p.folded or p.all_in:
            current.big_blind = False
            continue

        if not p.action_count == 0 and current.largest_bet == p.bet:
            current.pre_bets = False               
            current.flop_bets = False
            current.turn_bets = False            
            current.river_bets = False
            
            reset_betting(current)
            return            
        
        p.show(current)
        wait_for_action()(p, current)
        p.seat.show_pot(current.pot)
        p.action_count +=1
        
       

def check_fold(player, current):
    player()
    player.show_click_fold()
    if current.largest_bet == player.bet:
        player.seat.update_action('Checked', 16, white)
    else:
        player.folded = True            
        current.folded.append(player)
        current.remaining.remove(player)
        current.folded_count += 1
        player.seat.draw_folded_seat(player.name, player.chips)
        player.seat.update_action('Folded', 16, fold_color)
        print(current.folded_count)
        print('in:',current.remaining)
        print('out:',current.folded)
        
def call_check(player, current):
    player()
    player.show_click_check()
    if current.largest_bet == player.bet:
        player.seat.update_action('Checked', 16, white)
    elif current.largest_bet - player.bet >= player.chips:
        current.all_in.append(player)
        player.all_in = True
        current.increase_pot(current.largest_bet - player.bet, player)
    else:
        current.increase_pot(current.largest_bet - player.bet, player)
        player.seat.update_action('Called', 16, white)

def raise_bet(player, current):
    player()
    player.show_click_bet()
    if current.largest_bet == 0:
        current.increase_pot(current.BB, player)
        player.seat.update_action('Bet', 16, white)
    elif current.BB + current.largest_bet - player.bet >= player.chips:
        current.all_in.append(player)
        player.all_in = True
        current.increase_pot(current.BB + current.largest_bet - player.bet, player)
    else:
        current.increase_pot(current.BB + current.largest_bet - player.bet, player)
        player.seat.update_action('Raised', 16, white) 

def reset_betting(current):
    current.max_bet += current.largest_bet
    print('MAX:', current.max_bet)
    current.largest_bet = 0
    for p in current.players:
        p.seat.update_action('', 14, white)
        p.action_count = 0
        p.bet = 0        
        p.update_bet()


def no_showdown(current):
    current.finished = True
    current.pre_bets = False               
    current.flop_bets = False
    current.turn_bets = False
    current.river_bets = False

    for p in current.players:
        if not p in current.folded:
            print(p.chips)
            p.chips += current.pot
            print(p.chips)
            current.pot = 0
            p.update_chips()
    print("no showdown")

def showdown(current):
    current.pre_bets = False               
    current.flop_bets = False
    current.turn_bets = False
    current.river_bets = False
  

        
                      


   
