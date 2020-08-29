import random
import pokerfunctions as pf
import winning_hand as wh
import pygame
import time



class Player(object):
    """
    Player represented as Table, Position, Chips, Dealt_Hand, in_Hand Boolean
    """
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
    

        self.table = 1
        self.pos = ""
        self.dealt_hand = None
        self.next = ""
        self.curr_bet = 0
        self.action_count = 0
        self.in_hand = True
        self.in_game = True
        self.chips = Starting_Chips
        self.turn = False
        self.name = None
        self.coord_name = None
        self.coord_chips = None
        self.coord_action = None
        self.coord_bet = None
        self.coord_top_left = None
        self.type_score = 0
        self.sum_rank = 0
        self.winner = False
        self.all_in = False
        
    def set_pos(self,pos):
        self.pos = pos
    def get_pos(self):
        return self.pos

    def set_curr_bet(self,curr_bet):
        self.curr_bet = curr_bet
    def get_curr_bet(self):
        return self.curr_bet
    def set_chips(self,chips):
        self.chips = chips
    def get_chips(self):
        return self.chips    
    def set_turn(self,turn):
        self.turn = turn
    def get_turn(self):
        return self.turn
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_coord_name(self,coord_name):
        self.coord_name = coord_name
    def get_coord_name(self):
        return self.coord_name
    def set_coord_chips(self,coord_chips):
        self.coord_chips = coord_chips
    def get_coord_chips(self):
        return self.coord_chips
    def set_coord_action(self,coord_action):
        self.coord_action = coord_action
    def get_coord_action(self):
        return self.coord_action
    def set_coord_bet(self,coord_bet):
        self.coord_bet = coord_bet
    def get_coord_bet(self):
        return self.coord_bet
    def set_coord_top_left(self,coord_top_left):
        self.coord_top_left = coord_top_left
    def get_coord_top_left(self):
        return self.coord_top_left

class Current_Hand(object):
    def __init__(self):

        self.pre_bets = True
        self.flop_bets = False
        self.turn_bets = False
        self.river_bets = False

        self.all_in = 0
        self.hand = False
        
        self.hands = None
        self.flop = None
        self.turn = None
        self.river = None

        self.pot = 0
        self.in_hand = 0
        self.nr_winners = 0
        self.finished = False
        self.showdown = False

    def set_pre_bets(self, x):
        self.pre_bets = x
    def set_flop_bets(self, x):
        self.flop_bets = x
    def set_turn_bets(self, x):
        self.turn_bets = x
    def set_river_bets(self, x):
        self.river_bets = x

    def get_pre_bets(self):
        return self.pre_bets
    def get_flop_bets(self):
        return self.flop_bets
    def get_turn_bets(self):
        return self.turn_bets
    def get_river_bets(self):
        return self.river_bets

    def set_hands(self, hands):
        self.hands = hands
    def set_flop(self, flop):
        self.flop = flop
    def set_turn(self, turn):
        self.turn = turn
    def set_river(self, river):
        self.river = river    
    
    def get_hands(self):
        return self.hands
    def get_flop(self):
        return self.hands
    def get_turn(self):
        return self.hands
    def get_river(self):
        return self.hands
        
       
""" END OF CLASS DEFINITIONS """

def card(a, b):
    win.blit(Ad,(a,b))

def text_object(text, font, color):
    ts = font.render(text, True, color)
    return ts, ts.get_rect()
    
def message(text,a,b,size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_object(text,font,color)
    text_rect.center = (a,b)
    win.blit(text_surf,text_rect)
    pygame.display.update()

def message2(text,a,size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_object(str(text),font,color)
    text_rect.center = (a)
    win.blit(text_surf,text_rect)
    pygame.display.update()

def draw_highlight(pl):
    x = pl.get_coord_top_left()[0] - 4
    y = pl.get_coord_top_left()[1] - 4
    red = (255, 0, 0)
    pygame.draw.line(win, lblue, (x, y) , (x+168, y) , 4)
    pygame.draw.line(win, lblue, (x, y) , (x, y+88) , 4)
    pygame.draw.line(win, lblue, (x, y+88) , (x+168, y+88) , 4)
    pygame.draw.line(win, lblue, (x+168, y), (x+168, y+88) , 4)
    pygame.display.update()    
    
    return

def remove_highlight(pl,color):
    x = pl.get_coord_top_left()[0] - 4
    y = pl.get_coord_top_left()[1] - 4
    
    pygame.draw.line(win, color, (x, y) , (x+168, y) , 4)
    pygame.draw.line(win, color, (x, y) , (x, y+88) , 4)
    pygame.draw.line(win, color, (x, y+88) , (x+168, y+88) , 4)
    pygame.draw.line(win, color, (x+168, y), (x+168, y+88) , 4)
    pygame.display.update()

def clear_bet_sq(pl):
    x = pl.get_coord_bet()[0] - 18
    y = pl.get_coord_bet()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 36, 36))
    
    pygame.display.update()   
    
    return

def clear_chips_sq(pl):
    x = pl.get_coord_chips()[0] - 38
    y = pl.get_coord_chips()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 76, 36))
    
    pygame.display.update()

       
    return

def clear_name_sq(pl):
    x = pl.get_coord_name()[0] - 38
    y = pl.get_coord_name()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 76, 36))
    
    pygame.display.update()

       
    return

def clear_action_sq(pl):
    x = pl.get_coord_action()[0] - 58
    y = pl.get_coord_action()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 116, 36))
    
    pygame.display.update()   
    
    return

def draw_seat2(n,c,b,color, border,middle):
    w = 40
    h = 20
    thickness = 2

    left = min(n[0],c[0]) - w    
    up = min(n[1],b[1]) - h
    right = w + max(n[0],c[0])
    down = h + max(n[1],b[1])

    bet_top = b[1] < n[1]
    bet_left = b[0] < n[0]

    pygame.draw.rect(win, middle, (left-3,up-3,4*w+9,4*h+9)) 

    if bet_top:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h )) , (left + w, up) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, up) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), down) , thickness)
    else:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h)) , (left + w, down) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, down) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), up) , thickness)
     
    pygame.draw.line(win, border, (left,up) , (right,up) , thickness)
    pygame.draw.line(win, color, (left,up+(2*h)) , (right,up+(2*h)) , thickness)
    pygame.draw.line(win, border, (left,down) , (right,down) , thickness)

    pygame.draw.line(win, border, (left,up) , (left,down) , thickness)
    pygame.draw.line(win, border, (right,up) , (right,down) , thickness)

    ##print(left,up,right,down,bet_top,"Dimensions: ",right - left, down - up)
    
    
def draw_table():
    
    pygame.draw.line(win, white, (0,470) , (1000,470) , 10)
    x=200
    color = (x,x,x)
    pygame.draw.line(win, color, (0,471) , (1000,471) , 9)
    x=150
    color = (x,x,x)
    pygame.draw.line(win, color, (0,472) , (1000,472) , 8)
    x=100
    color = (x,x,x)
    pygame.draw.line(win, color, (0,473) , (1000,473) , 7)
    x=75
    color = (x,x,x)
    pygame.draw.line(win, color, (0,474) , (1000,474) , 6)
    x=50
    color = (x,x,x)
    pygame.draw.line(win, color, (0,475) , (1000,475) , 5)
    x=100
    color = (x,x,x)
    pygame.draw.line(win, color, (0,476) , (1000,476) , 4)
    x=150
    color = (x,x,x)
    pygame.draw.line(win, color, (0,477) , (1000,477) , 3)
    x=200
    color = (x,x,x)
    pygame.draw.line(win, color, (0,478) , (1000,478) , 2)
    
    pygame.draw.line(win, white, (0,479) , (1000,479) , 1)
    #seat 1
    try:
        player0.set_coord_name((115,260))
        player0.set_coord_chips((195,260))
        player0.set_coord_action((135,220))
        player0.set_coord_bet((215,220))
        player0.set_coord_top_left((75,200))

                    
        draw_seat2(player0.get_coord_name(),player0.get_coord_chips(),player0.get_coord_bet(),white, white, black)
        message2(player0.get_name(),player0.get_coord_name(),20, white)
        message2(str(player0.get_chips()),player0.get_coord_chips(),20, white)
    except:
        draw_seat2((115,260),(195,260),(215,220),lighter_grey, black,lighter_grey)
        message2("Seat 1",(115,260),20, fold_color)
        message2("Empty",(195,260),20, fold_color)

    #seat 2
    try:
        player1.set_coord_name((140,100))
        player1.set_coord_chips((220,100))
        player1.set_coord_action((160,140))
        player1.set_coord_bet((240,140))
        player1.set_coord_top_left((100,80))

        draw_seat2(player1.get_coord_name(),player1.get_coord_chips(),player1.get_coord_bet(),white, white, black)
        message2(player1.get_name(),player1.get_coord_name(),20, white)
        message2(str(player1.get_chips()),player1.get_coord_chips(),20, white)
    except:
        draw_seat2((140,100),(220,100),(240,140),black,white)
        message2("Seat 2",(140,100),20, fold_color)
        message2("Empty",(220,100),20, fold_color)
        

    #seat 3
    try:
        player2.set_coord_name((365,60))
        player2.set_coord_chips((445,60))
        player2.set_coord_action((385,100))
        player2.set_coord_bet((465,100))
        player2.set_coord_top_left((325,40))

        draw_seat2(player2.get_coord_name(),player2.get_coord_chips(),player2.get_coord_bet(),white, white, black)
        message2(player2.get_name(),player2.get_coord_name(),20, white)
        message2(str(player2.get_chips()),player2.get_coord_chips(),20, white)
    except:
        draw_seat2((365,60),(445,60),(465,100),lighter_grey, black,lighter_grey)
        message2("Seat 3",(365,60),20, fold_color)
        message2("Empty",(445,60),20, fold_color)
        pygame.draw.line(win, black, (345,78) , (465,78) , 2)

    #seat 4
    try:
        player3.set_coord_name((565,60))
        player3.set_coord_chips((645,60))
        player3.set_coord_action((585,100))
        player3.set_coord_bet((665,100))
        player3.set_coord_top_left((525,40))

        draw_seat2(player3.get_coord_name(),player3.get_coord_chips(),player3.get_coord_bet(),white, white, black)
        message2(player3.get_name(),player3.get_coord_name(),20, white)
        message2(str(player3.get_chips()),player3.get_coord_chips(),20, white)
    except:
        draw_seat2((565,60),(645,60),(665,100),lighter_grey, black,lighter_grey)
        message2("Seat 4",(565,60),20, fold_color)
        message2("Empty",(645,60),20, fold_color)
        pygame.draw.line(win, black, (545,78) , (665,78) , 2)
       
    #seat 5
    try:
        player4.set_coord_name((790,100))
        player4.set_coord_chips((870,100))
        player4.set_coord_action((850,140))
        player4.set_coord_bet((770,140))
        player4.set_coord_top_left((750,80))

        draw_seat2(player4.get_coord_name(),player4.get_coord_chips(),player4.get_coord_bet(),white, white, black)
        message2(player4.get_name(),player4.get_coord_name(),20, white)
        message2(str(player4.get_chips()),player4.get_coord_chips(),20, white)
    except:
        draw_seat2((790,100),(870,100),(770,140),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(754,84,154,74))
        message2("Seat 5",(830,106),20, fold_color)
        message2("Empty",(830,134),20, fold_color)
        pygame.draw.line(win, light_grey, (770,118) , (890,118) , 2)

    #seat 6   
    try:
        player5.set_coord_name((815,220))
        player5.set_coord_chips((895,220))
        player5.set_coord_action((875,260))
        player5.set_coord_bet((795,260))
        player5.set_coord_top_left((775,200))

        draw_seat2(player5.get_coord_name(),player5.get_coord_chips(),player5.get_coord_bet(),white, white, black)
        message2(player5.get_name(),player5.get_coord_name(),20, white)
        message2(str(player5.get_chips()),player5.get_coord_chips(),20, white)
    except:
        draw_seat2((815,220),(895,220),(795,260),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(779,204,154,74))
        message2("Seat 6",(855,226),20, fold_color)
        message2("Empty",(855,254),20, fold_color)
        pygame.draw.line(win, light_grey, (795,238) , (915,238) , 2)
        
    #seat 7
    try:
        player6.set_coord_name((790,380))
        player6.set_coord_chips((870,380))
        player6.set_coord_action((850,340))
        player6.set_coord_bet((770,340))
        player6.set_coord_top_left((750,320))

        draw_seat2(player6.get_coord_name(),player6.get_coord_chips(),player6.get_coord_bet(),white, white, black)
        message2(player6.get_name(),player6.get_coord_name(),20, white)
        message2(str(player6.get_chips()),player6.get_coord_chips(),20, white)
    except:
        draw_seat2((790,380),(870,380),(770,340),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(754,324,154,74))
        message2("Seat 7",(830,346),20, fold_color)
        message2("Empty",(830,374),20, fold_color)
        pygame.draw.line(win, light_grey, (770,358) , (890,358) , 2)

    #seat 8
    try:
        player7.set_coord_name((565,420))
        player7.set_coord_chips((645,420))
        player7.set_coord_action((625,380))
        player7.set_coord_bet((545,380))
        player7.set_coord_top_left((525,360))

        draw_seat2(player7.get_coord_name(),player7.get_coord_chips(),player7.get_coord_bet(),white, white, black)
        message2(player7.get_name(),player7.get_coord_name(),20, white)
        message2(str(player7.get_chips()),player7.get_coord_chips(),20, white)
    except:
        draw_seat2((565,420),(645,420),(545,380),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(529,364,154,74))
        message2("Seat 8",(605,386),20, fold_color)
        message2("Empty",(605,414),20, fold_color)
        pygame.draw.line(win, light_grey, (545,398) , (665,398) , 2)

    #seat 9
    try:
        player8.set_coord_name((365,420))
        player8.set_coord_chips((445,420))
        player8.set_coord_action((425,380))
        player8.set_coord_bet((345,380))
        player8.set_coord_top_left((325,360))

        draw_seat2(player8.get_coord_name(),player8.get_coord_chips(),player8.get_coord_bet(),white, white, black)
        message2(player8.get_name(),player8.get_coord_name(),20, white)
        message2(str(player8.get_chips()),player8.get_coord_chips(),20, white)
    except:
        draw_seat2((365,420),(445,420),(345,380),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(329,364,154,74))
        message2("Seat 9",(405,386),20, fold_color)
        message2("Empty",(405,414),20, fold_color)
        pygame.draw.line(win, light_grey, (345,398) , (465,398) , 2)

    #seat 10
    try:
        player9.set_coord_name((140,380))
        player9.set_coord_chips((220,380))
        player9.set_coord_action((160,340))
        player9.set_coord_bet((240,340))
        player9.set_coord_top_left((100,320))

        draw_seat2(player9.get_coord_name(),player9.get_coord_chips(),player9.get_coord_bet(),white,white, black)
        message2(player9.get_name(),player9.get_coord_name(),20, white)
        message2(str(player9.get_chips()),player9.get_coord_chips(),20, white)
    except:
        draw_seat2((140,380),(220,380),(240,340),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(104,324,154,74))
        message2("Seat 10",(180,346),20, fold_color)
        message2("Empty",(180,374),20, fold_color)
        pygame.draw.line(win, light_grey, (120,358),(240,358) , 2)

               
        pygame.display.update()

def show_click_fold():
    print("show click fold/check")
    pygame.draw.rect(win,light_grey,(250,510,100,60))
    pygame.display.update()
    pygame.time.wait(150)
    return

def show_click_check():
    print("show click check/call")
    pygame.draw.rect(win,light_grey,(400,510,100,60))
    pygame.display.update()
    pygame.time.wait(150)
    return

def show_click_bet():
    print("show click bet/raise")
    pygame.draw.rect(win,light_grey,(550,510,100,60))
    pygame.display.update()
    pygame.time.wait(150)
    return

def reset_action_count():
    for p in Player._registry:
        p.action_count = 0
        
    return

def select_next_player():
    for p in Player._registry:
        if p.turn == True:
                       
            globals()[p.next].set_turn(True)
            p.set_turn(False)
            return

def show_folded():
    for p in Player._registry:
        if p.in_game and not p.in_hand:
            message2("Folded",p.get_coord_action(),20, fold_color)
            remove_highlight(p, lighter_grey)
    return

def update_seat_info(pl):
    print("Entered bet amount update")
    if not pl.in_game:
        return
    clear_bet_sq(pl)
    if pl.curr_bet == 0:
        message2(pl.get_pos(),pl.get_coord_bet(),16, white)      ### D, SB, BB
    else:
        message2(pl.get_curr_bet(),pl.get_coord_bet(),16, red) ###show bet

    if pl.in_hand:
        clear_chips_sq(pl)        
        message2(pl.get_chips(),pl.get_coord_chips(),20, white) ###show chips
         
        message2(pl.get_name(),pl.get_coord_name(),20, white) ###show name
    else:
        message2(pl.get_chips(),pl.get_coord_chips(),20, fold_color) ###show chips
         
        message2(pl.get_name(),pl.get_coord_name(),20, fold_color) ###show name
        message2("Folded",pl.get_coord_action(),16, fold_color) ###folded
        remove_highlight(pl, white)

    pygame.draw.rect(win,black,(430,317,140,26))            ###delete pot
    pygame.draw.line(win,yellow,(429,316),(570,316),2)
    pygame.draw.line(win,yellow,(429,342),(570,342),2)
    pygame.draw.line(win,yellow,(429,342),(429,316),2)
    pygame.draw.line(win,yellow,(570,316),(570,342),2)
    message("POT: "+str(current.pot), 500, 332, 20, white)  ###show pot
    pygame.display.update()
    return
    
def show_current_player(pl):
    print("in current player loop")

    #### Shows current player's hand and betting options
    
    win.blit(pl.dealt_hand.card1.image,(5+(card_width * 0), display_height - 115))
    win.blit(pl.dealt_hand.card2.image,(10+(card_width * 1), display_height - 115))     
    
    ### Fold Button
    pygame.draw.rect(win,white,(250,510,100,60))
    message("Fold",300, 540, 20, black)

    ### Call/Check Button
    pygame.draw.rect(win,white,(400,510,100,60))
        
    if current.largest_bet == 0 or pl.curr_bet == current.largest_bet:
        message("Check",450, 540, 20, black)
    else:
        message("Call: "+str(current.largest_bet-pl.curr_bet),450, 540, 20, black)

    ### Bet/Raise Button    
    pygame.draw.rect(win,white,(550,510,100,60))
    
    if current.largest_bet == 0:
        message("Bet: "+str(BB),600, 540, 20, black)
        
    else:
        message("Raise",600, 540, 20, black)
       

    pygame.display.update()
    
    return
            
def wait_for_action(pl):
    print("Waiting for action:")
    clear_action_sq(pl)
    message2("TO ACT...",pl.get_coord_action(),20, yellow)
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
##                if current.in_hand < 2:
##                    current.finished = True
                if current.in_hand - current.all_in < 2:
                    current.showdown = True
                show_click_fold()
                pl.action_count += 1
                if current.largest_bet == 0:
                    clear_action_sq(pl)
                    message2("Checked",pl.get_coord_action(),20, white)  ### update action
                    clear_bet_sq(pl)
                    message2(pl.get_pos(),pl.get_coord_bet(),20, white)  ### display D, SB or BB for next round
                    
                else:
                    clear_action_sq(pl)
                    message2("Folded",pl.get_coord_action(),16, fold_color) ### update action
                    
                    clear_chips_sq(pl)
                    
                    pl.in_hand = False
                    current.in_hand -= 1
                    
                    clear_bet_sq(pl)                    
                    draw_seat2(pl.get_coord_name(),pl.get_coord_chips(),pl.get_coord_bet(),white, white,black) ### show out of hand 
                    message2(pl.get_pos(),pl.get_coord_bet(),20, white)  ### display D, SB or BB for next round
                    message2(pl.get_name(),pl.get_coord_name(),20, fold_color)
                    message2(pl.get_chips(),pl.get_coord_chips(),20, fold_color)
                    
                    
                
                pygame.display.update()
                return
            if 400 < mouse[0] < 500 and 510 < mouse[1] < 570:
##                if current.in_hand < 2:
##                    current.finished = True
                if current.in_hand - current.all_in < 2:
                    current.showdown = True
                show_click_check()
                pl.action_count += 1
                if current.largest_bet == 0:
                    
                    clear_action_sq(pl)
                    message2("Checked",pl.get_coord_action(),16, light_grey) ### update action
                    clear_bet_sq(pl)
                    message2(pl.get_pos(),pl.get_coord_bet(),20, white)  ### display D, SB or BB for next round
                else:
                    
                    if pl.curr_bet < current.largest_bet:
                        clear_chips_sq(pl)
                        pl.curr_bet += min((current.largest_bet - pl.curr_bet),pl.chips)
                        current.pot += min((current.largest_bet - pl.curr_bet),pl.chips)                        
                        pl.chips -= min((current.largest_bet - pl.curr_bet),pl.chips)

                        clear_action_sq(pl)
                        if pl.chips == 0:
                            message2("ALL IN!",pl.get_coord_action(),16, yellow)  ### update action
                            print("ALLL INNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
                            pl.all_in = True
                            current.all_in += 1
                        else:                        
                            message2("Called",pl.get_coord_action(),16, light_grey)  ### update action
                        
                    
                    update_seat_info(pl)
                pygame.display.update()
                return
            if 550 < mouse[0] < 650 and 510 < mouse[1] < 570:
##                if current.in_hand < 2:
##                    current.finished = True
                if current.in_hand - current.all_in < 2:
                    current.showdown = True
                show_click_bet()
                pl.action_count += 1
                if current.largest_bet == 0:
                    pl.curr_bet += min(pl.chips, BB) 
                    current.pot += min(pl.chips, BB) 
                    pl.chips -= min(pl.chips, BB) 
                    current.largest_bet = pl.curr_bet                    
                    clear_action_sq(pl)
                    if pl.chips == 0:
                        message2("ALL IN!",pl.get_coord_action(),16, yellow)  ### update action
                        pl.all_in = True
                        current.all_in += 1
                    else:    
                        message2("Bet",pl.get_coord_action(),16, light_grey)  ### update action
                    
                    update_seat_info(pl)
                else:
                    pl.curr_bet += min(pl.chips, current.largest_bet + BB)
                    current.pot += min(pl.chips, current.largest_bet + BB)
                    pl.chips -= min(pl.chips, current.largest_bet + BB)                    
                    current.largest_bet = pl.curr_bet
                    
                    clear_action_sq(pl)
                    if pl.chips == 0:
                        message2("ALL IN!",pl.get_coord_action(),16, yellow)  ### update action
                        pl.all_in = True
                        current.all_in += 1
                    else:
                        message2("Raised",pl.get_coord_action(),16, light_grey) ### update action
                    
                    update_seat_info(pl)
                
                pygame.display.update()
                return                
    
def more_betting():
    print("in more betting")
    if current.showdown:
        current.set_pre_bets(False)                
        current.set_flop_bets(False)
        current.set_turn_bets(False)
        current.set_river_bets(False)
        return

    if current.in_hand < 2:
        current.finished = True
        current.set_pre_bets(False)                
        current.set_flop_bets(False)
        current.set_turn_bets(False)
        current.set_river_bets(False)
        for p in Player._registry:
                if p.turn:
                    p.chips += current.pot
                    current.pot = 0
                    print("pot to blind")
                    return
        
                     

    show_folded()
    for p in Player._registry:
        if p.turn == True:
            if p.in_hand == False or p.all_in or not p.in_game:
                select_next_player()
                break
            show_current_player(p)  
            draw_highlight(p)
            
            print("largest bet: ", current.largest_bet)
            print("action count: ", p.action_count)
            print("name: ", p.name)
            print("current bet: ", p.curr_bet)
            print("In hand: ", current.in_hand)
            print("All in: ", current.all_in)
            
           
            if p.action_count == 0:               
                    
                wait_for_action(p)
                remove_highlight(p, lblue)
                globals()[p.next].set_turn(True)
                p.set_turn(False)
                return
                
            elif p.curr_bet < current.largest_bet:             
                    
                wait_for_action(p)
                remove_highlight(p, lblue)
                globals()[p.next].set_turn(True)
                p.set_turn(False)
                return
                
            else:
                current.set_pre_bets(False)                
                current.set_flop_bets(False)
                current.set_turn_bets(False)
                current.set_river_bets(False)

                current.largest_bet = 0
                reset_action_count()
                                
                for p in Player._registry:
                    p.set_turn(False)
                    update_seat_info(p)
                    if p.get_pos() == "SB":

                        p.set_turn(True)
                    if p.in_game:
                        p.set_curr_bet(0)
                        clear_bet_sq(p)
                        clear_action_sq(p)
                        remove_highlight(p, lblue)
                        message2(p.get_pos(),p.get_coord_bet(),20, white)
                return
            
        
        
            return
                               
        
def river_loop():
    
    win.blit(current.river.image,(gap+(card_width * 8), int(display_height*0.3)))
    pygame.display.update()    

    while current.get_river_bets():
        
        more_betting()
        
def turn_loop():
    
    win.blit(current.turn.image,(gap+(card_width * 7), int(display_height*0.3)))
    pygame.display.update()

    while current.get_turn_bets():
        
        more_betting()

def flop_loop():
    print("Entered flop_loop")

    win.blit(current.flop.card1.image,(gap+(card_width * 4), int(display_height*0.3)))
    win.blit(current.flop.card2.image,(gap+(card_width * 5), int(display_height*0.3)))
    win.blit(current.flop.card3.image,(gap+(card_width * 6), int(display_height*0.3)))
    pygame.display.update()

    while current.get_flop_bets():
        
        more_betting()
        
def pre_flop_loop():
    print("Entered pre_flop_loop")    

    while current.get_pre_bets():
        
        more_betting()
        print("pre loop, in hand: ", current.in_hand)

def draw_empty_seat(pl):
        pl.get_coord_name()
        pl.get_coord_chips()        
        pl.get_coord_bet()
        x = pl.get_coord_top_left()[0]
        y = pl.get_coord_top_left()[1]

        remove_highlight(pl, lighter_grey)
        draw_seat2(pl.get_coord_name(),pl.get_coord_chips(),pl.get_coord_bet(),light_grey, black,light_grey)
        pygame.draw.rect(win, black,(x+4,y+4,154,74))
        message2("Seat 10",(x + 80,y + 26),20, fold_color)
        message2("Empty",(x + 80,y + 54),20, fold_color)
        pygame.draw.line(win, light_grey, (x + 20,y + 38),(x + 140,y + 38) , 2)
        pygame.display.update()
        return

def draw_seat(pl):
        pl.get_coord_name()
        pl.get_coord_chips()        
        pl.get_coord_bet()
        x = pl.get_coord_top_left()[0]
        y = pl.get_coord_top_left()[1]

        
        draw_seat2(pl.get_coord_name(),pl.get_coord_chips(),pl.get_coord_bet(),white, white, black)
        message2(pl.get_name(),pl.get_coord_name(),20, white)
        message2(str(pl.get_chips()),pl.get_coord_chips(),20, white)
        remove_highlight(pl, lblue)
        pygame.display.update()
        return
            
def prepare_new_hand():
    
    print("preparing new hand")
    hands, flop, turn, river = shuffle()
    
    current.set_pre_bets(True)
    current.finished = False
    current.showdown = False
    current.all_in = 0
    current.in_hand = 0
    current.nr_winners = 0
    
    current.set_hands(hands)
    current.set_flop(flop)
    current.set_turn(turn)
    current.set_river(river)
    
    current.largest_bet = BB
    current.pot = SB + BB   

        
    h = 0
    for i in range(Players):
        if globals()['player'+str(i)].chips == 0:
            globals()['player'+str(i)].in_game = False
##            globals()['player'+str(i)].pos = "OUT"
        if globals()['player'+str(i)].in_game:
            globals()['player'+str(i)].dealt_hand = hands[h]
            h += 1

    reset_turn()
    for p in Player._registry:
        print("Position: ", p.pos, "   ", p.in_game)
    set_dealer("D")
    for p in Player._registry:
        print("Position: ", p.pos, "   ", p.in_game)
    set_small()
    for p in Player._registry:
        print("Position: ", p.pos, "   ", p.in_game)
    set_big()
    for p in Player._registry:
        print("Position: ", p.pos, "   ", p.in_game)
    set_first_to_act()

    show_blinds()       
    
    win.blit(pygame.image.load('Cards_png/table_new3.png'),(290,140 ))
    
    current.set_flop_bets(True)    
    return

def reset_turn():
    for p in Player._registry:
        p.set_turn(False)
    return
    
def set_dealer(pos):

    for p in Player._registry:
        if p.pos == pos:
            globals()[p.next].pos = pos
            p.pos = ""
            dealer_plus1 = p.next
            print("pos found")
            break

    if globals()[dealer_plus1].in_game:
        return
    else: set_dealer(pos)

    return

def set_small():

    for p in Player._registry:
        if p.pos == "D":
            globals()[p.next].pos = "SB"
            small = p.next
            print("D found")
            break

    if globals()[small].in_game:
        return
    else:
        set_dealer("SB")
        
    return

def set_big():

    for p in Player._registry:
        if p.pos == "SB":
            globals()[p.next].pos = "BB"
            big = p.next
            print("SB found")
            break

    if globals()[big].in_game:
        return
    else:
        set_dealer("BB")
        
    return

def set_first_to_act():

    for p in Player._registry:
        if p.pos == "BB":
            globals()[p.next].set_turn(True)
            p.set_turn(False)
            first = p.next
            print("BB found")
            break

    if globals()[first].in_game:
        show_current_player(globals()[first])
        return
    else:
        set_next_turn()

    return

def set_next_turn():

    for p in Player._registry:
        if p.turn:
            globals()[p.next].set_turn(True)
            p.set_turn(False)
            plus1 = p.next
            print("turn found")
            break

    if globals()[plus1].in_game:
        show_current_player(globals()[plus1])
        return
    else: set_next_turn()

    return

def show_blinds():
    for p in Player._registry:

        if not p.in_game:
            draw_empty_seat(p)
        else:
            draw_seat(p)       
            p.in_hand = True        
            p.winner = False
            p.all_in = False
            p.curr_bet = 0
            p.action_count = 0
            current.in_hand += 1
            
            if p.pos == "D":       
                message2("Dealer",p.get_coord_action(),16, light_grey)
            
            if p.pos == "SB":
                message2("Small Blind",p.get_coord_action(),16, light_grey)
                p.set_curr_bet(SB)
                p.chips -= SB
                message2(p.get_curr_bet(),p.get_coord_bet(),16, red)

            if p.pos == "BB":
                message2("Big Blind",p.get_coord_action(),16, light_grey)
                p.set_curr_bet(BB)
                p.chips -= BB
                message2(p.get_curr_bet(),p.get_coord_bet(),16, red)           
    return
    
    
        
def hand_loop():
    
    global clock

    tick_count = 0

    current.hand = True
    
    while current.hand:

        pygame.time.delay(50)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        while current.get_pre_bets():
            
            pre_flop_loop()
        print("Showdown: ", current.showdown, "   Finished: ", current.finished)
        if current.finished:
            break
        current.set_flop_bets(True)
        
        while current.get_flop_bets(): 

            flop_loop()
        print("Showdown: ", current.showdown, "   Finished: ", current.finished)
        if current.finished:
            break
            
        current.set_turn_bets(True)
        
        while current.get_turn_bets():                              
            
            turn_loop()
        print("Showdown: ", current.showdown, "   Finished: ", current.finished)
        if current.finished:
            break
                                   
        current.set_river_bets(True)
       
        while current.get_river_bets():                              
            
            river_loop()
        print("Showdown: ", current.showdown, "   Finished: ", current.finished)
                        
        
        print("river loop finished")
        

    #### EVAL HAND ####

        winner()
        current.hand = False
        
    prepare_new_hand()
        
    hand_loop()
    return

def winner():
    print("entered winner loop")    
    
    m=0
    sr = 0
    for p in Player._registry:
        if p.in_hand:
            x=[]
            
            x.append(str(p.dealt_hand.card1))
            x.append(str(p.dealt_hand.card2))
            x.append(str(current.flop.card1))
            x.append(str(current.flop.card2))
            x.append(str(current.flop.card3))
            x.append(str(current.turn))
            x.append(str(current.river))

            hand_type, best = wh.eval(x)
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

            p.type_score = type_score
            p.sum_rank = pf.sum_rank(best)

            m = max(m, type_score)
            
                  
            
            print(best)

    for p in Player._registry:
        if p.type_score == m:
            sr = max(sr, p.sum_rank)

    for p in Player._registry:
        if p.type_score == m and p.sum_rank == sr:
            p.winner = True
            current.nr_winners +=1
        print(p.winner)
            
    for p in Player._registry:
        if p.winner:
            p.chips = p.chips + (current.pot / current.nr_winners)
            print(p.chips)
            print(current.pot)
            print(current.nr_winners)
            update_seat_info(p)
            message2("WINNER",p.get_coord_action(),16, yellow)
            pygame.time.wait(500)
            clear_action_sq(p)
            message2("WINNER",p.get_coord_action(),16, yellow)
            pygame.time.wait(400)
            clear_action_sq(p)
            message2("WINNER",p.get_coord_action(),16, yellow)
            pygame.time.wait(300)
            clear_action_sq(p)
            message2("WINNER",p.get_coord_action(),16, yellow)
            pygame.time.wait(200)
            clear_action_sq(p)
        
      
    
    print(current.nr_winners)    
    
    return

def shuffle():

    """ SHUFFLE DECK """

    Deck_Fresh =pf.FreshDeck()
    Deck_Shuffled = pf.ShuffleDeck(Deck_Fresh)

    """ DEAL HANDS """

    hands, DECK = pf.Deal(Deck_Shuffled,Players)

    for index in range(len(hands)):
        print(hands[index])

    """Deal community cards"""

    flop, DECK = pf.Deal_Flop(DECK)
    turn = DECK[0]
    river = DECK[1]

    print("Flop:")
    print (flop)
    print("Turn:")
    print(turn)
    print("River:")
    print(river)

    return hands, flop, turn, river

################################################################################################

""" NUMBER OF SEATS / CHIPS / BLINDS """
Players = 8 #int(input("Enter number of Players: "))
Starting_Chips = 3000 #int(input("Starting Chips: "))
SB = 25
BB = 50

""" CONSTANTS """

display_width = 1000
display_height = 600
card_width = 78
card_height = 106
gap = 2

""" COLOURS """

white = (255, 255, 255)
light_grey = (150,150,150)
lighter_grey = (222,222,222)

fold_color = (155,66,44)
black = (33, 33, 33)
green = (40,80,20)
lblue = (88, 133, 255)
yellow = (255,200,50)
red = (255,10,20)

""" INITIATE PLAYERS """

for i in range(Players):
    globals()['player'+str(i)] = Player()    
    
    if i == Players - 1:
        globals()['player'+str(i)].next = 'player'+str(0)
    else:
        globals()['player'+str(i)].next = 'player'+str(i+1)    
    
try:
    player0.name = "Ian"
except: a = 1
try:
    player1.name = "Garth"
except: a = 1
try:
    player2.name = "Tony"
except: a = 1
try:
    player3.name = "Jimmy"
except: a = 1
try:
    player4.name = "Edu"
except: a = 1
try:
    player5.name = "Jono"
except: a = 1
try:
    player6.name = "Oli"
except: a = 1
try:
    player7.name = "Vargas"
except: a = 1
try:
    player8.name = "Diego"
except: a = 1
try:
    player9.name = "Juan"
except: a = 1


""" DEFINE GLOBALS """

player0.pos = "D"
current = Current_Hand()      



""" LAUNCH PYGAME"""
pygame.init()
clock = pygame.time.Clock()


""" DRAW TABLE """
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("POKER")

x = pygame.image.load('Cards_png/download2.jpe')
y = pygame.image.load('Cards_png/table.png')
##print("Width: ",y.get_width())
##print("Height: ",y.get_height())
win.blit(x ,(0, 0))
win.blit(x ,(474, 0))
win.blit(x ,(948, 0))
win.blit(y ,(180, 85))


draw_table()
prepare_new_hand()

    
""" START HAND """        
##for p in Player._registry:
##   
##    print (p.name)
##    print(p.dealt_hand)
##    print(p.get_turn())


hand_loop()
pygame.display.update()


   

    #message(str(clock.get_time),10,10,20)
    

    
    




pygame.quit()
quit()



        

    
