import pygame
from seats import Seat
from colours import lgrey, grey, black, red, white, lblue, name_chips

""" CONSTANTS """

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600
CARD_WIDTH = 78
CARD_HEIGHT = 106
GAP = 2

class Player():
    """
    Player represented as Table, Position, Chips, Dealt_Hand, in_Hand Boolean
    """
    
    
    def __init__(self, seat_number, name, game_window):

        self.in_hand = True
        self.name = name
        
        self.chips = 1000
        self.action = ""
        self.bet = 0
        self.hand = None
        self.pot = None

        self.game_window = game_window
        
        self.seat = Seat(seat_number, name, game_window, self.in_hand)

        self.folded = False
        self.out = False
        self.action_count = 0
        
        
        self.cards = None
        self.eval = None
        
        
      
        self.type_score = 0
        self.sum_rank = 0
        self.winner = False
        self.all_in = False

    def update_bet(self):
        self.seat.update_bet(self.bet)

    def update_chips(self):
        self.seat.update_chips(self.chips, name_chips)

    def draw_empty(self):
        Seat.draw_empty_seat(self.game_window,self.seat.number)

    def show(self, current):
        self.game_window.blit(self.hand.card1.image,(5+(CARD_WIDTH * 0), DISPLAY_HEIGHT - 115))
        self.game_window.blit(self.hand.card2.image,(10+(CARD_WIDTH * 1), DISPLAY_HEIGHT - 115))     

        self.seat.color = lgrey
        ### Fold Button        
        self.seat.draw_rect(300,540,100,60)
        self.seat.draw_msg(300, 540, "Fold", 20, black)

        ### Call/Check Button
        self.seat.draw_rect(450,540,100,60)
            
        if current.largest_bet == 0 or self.bet == current.largest_bet:
            self.seat.draw_msg(450, 540, "Check", 20, black)
        else:
            self.seat.draw_msg(450, 540, "Call: "+str(current.largest_bet-self.bet), 20, black)
            
        ### Bet/Raise Button
        self.seat.draw_rect(600,540,100,60) 
               
        if current.largest_bet == 0:
            self.seat.draw_msg(600, 540, "Bet: "+str(current.BB), 20, black)     
            
        else:
            self.seat.draw_msg(600, 540, "Raise", 20, black)

        self.seat.draw_highlight(self.name, self.chips, self.bet)
        if self.eval:
            self.seat.draw_msg(800, 540, self.eval, 20, white)
            
        pygame.display.update()

    def hand_value(self, hand_type):

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
                ].index(hand_type)

        return type_score    
            

            

            
    def show_click_fold(self):        
        self.seat.draw_rect(300,540,100,60)
        pygame.display.update()
        pygame.time.wait(150)
        return

    def show_click_check(self):        
        self.seat.draw_rect(450,540,100,60)
        pygame.display.update()
        pygame.time.wait(150)
        return

    def show_click_bet(self):
        self.seat.draw_rect(600,540,100,60)
        pygame.display.update()
        pygame.time.wait(150)
        return


        
              

        


    def __call__(self):

        self.seat.update_player_info(self.name, self.chips, self.bet)        
        
      
    def __str__(self):        
        return self.name

    def __repr__(self):        
        return self.name
            
            
        
        
